function mostrarSaidaEntrada(event){
    event.preventDefault();
    let div = document.getElementById("oculta");
    div.style.display = "block";
}

// Função para mostrar a mensagem de erro
function showErrorMessage() {
    var errorMessage = document.getElementById("error-message");
    errorMessage.style.display = "block";

    // Ocultar a mensagem após 5 segundos (ou o período desejado)
    setTimeout(function() {
        errorMessage.style.display = "none";
    }, 5000); // 5000 milissegundos = 5 segundos
}

// Chame a função para mostrar a mensagem de erro quando necessário
showErrorMessage();


function formaPagamento(event){
    event.preventDefault();
    let divPrincipal = document.getElementById("main-vendas")
    let divSecundaria = document.getElementById("main-vendas-2")
    divPrincipal.style.display="none";
    divSecundaria.style.display="block";

}

