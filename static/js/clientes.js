function exibeCadastro() {

    $("#formEditar").hide();
    $("#tabelaDeClientes").hide();
    $("#formCadastro").show();
}

function exibeEditarCadastro() {
    
    $("#formCadastro").hide();
    $("#formEditar").show();
    $("#tabelaDeClientes").show();
}

function exibeCliente() {

    $("#formCadastro").hide();
    $("#formEditar").hide();
    $("#tabelaDeClientes").show();
}