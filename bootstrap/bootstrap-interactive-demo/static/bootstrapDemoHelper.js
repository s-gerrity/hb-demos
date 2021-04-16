$('div[class^="col"]').each((i, el) => {
  const color = randomColor({ format: 'hsl' });
  console.log(color);

  if (Number(color.split(',')[2].trim().replace('%)', '')) < 45) {
    $(el).css({ color: 'white' });
    $(el).addClass('dark');
  }

  $(el).css({ background: color });
});
