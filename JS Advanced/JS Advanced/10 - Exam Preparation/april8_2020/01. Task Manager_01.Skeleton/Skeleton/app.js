function solve() {
    const [task, date] = document.querySelectorAll('input');
    const description = document.querySelector('textarea');
    const addBtn = document.getElementById('add');
    const taskValue = task.value;
    const descrValue =description.value;
    const dateValue = date.value;
    const [addTask,opened, inProgress, completed] = document.querySelectorAll('section')

    function createEl(type, content, className){
        const result = document.createElement(type);
        result.textContent = content;
        if (className) {
            result.className = className;
        }
        return result;
    }

   
    function add(e){
        e.preventDefault();
        if (!task.value || !description.value || !Date.parse(date.value)){
            return;
        }
        const secondDiv = opened.querySelector("div:nth-child(2)");
        const article = createEl('article');
        const h3 = createEl('h3',task.value);
        const pDescr = createEl('p',`Description: ${description.value}`);
        const pDate = createEl('p',`Due Date: ${date.value}`);
        const insideDiv = createEl('div', '', 'flex');
        const startBtn = createEl('button','Start', 'green'); 
        const deleteBtn = createEl('button','Delete','red');

        article.appendChild(h3);
        article.appendChild(pDescr);
        article.appendChild(pDate);
        insideDiv.appendChild(startBtn);
        insideDiv.appendChild(deleteBtn);
        article.appendChild(insideDiv);
        secondDiv.appendChild(article);


        startBtn.addEventListener('click', start);
        deleteBtn.addEventListener('click', deleteEl);
    }

    function deleteEl(e){
        e.target.parentNode.parentNode.remove();
    }

    function start(e){
        const secondDiv = inProgress.querySelector("div:nth-child(2)");
        const article = createEl('article');
        const h3 = createEl('h3',task.value);
        const pDescr = createEl('p',`Description: ${description.value}`);
        const pDate = createEl('p',`Due Date: ${date.value}`);
        const insideDiv = createEl('div', '', 'flex');
        const deleteBtn = createEl('button','Delete', 'red'); 
        const finishBtn = createEl('button','Finish','orange');

        article.appendChild(h3);
        article.appendChild(pDescr);
        article.appendChild(pDate);
        insideDiv.appendChild(deleteBtn);
        insideDiv.appendChild(finishBtn);
        article.appendChild(insideDiv);
        secondDiv.appendChild(article);

        finishBtn.addEventListener('click', finish);
        deleteBtn.addEventListener('click', deleteEl);
        
        deleteEl(e);
    }

    function finish(e){
        const secondDiv = completed.querySelector("div:nth-child(2)");
        const article = createEl('article');
        const h3 = createEl('h3',task.value);
        const pDescr = createEl('p',`Description: ${description.value}`);
        const pDate = createEl('p',`Due Date: ${date.value}`);

        article.appendChild(h3);
        article.appendChild(pDescr);
        article.appendChild(pDate);
        secondDiv.appendChild(article);

    }


    addBtn.addEventListener('click', add);

}

