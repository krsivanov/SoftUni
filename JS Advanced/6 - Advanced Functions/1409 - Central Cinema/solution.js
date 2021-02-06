function solve() {
    const formElements = document.querySelector('#container').children;
    const inputs = [...formElements].slice(0,formElements.length-1);
    const onScreenBtn = [...formElements].slice(formElements.length-1)[0];
    const moviesUl = document.querySelector('#movies>ul');

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

        moviesUl.appendChild(li);
    }

    onScreenBtn.addEventListener('click', createMovie);
}