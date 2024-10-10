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

function constroiTabela(){
    $("#tabelaClientes thead").append(`
        <tr>
            <th>Cliente</th>
            <th>Rua</th>
            <th>Bairro</th>
            <th>Cidade</th>
            <th>CPF</th>
            <th>Telefone</th>
            <th>E-mail</th>
        </tr>
    `)

    clientes.forEach(function(cliente, index){
        $("#tabelaClientes tbody").append(`
            <tr>
            <td>${cliente.nome}</td>
            <td>${cliente.rua}</td>
            <td>${cliente.bairro}</td>
            <td>${cliente.cidade}</td>
            <td>${cliente.cpf}</td>
            <td>${cliente.telefone}</td>
            <td>${cliente.email}</td> 
        </tr>
`)
    })
}

$(document).ready(function(){
    console.log(clientes,'js');
    constroiTabela();
})  
