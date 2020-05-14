#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
