<<<<<<< HEAD
const elementoDia = document.getElementById('dia');
const elementoImg = document.querySelector('#imagem')
let elementoBtn = document.querySelector('#alterar')


elementoBtn.addEventListener('click', () =>{
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './img/homer_segunda.png'
        elementoDia.innerText= 'Segunta-Feira'
        elementoBtn.value ='segundo'
    } else if(elementoBtn.value == 'segundo'){
        elementoImg.src = './img/homer_terca.png'
        elementoDia.innerText= 'Terça-Feira'
        elementoBtn.value ='terceiro'
    } else if(elementoBtn.value == 'terceiro'){
        elementoImg.src = './img/homer_quarta.png'
        elementoDia.innerText= 'Quarta-Feira'
        elementoBtn.value ='quarto'    
    } else if(elementoBtn.value == 'quarto'){
        elementoImg.src = './img/homer_quinta.png'
        elementoDia.innerText= 'Quinta-Feira'
        elementoBtn.value ='quinto'    
    } else if(elementoBtn.value == 'quinto'){
        elementoImg.src = './img/homer_sexta.png'
        elementoDia.innerText= 'Sexta-Feira'
        elementoBtn.value ='sexto'    
    } else{
        elementoImg.src='./img/ihomer.png'
        elementoDia.innerText = '  ? '
        elementoBtn.value = 'primeiro'
    }

})
=======
const elementoDia = document.getElementById('dia');
const elementoImg = document.querySelector('#imagem')
let elementoBtn = document.querySelector('#alterar')


elementoBtn.addEventListener('click', () =>{
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './img/homer_segunda.png'
        elementoDia.innerText= 'Segunta-Feira'
        elementoBtn.value ='segundo'
    } else if(elementoBtn.value == 'segundo'){
        elementoImg.src = './img/homer_terca.png'
        elementoDia.innerText= 'Terça-Feira'
        elementoBtn.value ='terceiro'
    } else if(elementoBtn.value == 'terceiro'){
        elementoImg.src = './img/homer_quarta.png'
        elementoDia.innerText= 'Quarta-Feira'
        elementoBtn.value ='quarto'    
    } else if(elementoBtn.value == 'quarto'){
        elementoImg.src = './img/homer_quinta.png'
        elementoDia.innerText= 'Quinta-Feira'
        elementoBtn.value ='quinto'    
    } else if(elementoBtn.value == 'quinto'){
        elementoImg.src = './img/homer_sexta.png'
        elementoDia.innerText= 'Sexta-Feira'
        elementoBtn.value ='sexto'    
    } else{
        elementoImg.src='./img/ihomer.png'
        elementoDia.innerText = '  ? '
        elementoBtn.value = 'primeiro'
    }

})
>>>>>>> e63f108cca048f3dec5b932f58327f3da77ea60d
