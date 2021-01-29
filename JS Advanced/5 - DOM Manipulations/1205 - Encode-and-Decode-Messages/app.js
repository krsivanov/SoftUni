function encodeAndDecodeMessages() {
    const textAreas = document.querySelectorAll('textarea');
    const buttons  =document.querySelectorAll('button');

    const elems = {
        encode: {
            text: textAreas[0],
            btn: buttons[0],
            func: (char) => String.fromCharCode(char.charCodeAt(0) + 1)
            
        },
        decode: {
            text: textAreas[1],
            btn: buttons[1],
            func: (char) => String.fromCharCode(char.charCodeAt(0) - 1)
        }
    }

    document.getElementById('main').addEventListener('click', function(e){
        if (e.target.tagName !== 'BUTTON'){
            return;
        }

        const type = e.target.textContent.toLowerCase().trim().includes('encode') ? 'encode' : 'decode';

        const message = elems[type].text.value.split('').map(elems[type].func).join("");   
        elems.encode.text.value = '';
        elems.decode.text.value = message;
    });
}