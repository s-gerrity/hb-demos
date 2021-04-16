
function Hello(props) {
  return (
    <div>
      <p>
        Hi {props.to}
      </p>
      <p>
        from {props.from}
      </p>
    </div>
  );
}

ReactDOM.render(
  <Hello to="you" from="Balloonicorn" />,
  document.querySelector('#root')
);
