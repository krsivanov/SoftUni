function attachGradientEvents() {
    let gradientElement = document.getElementById('gradient');

    gradientElement.addEventListener('click', e => {
        let resultElement = document.getElementById('result');
        let offset = e.offsetX;
        let width = e.currentTarget.offsetWidth;

        let percent = (offset/width)*100;
        resultElement.textContent = `${percent.toFixed(0)}%`;
    });
}