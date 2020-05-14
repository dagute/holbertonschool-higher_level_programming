$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (response) => {
      $('#hello').append(response.hello);
    }
  });
});
