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

// add the css class `.red`, the dot is not needed this is because the classList property provides
// a collection of the element's classes as a DOMTokenList object,
// and you specify the class name directly as a parameter to classList.add().
// The dot is part of the CSS syntax to denote class selectors,
// but when working with JavaScript's classList, you only provide the class name itself
redHeader.addEventListener('click', () => {
  header.classList.add('red');
})
