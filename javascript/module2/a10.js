const candidates = [];

const numOfCandidates = parseInt(prompt('How many candidates?'));
for (let i = 0; i < numOfCandidates; i++) {
  const name = prompt(`Name of candidate ${i + 1}?`);
  const candidate = {
    name: name,
    votes: 0,
  };
  candidates.push(candidate);
}

const numOfVoters = parseInt(prompt('How many voters?'));
for (let i = 0; i < numOfVoters; i++) {
  const voteName = prompt('Who do you vote for?');
  for (let candidate of candidates) {
    if (voteName === candidate.name) {
      candidate.votes++;
    }
  }
}

candidates.sort((a, b) => b.votes - a.votes);

console.log(`The winner is ${candidates[0].name.charAt(0).toUpperCase() +
candidates[0].name.slice(1).toLowerCase()} with ${candidates[0].votes} votes.`);

console.log('Results:');

for (let candidate of candidates) {
  console.log(`${candidate.name.charAt(0).toUpperCase() +
  candidate.name.slice(1).toLowerCase()}: ${candidate.votes} votes`);
}
