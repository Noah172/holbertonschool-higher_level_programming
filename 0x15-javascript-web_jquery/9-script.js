#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function (data, status) {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
    $('#hello').text(data.hello);
  });
});
