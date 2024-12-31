from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from social_django.utils import load_strategy  # type: ignore
from social_core.backends.google import GoogleOAuth2  # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken
import os

class GoogleAuthView(APIView):
    """
    Handle Google OAuth login flow in a single view.
    This view will either redirect to the Google OAuth login page or complete the login process.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        # This method initiates the Google OAuth process
        google_client_id = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
        redirect_uri = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI')
        
        # Get the next URL parameter, which will be the redirect URL after successful login
        next_url = request.GET.get('next', '/')
        
        # Construct the Google OAuth URL
        auth_url = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={google_client_id}&redirect_uri={redirect_uri}&scope=email&state={next_url}"

        return Response({
            "auth_url": auth_url
        })

    def post(self, request):
        # This method completes the Google OAuth login process
        code = request.data.get('code')
        if not code:
            return Response({"error": "Authorization code not provided."}, status=400)

        try:
            # Authenticate the user using the Google backend
            backend = GoogleOAuth2()
            strategy = load_strategy(request)
            user = backend.do_auth(
                access_token=None,
                code=code,
                redirect_uri=os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI')
            )

            if not user:
                return Response({"error": "Authentication failed."}, status=400)

            # Generate JWT tokens for the user
            refresh = RefreshToken.for_user(user)

            # Get the 'next' URL from the request's state parameter
            next_url = request.data.get('state', '/')

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                },
                "next": next_url  # Return the next URL to redirect to after login
            })

        except Exception as e:
            return Response({"error": str(e)}, status=400)
