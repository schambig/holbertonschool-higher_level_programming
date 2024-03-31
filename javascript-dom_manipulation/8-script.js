const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// fetch(url)
//   .then(res => {
//     if (!res.ok) throw new Error(res.status);
//     return res.json();
//   })
//   .then(data => {
//     const helloElement = document.getElementById('hello');
//     helloElement.innerHTML = data.hello;
//   });

async function sayHelloInFrench() {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(res.status);
    // console.log(res.json());
    const { hello } = await res.json();
    // console.log(hello);
    const helloElement = document.getElementById('hello').textContent = hello;
    // line above can be done in two lines (as follows) for more readability:
    // const helloElement = document.getElementById('hello');
    // helloElement.textContent = hello;
  } catch (e) {
    console.log('Error', e)
  }
};

sayHelloInFrench();
