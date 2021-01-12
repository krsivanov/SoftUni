function solve() {
  let text = document.getElementById('input').innerText;
  let outputElement = document.getElementById('output');
  let sentences = text.split('.');

  while (sentences.length > 0) {
    let currentParagraph = sentences.splice(0,3);

    let paragraphElement = document.createElement('p');
    paragraphElement.innerText = currentParagraph;

    outputElement.appendChild(paragraphElement);
  }
}
