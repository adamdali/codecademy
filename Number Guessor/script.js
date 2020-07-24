let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// My Code...

const generateTarget = () => {
  return Math.floor(Math.random() * 10);
}

const compareGuesses = (human, computer, target) => {
  const humanResult = target - human
  const computerResult = target - computer
  return humanResult <= computerResult;
}

const updateScore = winner => {
  if (winner === 'human') {
    humanScore++;
  } else if (winner === 'computer') {
    computerScore++;
  }
}

const advanceRound = () => currentRoundNumber++;