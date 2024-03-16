// Get a reference to the header and red_header elements
const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

/* redHeader.onclick = () => {
  header.style.color = '#FF0000';
}; */

// Use event listener to the "Red header" best practice)
redHeader.addEventListener('click', function() {
  // Change the color (to red) of the header when the "Red header" div is clicked
  header.style.color = '#FF0000';
});
