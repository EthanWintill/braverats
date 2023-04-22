
  const imgDiv = document.querySelector('.user_img');
  const img = document.querySelector('#photo');
  const file = document.querySelector('#file');
  const upload = document.querySelector('#upload');

  //if user hovers on img div, show upload
  imgDiv.addEventListener('mouseenter', function() {
    upload.style.display = "block";
  });

  //if we hover out of imgDiv
  imgDiv.addEventListener('mouseleave', function() {
    upload.style.display = "none";
  });

  file.addEventListener('change', function(){
    const chooseFile = this.files[0];

    if(chooseFile) {

      const reader = new FileReader();

      reader.addEventListener('load', function(){
        img.setAttribute('src', reader.result);
      });

      reader.readAsDataURL(chooseFile);
    }
  });
