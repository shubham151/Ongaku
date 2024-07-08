import { useState } from 'react'
import './App.css'
import axios from 'axios'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilm } from '@fortawesome/free-solid-svg-icons'
import Lottie from 'lottie-react'
import animationData from './assets/video-film.json'
import FirstPage from './FirstPage'
import SecondPage from './SecondPage'
import LoadingPage from './LoadingPage'

function App() {
  const [uploadStatus, setUploadStatus] = useState('not uploaded')
  const [file, setFile] = useState(null)
  const [songs, setSongs] = useState([])
  const handleFileUpload = (upFile) => {
    console.log(upFile ,'up')
    setFile(upFile);
    console.log(file);  
  }
  const handleFileChange = async() => {
    console.log(file)
    if(!file){
      console.log(file)
      console.log('No file chosen')
      return;
    } else {
      const fd = new FormData();
      fd.append('file', file);

      setUploadStatus('uploading')
      
      axios.post('http://httpbin.org/post', fd, {
        onUploadProgress: (progEvent) => { console.log(progEvent.progress*100) },
        headers: {
          'Custom-Header': 'value',
        }
      })
      .then(res => {
        setSongs(['Count me out - Kendrick Lamar', 'So far away - Avenged Sevenfold', 'Won\'t go home without you - Maroon 5', 'Toxicity - System of a down', 'Seven Nation Army - The white stripes']);
        setUploadStatus('uploaded')
        console.log(res.data)
        // console.log(songs)
        })
      .catch(err => console.error(err));
    }
  }

  return (
    <>
      <div className='root'>
      <h1>Ongaku</h1>
        <div className='upload-card'>
          {uploadStatus === 'not uploaded' && <FirstPage setUStat = { handleFileChange } fileChange={ handleFileUpload } />}
          {uploadStatus === 'uploading' && <LoadingPage/>}
          {uploadStatus === 'uploaded' && <SecondPage songs = {songs}/>}
        </div>
      </div>
    </>
  )
}

export default App
