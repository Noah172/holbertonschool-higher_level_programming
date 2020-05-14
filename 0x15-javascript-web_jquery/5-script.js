#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(function () {
    const item = '<li>Item</li>';
    $('.my_list').append(item);
  });
});
