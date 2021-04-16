const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';

const Word = (props) => {
  const charDivs = [];
  for (const [ i, letter ] of Object.entries(props.word)) {
    let displayLetter = null;
    if (props.guessedLetters.includes(letter)) {
      displayLetter = letter;
    }

    charDivs.push(
      <div
        key={i}
        className="letter-box"
      >
        {displayLetter}
      </div>
    );
  }

  return (
    <section className="word-container">
      {charDivs}
    </section>
  )
};

const Letters = (props) => {
  const letterBtns = [];
  for (const letter of ALPHABET) {
    const handleClick = () => {
      props.handleGuessLetter(letter);
    };

    letterBtns.push(
      <button
        key={letter}
        disabled={props.guessedLetters.includes(letter)}
        onClick={handleClick}
      >
        {letter}
      </button>
    );
  }

  return (
    <section className="letter-buttons">
      {letterBtns}
    </section>
  )
};


const Sharkwords = (props) => {
  const [ guessedLetters, setGuessedLetters ] = React.useState([]);
  const [ numWrong, setNumWrong ] = React.useState(0);

  const guessLetter = (letter) => {
    if (!props.word.includes(letter)) {
      setNumWrong(numWrong + 1);
    }

    setGuessedLetters(prevLetters => prevLetters.concat([letter]));
  };

  return (
    <div>
      <section id="shark-img">
        <img
          src={`/static/images/guess${numWrong}.png`}
        />
      </section>

      <Word
        word={props.word}
        guessedLetters={guessedLetters}
      />

      <Letters
        guessedLetters={guessedLetters}
        handleGuessLetter={guessLetter}
      />
    </div>
  );
}



ReactDOM.render(
  <Sharkwords word="hello" />,
  document.querySelector('#root')
);
