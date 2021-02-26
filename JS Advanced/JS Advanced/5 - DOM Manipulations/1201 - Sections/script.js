function create(words) {
   const content = document.getElementById('content');

   for (let i=0; i<words.length; i++){
      let div = document.createElement('div');
      let paragraph = document.createElement('p');
      paragraph.textContent = words[i];
      paragraph.style.display = 'none';
      div.appendChild(paragraph);
      content.appendChild(div);
   }
   
   content.addEventListener('click', function (e){
      if(e.target !== e.currentTarget){
         const p = e.target.children[0] || e.target;
         const isVisible = p.style.display=== 'block';
         p.style.display = isVisible ? 'none' : 'block';
      }
      
   });
}
