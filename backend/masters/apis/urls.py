from django.urls import path
from masters.apis.views import (
    CategoryDetailView,
    CategoryList,
    # CategoryViewSet,  # Uncomment if you want to use CategoryViewSet
)

# If you want to use CategoryViewSet with Django Rest Framework's ViewSet:
# category_details = CategoryViewSet.as_view({'get': 'list'})
# category_detail = CategoryViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    # Path for listing categories
    path('category/', CategoryList.as_view({'get': 'list'}), name='category'),

    # Path for retrieving a specific category by ID
    path('category/<id>', CategoryDetailView.as_view(), name='category_detail'),

    # Alternative paths you had commented out
    # path('category/', CategoryList.as_view()),  # Uncomment this if you want to use this route for CategoryList without specifying HTTP methods
    # path('category/<str:name>/', CategoryDetail.as_view()),  # Uncomment this if you want to use a category with name instead of id

    # Using ViewSet approach (if CategoryViewSet is defined)
    # path('category/', category_details, name='category-list'),  # Use ViewSet for list view
    # path('category/<int:id>/', category_detail, name='category-detail'),  # Use ViewSet for individual category detail
]
