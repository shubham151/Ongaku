import './App.css'

function FirstPage(){
    return(
        <>
        <div className='card'>
          
          <Lottie animationData={animationData} className='gif'/>
          <label for="file-upload" class="custom-file-upload">
          <FontAwesomeIcon icon={faFilm} />  
          {' Upload Video'}
          </label>
          <input id="file-upload" type='file'></input>
          {/* <button>Upload</button> */}
          </div>
        </>
    )
}
export default FirstPage