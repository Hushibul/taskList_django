console.log('Hellow World');

document.addEventListener('DOMContentLoaded', function () {
  const deleteBtn = document.querySelector('#deleteBtn');

  deleteBtn?.addEventListener('click', function (event) {
    console.log('Delete button clicked!');
  });
});
