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




