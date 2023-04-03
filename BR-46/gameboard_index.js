// Get all the cards on the player's side
const playerCards = document.querySelectorAll('.player .faceDown');

// Add event listeners to the player's cards
playerCards.forEach(card => {
  card.addEventListener('click', () => {
    // Move the clicked card to the middle
    const middle = document.querySelector('.middle');
    card.classList.add('in-middle');
    card.classList.toggle('faceDown');
    middle.appendChild(card);
  });
});

// Get all the cards on the opponent's side
const opponentCards = document.querySelectorAll('.opponent .faceDown');

// Move a random card from the opponent's side to the middle every 3 seconds
setInterval(() => {
  const randomIndex = Math.floor(Math.random() * opponentCards.length);
  const randomCard = opponentCards[randomIndex];
  randomCard.classList.add('in-middle');
}, 3000);
