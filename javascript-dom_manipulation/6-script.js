const url = 'https://swapi-api.hbtn.io/api/people/13/?format=json';

/* 
// use 'old' syntax, .then()
fetch(url)
  .then((res) => {
    if (!res.ok) throw new Error(`Sure about that URL? (${res.status})`);
    return res.json();
  })
  .then((data) => {
    const characterElement = document.getElementById('character');
    let charName = data.name;
    // characterElement.innerHTML = charName;
    characterElement.textContent = charName;
  });
 */

// use async-await, modern syntax
async function displayCharacter() {
  try {
    const res = await fetch(url);
    // console.log(res)
    if (!res.ok) throw new Error(`Sure about that URL? (${res.status})`);
    // use object destructuring to extract the name property from the object returned by res.json()
    const { name } = await res.json();
    // document.getElementById('character').innerHTML = name;
    document.getElementById('character').textContent = name;
    // line above can be done in two lines (as follows) for more readability:
    // const characterElement = document.getElementById('character')
    // characterElement.textContent = name;
  } catch (e) {
    console.error('Error:', e);
  }
}

displayCharacter();
