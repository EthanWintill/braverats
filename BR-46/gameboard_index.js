// get all player cards
const playerCards = document.querySelectorAll('.player .card');

// get all opponent cards
const opponentCards = document.querySelectorAll('.opponent .card');

// add click event listener to each card
playerCards.forEach(card => {
  card.addEventListener('click', () => {
    // move clicked card to middle of board
    card.classList.add('middle-card');

    // remove the selected opponent card from the list of available cards
    const availableOpponentCards = Array.from(opponentCards).filter(opponentCard => !opponentCard.classList.contains('right-card'));


    // wait one second and move random opponent card to right of middle card
    setTimeout(() => {
        //generate random index number based on card length
      const randomCardIndex = Math.floor(Math.random() * availableOpponentCards.length);
      const randomCard = availableOpponentCards[randomCardIndex];
      //pick a random card based off of that opponent
      
      // move selected opponent card to right of middle card
      randomCard.classList.add('right-card');
    }, 1000);
  });
});







