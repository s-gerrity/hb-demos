"use strict";

$('#update-status').on('click', () => {
  // Our GET request URL will look like this:
  //       /status?order=123
  $.get('/status', { order: 123 }, (res) => {
    $('#order-status').html(res);
  });
});
