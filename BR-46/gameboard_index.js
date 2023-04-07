/*// get all player cards
const playerCards = document.querySelectorAll('.player .card');

// get all opponent cards
const opponentCards = document.querySelectorAll('.opponent .card');

// array to keep track of used image indices
let usedImageIndices = [];

// add click event listener to each card
playerCards.forEach(card => {
  card.addEventListener('click', () => {
    // move clicked card to middle of board
    card.classList.add('middle-card');

    // remove the selected opponent card from the list of available cards
    const availableOpponentCards = Array.from(opponentCards).filter(opponentCard => !opponentCard.classList.contains('right-card'));

    // exclude used image indices from the pool of available indices
    const availableImageIndices = Array.from({length: 8}, (_, i) => i)
      .filter(i => !usedImageIndices.includes(i));

    // wait one second and move random opponent card to right of middle card
    setTimeout(() => {
      // generate random index number based on available card and image lengths
      const randomCardIndex = Math.floor(Math.random() * availableOpponentCards.length);
      const randomCard = availableOpponentCards[randomCardIndex];
      const randomImageIndex = availableImageIndices[Math.floor(Math.random() * availableImageIndices.length)];

      // set the background image of the face-down element to the randomly selected image
      const faceDown = randomCard.querySelector('.face-down');
      faceDown.style.backgroundImage = `url(cardImages/A-${randomImageIndex}.png)`;

      // add the face-up class to the face-down element to flip it over
      faceDown.classList.add('face-up');

      // move selected opponent card to right of middle card
      randomCard.classList.add('right-card');

      // add the used image index to the array of used indices
      usedImageIndices.push(randomImageIndex);
    }, 1000);
  });
});




*/
















