import './App.css'
import Lottie from 'lottie-react'
import animationData from './assets/error.json'

function ErrorPage() {
    return(
        <div className="error">
            <Lottie animationData={animationData} className='gif-load' />
            <span>An error has occurred</span>
        </div>
    )
}

export default ErrorPage