function solve() {
  const [input, output] = [...document.querySelectorAll('textarea')];
  const table = document.querySelector('table.table tbody');
  const [generateBtn, buyBtn] = [...document.querySelectorAll('button')];

  const furnitureArray = JSON.parse(input.value.toString().trim());

  generateBtn.addEventListener('click', () => {
    table.innerHTML = '';
    furnitureArray.forEach(f => table.appendChild(createRow(f)));  
  });

  buyBtn.addEventListener('click', () => {

  });

  function createRow(data){
    const img = e('img');
    img.src = data.img;

    const check = e('input');
    check.type = 'checkbox';

    return e('tr',
     e('td',img),
     e('td',data.name),
     e('td',data.price),
     e('td',data.decFactor),
     e('td',check)
     );
  }

  function e(type, ...content){
    const result = document.createElement(type);
    
    content.forEach(e => {
      if (typeof e =='string'){
        const nude = document.createTextNode(e);
        result.appendChild(node);
      } else {
        result.appendChild(e);
      }
    });
    return result;
  }
}