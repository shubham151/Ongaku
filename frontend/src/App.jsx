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
import ErrorPage from './ErrorPage'

function App() {
  const [uploadStatus, setUploadStatus] = useState('not uploaded')
  const [file, setFile] = useState(null)
  const [songs, setSongs] = useState([])
  const handleFileUpload = (upFile) => {
    setFile(upFile);
  }
  const handleFileChange = async() => {
    if(!file){
      console.log(file)
      console.log('No file chosen')
      setUploadStatus('error');
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
        // setSongs(['Count me out - Kendrick Lamar', 'So far away - Avenged Sevenfold', 'Won\'t go home without you - Maroon 5', 'Toxicity - System of a down', 'Seven Nation Army - The white stripes']);
       const v = [{ artist: 'Charli xcx',
          image: 'https://i.scdn.co/image/ab67616d0000b27388e3822cccfb8f2832c70c2e',
          songUrl:'https://api.spotify.com/v1/tracks/4w2GLmK2wnioVnb5CPQeex',
          songName: '360',
        },
        { artist:'Tinashe',
          image:'https://i.scdn.co/image/ab67616d0000b27399068b5c52ec35ec2db977a7',
          songUrl:'https://api.spotify.com/v1/tracks/6NjWCIYu1W8xa3HIvcIhd4',
          songName:'Nasty',
        },
        { artist:'Michael Marcagi',
          image:'https://i.scdn.co/image/ab67616d0000b27351ef67c49732e45cd2b26fbe',
          songUrl:'https://api.spotify.com/v1/tracks/3Pbp7cUCx4d3OAkZSCoNvn',
          songName:'Scared To Start',
          },
        { artist:'Zach Bryan',
          image:'https://i.scdn.co/image/ab67616d0000b273647ad18a07e9e939e399e5a1',
          songUrl:'https://api.spotify.com/v1/tracks/5iJKGpnFfvbjZJeAtwXfCj',
          songName:'28',
        },
        { artist:'Kendrick Lamar',
          image:'https://i.scdn.co/image/ab67616d0000b2731ea0c62b2339cbf493a999ad',
          songUrl:'https://api.spotify.com/v1/tracks/6AI3ezQ4o3HUoP6Dhudph3',
          songName:'Not Like Us',
        }]
        setSongs(v);

        setUploadStatus('uploaded')
        console.log(res.data)
        // console.log(songs)
        })
      .catch(err => {
        console.error(err)
        setUploadStatus('error')
      });
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
          {uploadStatus === 'error' && <ErrorPage/>}
        </div>
      </div>
    </>
  )
}

export default App
