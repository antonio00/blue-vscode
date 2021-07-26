let inputNome = document.querySelector('#nome') //recebe o elemento com id nome, na variavel inputNome
let inputEmail = document.querySelector('email')
let textareaMensagem = document.querySelector('#mensagem')
let btnEnviar = document.querySelector('#enviar')

btnEnviar.addEventListener('click', () => {
    /* Pega a div de carregamento */
    let carregamento = document.querySelector('#carregamento')
    /* Mostra a div de carregamento, adicionando o 'flex' ao display */
    carregamento.style.display = 'flex'
 
    /* Pega o Form */
    let form = document.querySelector('form')
    /* Esconde o Form, mudando o display pra 'none' */
    form.style.display = 'none'
 })