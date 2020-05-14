#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('green red');
  });
});
