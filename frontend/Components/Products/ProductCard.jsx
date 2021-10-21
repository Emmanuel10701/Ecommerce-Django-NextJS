import AddToCartButton from 'Components/UI/AddToCartButton';
import BuyNow from 'Components/UI/BuyNow';
import Image from 'next/image'
import { useDispatch } from 'react-redux';
import { addToCart } from "store/modules/product";

const ProductCard = ({ product }) => {
    const dispatch = useDispatch()

    const moveToCart = () => {
        console.log('clicked', product.id, product.name)
        dispatch(addToCart(1))
    }

    return (
        <div className="max-w-lg mx-auto">
            <div className="bg-white shadow-md border border-gray-200 rounded-lg max-w-full mb-5">
                <a href="#">
                    <Image
                        width="100%" height="100%" layout="responsive"
                        src={product.image}
                        alt={product.name}
                    />
                </a>
                <div className="p-5 bg-indigo-100">
                    <a href="#">
                        <h5 className="text-gray-900 font-bold text-2xl tracking-tight mb-2">
                            {product.name}
                        </h5>
                    </a>
                    <p className="font-sm text-gray-700 mb-3">
                        {product?.short_description}
                        {/* in reverse chronological order. */}
                    </p>
                    <p className='text-bold text-yellow-700 font-extrabold text-xl pb-1'>
                        <span>&#8377;</span>
                        {product?.price}
                    </p>
                    <div className="text-center space-x-10 inline-flex flex-shrink">
                        <AddToCartButton moveToCart={moveToCart} />
                        <BuyNow />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ProductCard;