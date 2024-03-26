// Get reference to `header` and `update_header` elements
const header = document.querySelector('header');
const updateHeader = document.getElementById('update_header');

/* 
updateHeader.onclick = () => {
  header.innerHTML = 'New Header!!!';
};
 */

updateHeader.addEventListener('click', () => {
  // same comment as in task 4-script.js
  header.textContent = 'New Header!!!';
  // header.innerHTML = 'New Header!!!';
});
