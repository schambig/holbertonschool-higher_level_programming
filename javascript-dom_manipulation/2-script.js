// Get a reference to the header and red_header elements
const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

// 4 ways to accomplish the same:

/* 
redHeader.onclick = () => {
  header.classList.add('red');
};
 */

/* 
function addRedClass() {
  header.classList.add('red');
}

redHeader.addEventListener('click', addRedClass);
 */

/* 
redHeader.addEventListener('click', function() {
  header.classList.add('red');
})
 */

redHeader.addEventListener('click', () => {
  header.classList.add('red');
})
