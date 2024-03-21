// Get a reference to the header and toggle_header elements
const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

/* 
toggleHeader.onclick = () => {
  // check if the header already has the class. If it does, remove it. If ir doesn't, add it
  header.classList.toggle('green', !header.classList.contains('green'));
  header.classList.toggle('red', !header.classList.contains('red'));
};
 */

toggleHeader.onclick = () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
};
