import { useState } from 'react'
import './App.css'
import axios from 'axios'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilm } from '@fortawesome/free-solid-svg-icons'
import Lottie from 'lottie-react'
import animationData from './assets/video-film.json'
import FirstPage from './FirstPage'
import SecondPage from './SecondPage'

function App() {
  const [count, setCount] = useState(0)
  const [uploadStatus, setUploadStatus] = useState('not uploaded')
  const handleChange = () => {

  }
  const songs = ['Count me out - Kendrick Lamar', 'So far away - Avenged Sevenfold', 'Won\'t go home without you - Maroon 5', 'Toxicity - System of a down', 'Seven Nation Army - The white stripes']
  return (
    <>
      <div className='root'>
      <h1>Ongaku</h1>
        <div className='upload-card'>
          {uploadStatus === 'not uploaded' && <FirstPage/>}
          {/* Loading screeen for uploading */}
          {uploadStatus === 'uploaded' && <SecondPage/>}
        </div>
      </div>
    </>
  )
}

export default App
