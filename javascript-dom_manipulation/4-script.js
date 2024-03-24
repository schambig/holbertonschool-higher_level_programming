// Get a reference to the header and add_item elements
const ulElement = document.querySelector('ul');
const addItem = document.getElementById('add_item');

/* 
addItem.onclick = () => {
  const newElement = document.createElement('li');
  newElement.innerHTML = 'Item';
  ulElement.appendChild(newElement);
};
 */

addItem.addEventListener('click', () => {
  // Create a new <li> element
  const newElement = document.createElement('li');

  /* Set the inner text of the new <li> element, use `textContent` instead of `innerHTML`, it is considered
  a better approach when delaing with plain text content,
  it reduces the risk of XSS (Cross-Site Scripting) atacks because it treats the content as plain text rather then HTML.
  But since here we are internally inserting a new <li> tag there's no risk to a malicious input from exterior
  so we can use both */
  // newElement.innerHTML = 'Item';
  newElement.textContent = 'Item';

  // Append the new <li> element to the <ul> element
  ulElement.appendChild(newElement);  
})
