import './App.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilm } from '@fortawesome/free-solid-svg-icons'
import Lottie from 'lottie-react'
import animationData from './assets/video-film.json'
import { useState } from 'react'

function FirstPage({setUStat, fileChange}){
  const [isFileChosen, setIsFileChosen] = useState(false);

  const handleChange = (ev) => {
    const file = ev.target.files[0]
    fileChange(file);
    setIsFileChosen(true);
  }
    return(
        <div className='card'>
          <Lottie animationData={animationData} className='gif'/>
          <label for="file-upload" className="custom-file-upload">
          <FontAwesomeIcon icon={faFilm} />  
          {!isFileChosen && ' Choose a file'}
          {isFileChosen && ' File has been chosen'}
          </label>
          <div className='button-bar'>
          <input id="file-upload" type='file' onChange = { (e) => handleChange(e) }></input>
          <button disabled={!isFileChosen} className="custom-file-upload" onClick = {setUStat}>Upload</button>
          </div>
        </div>
    )
}
export default FirstPage