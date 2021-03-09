document.querySelector('form').addEventListener('submit',onLoginSubmit);

async function onLoginSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    const email = formData.get('email');
    const password = formData.get('password');

    const responose = await fetch('http://localhost:3030/users/login', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email, password})
    });  

    if(responose.ok == false){
        const error = await responose.json();
        return alert(error.message);
    }
    
    const data = await responose.json();
    sessionStorage.setItem('userToken', data.accessToken);
    window.location.pathname = '/cookbook/cookbook/js-apps-workshop-master/lesson-03/base/index.html';
}