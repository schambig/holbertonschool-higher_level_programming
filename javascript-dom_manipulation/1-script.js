// Get a reference to the header element
const header = document.querySelector('header');

// Get a reference to the "Red header" div
const redHeader = document.getElementById('red_header');

/* redHeader.onclick = () => {
  header.style.color = '#FF0000';
}; */

// Add an event listener to the "Red header" div
redHeader.addEventListener('click', function() {
  // Change the color of the header when the "Red header" div is clicked
  header.style.color = '#FF0000'; // Change to red
});
