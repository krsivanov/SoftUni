function solve() {
    const formElements = document.querySelector('#container').children;
    const inputs = [...formElements].slice(0,formElements.length-1);
    const onScreenBtn = [...formElements].slice(formElements.length-1)[0];
    const moviesUl = document.querySelector('#movies>ul');

    function archive(e){
        console.log('archive');
    }

    function createMovie(e){
        e.preventDefault();

        const name = inputs[0].value;
        const hall = inputs[1].value;
        const price = Number(inputs[2].value) ;

        if (!name || !hall || !price) {return;}

        inputs[0].value = '';
        inputs[1].value = '';
        inputs[2].value = '';

        const li = document.createElement('li');

        const span = document.createElement('span');
        span.textContent = name;
        li.appendChild(span);

        const strong = document.createElement('strong');
        strong.textContent = `Hall: ${hall}`;
        li.appendChild(strong);

        const div = document.createElement('div');
        const innerStrong = document.createElement('strong');
        innerStrong.textContent = price;
        const input = document.createElement('input');
        input.setAttribute('placeholder', 'Ticket Sold');
        const archiveBtn = document.createElement('archiveBtn');
        archiveBtn.textContent = 'Archive';
        archiveBtn.addEventListener('click', archive);


        div.appendChild(innerStrong);
        div.appendChild(input);
        div.appendChild(archiveBtn);


        li.appendChild(div);
        
        moviesUl.appendChild(li);
    }

    onScreenBtn.addEventListener('click', createMovie);
}