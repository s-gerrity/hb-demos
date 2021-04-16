"use strict";

$.get('/adjective', (response) => {
  $('#adjective').text(response);
});
