const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';

class Sharkwords extends React.Component {
  constructor(props) {
    super(props);

    // this.props.word -> word user needs to guess

    this.state = {
      guessedLetters: [],
      numWrong: 0,
    };
  }

  renderWord() {
    const charDivs = [];
    for (const [ i, letter ] of Object.entries(this.props.word)) {
      let displayLetter;
      if (this.state.guessedLetters.includes(letter)) {
        displayLetter = letter;
      }

      charDivs.push(
        <div key={i} className="letter-box">
          {displayLetter}
        </div>
      );
    }

    return charDivs;
  }

  renderLetterButtons() {
    const letterBtns = [];
    for (const letter of ALPHABET) {
      const handleClick = () => {
        this.guessLetter(letter);
      };

      letterBtns.push(
        <button
          key={letter}
          onClick={handleClick}
        >
          {letter}
        </button>
      );
    }

    return letterBtns;
  }

  guessLetter(letter) {
    this.setState((prevState) => {
      return {
        guessedLetters: prevState.guessedLetters + [letter]
      };
    });

    if (!this.props.word.includes(letter)) {
      this.setState((prevState) => {
        return {
          numWrong: prevState.numWrong + 1
        };
      });
    }
  }

  render() {
    return (
      <div>
        <section id="shark-img">
          <img
            src={`/static/images/guess${this.state.numWrong}.png`}
          />
        </section>

        <section id="word-container">
          {this.renderWord()}
        </section>

        <section id="letter-buttons">
          {this.renderLetterButtons()}
        </section>
      </div>
    );
  }
}


ReactDOM.render(
  <Sharkwords word="hello" />,
  document.querySelector('#root')
);
