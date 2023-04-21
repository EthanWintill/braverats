const editIcon = document.querySelector('.edit-icon');
const modal = document.querySelector('.modal');
const images = document.querySelectorAll('.image');
const profilePicture = document.querySelector('.profile-picture');

editIcon.addEventListener('click', () => {
  modal.style.display = 'block';
});

images.forEach((image) => {
  image.addEventListener('click', () => {
    profilePicture.src = image.src;
    modal.style.display = 'none';
  });
});

window.addEventListener('click', (event) => {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
});


