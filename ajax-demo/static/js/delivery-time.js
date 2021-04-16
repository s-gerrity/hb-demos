"use strict";

$('#delivery-form').on('submit', (evt) => {
  evt.preventDefault();

  // Get user input from a form
  const formData = {
    city: $('#city-field').val(),
    address: $('#adr-field').val()
  };

  // Send formData to the server (becomes a query string)
  $.get('/delivery-info.json', formData, (res) => {
    // Display response from the server
    alert(`This will cost $${res.cost}`);
    alert(`This will arrive in ${res.days} day(s)`);
  });
});
