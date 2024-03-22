// Get a reference to the header and toggle_header elements
const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');


/* toggleHeader.onclick = () => {
  // check if the header already has the class. If it does, remove it. If ir doesn't, add it
  header.classList.toggle('green', !header.classList.contains('green'));
  header.classList.toggle('red', !header.classList.contains('red'));
};


// `classList.toggle(Class Name, Force(bool))` arguments explained
//   Class Name (required):
//     - This is the name of the class you want to toggle.
//     - It's a required argument, and you must provide the class name as a string.
//   Force (optional):
//     - This argument determines whether to force adding or removing the class based on a condition.
//     - It's optional, and if not provided, the method simply toggles the class
//       (adds if it's not present, removes if it is).
//     - If true, it forces the class to be added regardless of whether it's already present.
//     - If false, it forces the class to be removed regardless of whether it's already present.
//     - If not provided, the method determines whether to add or remove the class
//       based on its current presence.
//       If the class is present, it will be removed; if it's not present, it will be added.
//       
//       Use classList.toggle() with both arguments:
//         element.classList.toggle('classname'); // Toggles the class 'classname' based on its current presence
//         element.classList.toggle('classname', true); // Always adds the class 'classname'
//         element.classList.toggle('classname', false); // Always removes the class 'classname'

 */

/* 
toggleHeader.onclick = () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
};
 */

toggleHeader.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');  
});
