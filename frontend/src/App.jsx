import { useState } from 'react'
import './App.css'
import axios from 'axios'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilm } from '@fortawesome/free-solid-svg-icons'
import Lottie from 'lottie-react'
import animationData from './assets/video-film.json'
// import FirstPage from './firstPage'


function App() {
  const [count, setCount] = useState(0)
  const songs = ['Count me out - Kendrick Lamar', 'So far away - Avenged Sevenfold', 'Won\'t go home without you - Maroon 5', 'Toxicity - System of a down', 'Seven Nation Army - The white stripes']
  return (
    <>
      <div className='root'>
      <h1>Ongaku</h1>
        <div className='upload-card'>
          {/* <FirstPage/> */}
          <div className='card'>
          
          <Lottie animationData={animationData} className='gif'/>
          <label for="file-upload" class="custom-file-upload">
          <FontAwesomeIcon icon={faFilm} />  
          {' Upload Video'}
          </label>
          <input id="file-upload" type='file'></input>
          {/* <button>Upload</button>*/}
          </div> 
          {/* <div className='table'>
            <h2>Try one of these songs!</h2>
              {songs.map((item) => (
                <span>{item}</span>
              ))}
          </div>
         <img src='https://cdn-0.studybreaks.com/wp-content/uploads/2022/11/IMG_2547.png?ezimgfmt=rs:387x258/rscb8/ngcb8/notWebP'/> */}
        </div>
      </div>
    </>
  )
}

export default App
