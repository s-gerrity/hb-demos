function Fruits() {

  const [fruits, setFruits] = React.useState([])

  React.useEffect(() => {
    $.get('/api/fruits', (result) => {
      setFruits(result);
    });
  }, [])

  const fruitListItems = []
  for (let fruit of fruits) {
    fruitListItems.push(<li key={fruit.fruit_id}>{fruit.name}</li>)
  }

  // We can also use map for a little shorter code.
  // const fruitListItems = fruits.map((fruit) => {
  //   return (<li key={fruit.fruit_id}>{fruit.name}</li>);
  // });

  if (fruits.length > 0) {
    return (
      <ul>
        {fruitListItems}
      </ul>
    );
  } else {
    return <p>Loading...</p>;
  }
}


ReactDOM.render(<Fruits />, document.getElementById('root'));
