function getRandomNum(upperLimit) {
  return Math.ceil(Math.random() * upperLimit);
}

function Die(props) {

  const [diceValue, setDiceValue] = React.useState('?')

  function roll() {
    const rollResult = getRandomNum(props.sides);
    setDiceValue(rollResult)
  }

  return (
    <button className="die" onClick={roll}>
      <i>sides={props.sides}</i>
      <b>{diceValue}</b>
    </button>
  );
}

ReactDOM.render(
  (
    <div>
      <Die sides="4" />
      <Die sides="6" />
      <Die sides="8" />
      <Die sides="10" />
      <Die sides="12" />
      <Die sides="20" />
    </div>
  ),
  document.getElementById('root')
);
