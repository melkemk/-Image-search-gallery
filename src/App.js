import { useEffect, useState } from 'react';
import { createApi } from 'unsplash-js';
import './App.css';
function AllImages(props) {
  const [images, setImages] = useState([]);
  const unsplash = createApi({ accessKey: '0ULNREq3mRIMkZQ90jCpPxV_QnvLC-smPmcEqrwio70' })

  useEffect(() => {
    unsplash.search
      .getCollections({
        query: props.value,
        page: 1,
        perPage: 10,
      })
      .then((result) => {
        const photoUrls = result.response.results.map((result) => result.preview_photos[0].urls.regular);
        setImages(photoUrls);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [unsplash.search]);

  return (
    <>
      {images.length > 0 ? (images.map((imageUrl) => (
        <img src={imageUrl} alt="A cat" />
      ))) : (<p>loading... </p>)}

    </>
  );
}




export function Search() {
  const [value, setValue] = useState('')
  const [clicked, setClicked] = useState(0)

  function handleKeyDown(e) {
    if (e.key === 'Enter') setClicked(1);
  }
  useEffect(() => {
    document.getElementById('input').addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [value]);



  return (
    <>
      <div className="search">
        Image search <br />
        <input type="text" id='input' onChange={(e) => setValue(e.target.value)} />
      </div>

      <div className='main'>
        {clicked ? (< AllImages value={value} />
        ) : (<p> </p>)}
      </div>


    </>
  )
}


// 0ULNREq3mRIMkZQ90jCpPxV_QnvLC - smPmcEqrwio70  acess
// 3ne8aoJ72oVEDHNufXvyusQ8xMFKzSebaoQ0OIuNiAY  secret