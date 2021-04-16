function adder(x, y) {
    return x + y;
}

$('#calc-form').on('submit', function (evt) {
    evt.preventDefault();

    var x = parseInt($('#x-field').val());
    var y = parseInt($('#y-field').val());

    $('#result').text(adder(x, y));

});
