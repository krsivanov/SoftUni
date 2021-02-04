function solve() {
  const furnitureArray = JSON.parse(document.querySelector('textarea').value);
  const output = document.querySelector('table.table tbody');
  
  const [generateBtn, buyBtn] = [...document.querySelectorAll('button')];
  generateBtn.addEventListener('click', () => {
    // output.innerHTML = '';
    furnitureArray.forEach(f => output.appendChild(createRow(f)));  
  });
  furnitureArray.forEach(f => output.appendChild(createRow(f)));

  function createRow(data){
    return e('tr', e('td','hi'));
  }

  function e(type, content){
    const result = document.createElement(type);
    
    if (typeof content =='string'){
      result.textContent = content;
    } else {
      result.appendChild(content);
    }
    return result;
  }
}