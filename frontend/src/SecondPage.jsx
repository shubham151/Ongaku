import './App.css'


function SecondPage({ songs }){
    console.log('Songs prop:', songs);
    return(
        <><div className='table'>
            <h2>Try one of these songs!</h2>
            {songs.map((item) => (
                <span>{item}</span>
            ))}
        </div>
        <img src='https://cdn-0.studybreaks.com/wp-content/uploads/2022/11/IMG_2547.png?ezimgfmt=rs:387x258/rscb8/ngcb8/notWebP' /></>
    )
}
export default SecondPage