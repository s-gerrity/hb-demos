function JQueryWeatherAlert() {
  function alertWeather() {
    $.get('/api/weather', (data) => {
      alert(`The weather will be ${data.forecast}`);
    });
  }

  return (
    <button onClick={alertWeather}>
      Get Weather with jQuery
    </button>
  );
}

function FetchWeatherButton() {
  function alertWeather() {
    fetch('/api/weather')
    .then(response => {
      return response.json();
    })
    .then(data => {
      alert(`The weather will be ${data.forecast}`);
    });
  }

  return (
    <button onClick={alertWeather}>
      Get Weather with Fetch
    </button>
  );
}

ReactDOM.render(
  (
    <div>
      <JQueryWeatherAlert />
      <FetchWeatherButton/>
    </div>
  ),
  document.getElementById('root'),
);
