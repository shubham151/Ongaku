import './App.css'
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';


function SecondPage({ songs }){
    console.log('Songs prop:', songs);
    return(
        <><div className='table'>
            <h2>Try one of these songs!</h2>
            <Carousel>
            {songs.map((item,index) => (
                // <div className='song'>
                // <img className='thumbnail'src={item.image} />
                // <span>{item.songName + " - " + item.artist}</span>
                // </div>
                  <div key={index}>
                    <img src={item.image} alt={`Slide ${index}`} />
                    <a className="legend" href={item.songUrl}>{item.songName + " - " + item.artist}</a>
                  </div>
                ))}
              </Carousel>
            {/* ))} */}
        </div>
        {/* <img className= 'side' src='https://cdn-0.studybreaks.com/wp-content/uploads/2022/11/IMG_2547.png?ezimgfmt=rs:387x258/rscb8/ngcb8/notWebP' /> */}
        </>
    )
}
export default SecondPage