function HelloClicker() {
  function alertMessage() {
    alert('You just handled an event!');
  }

  return (
    <button onClick={alertMessage}>
      Click me
    </button>
  );
}

ReactDOM.render(
  <HelloClicker />,
  document.getElementById('root')
);
