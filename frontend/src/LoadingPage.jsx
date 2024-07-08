import './App.css'
import Lottie from 'lottie-react'
import animationData from './assets/loading.json'

function LoadingPage() {
    return(
        <div className='loading-box'>
        <Lottie animationData={animationData} className='gif-load' />
        <span>Uploading Please Wait!</span>
        </div>
    )
}
export default LoadingPage