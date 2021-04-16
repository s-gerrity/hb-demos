
function Hello() {
  return (
    <ul>
      <h1> React Demo Thing </h1>
      <p>Hi World!</p>
      <p> Isn't that neat? </p>
    </ul>
  );
}

ReactDOM.render(
  <Hello />,
  document.querySelector('#root')
);
