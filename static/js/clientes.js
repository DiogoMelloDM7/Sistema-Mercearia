function exibeCadastro() {

    $("#formEditar").hide();
    $("#tabelaDeClientes").hide();
    $("#formCadastro").show();
    resetaFormEditar();
}

function exibeEditarCadastro() {
    constroiTabelaClientes();
    $("#formCadastro").hide();
    $("#formEditar").show();
    $("#tabelaDeClientes").hide();
    console.log(clientes)
}

function exibeCliente() {
    constroiTabela();
    $("#formCadastro").hide();
    $("#formEditar").hide();
    $("#tabelaDeClientes").show();
    resetaFormEditar();
}

function constroiTabela(){

    $("#tabelaClientes thead").empty().append(`
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

    $("#tabelaClientes tbody").empty();
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

function constroiTabelaClientes(){
    $("#tabelaEdicaoClientes thead").empty().append(`
        <tr>
            <th>Cliente</th>
            <th>Rua</th>
            <th>Bairro</th>
            <th>Cidade</th>
            <th>CPF</th>
            <th>Telefone</th>
            <th>E-mail</th>
            <th>Ações</th>
        </tr>
    `)

    $("#tabelaEdicaoClientes tbody").empty();
    clientes.forEach(function(cliente, index){
        $("#tabelaEdicaoClientes tbody").append(`
            <tr>
            <td>${cliente.nome}</td>
            <td>${cliente.rua}</td>
            <td>${cliente.bairro}</td>
            <td>${cliente.cidade}</td>
            <td>${cliente.cpf}</td>
            <td>${cliente.telefone}</td>
            <td>${cliente.email}</td>
            <td>
                <button class="btn btn-sm btn-primary edit-cliente-btn" data-index=${index}>Editar</button>
            </td> 
        </tr>
`)
    })
}

$(document).ready(function () {
    


    $("#clienteNome").on('keyup', function () { 
        let clienteNome = $("#clienteNome").val().toLowerCase();

        $("#tabelaClientes thead").empty().append(`
            <tr>
                <th>Cliente</th>
                <th>Rua</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>CPF</th>
                <th>Telefone</th>
                <th>E-mail</th>
            </tr>
        `);

        $("#tabelaClientes tbody").empty();
        clientes.forEach(function (cliente, index) {
            if (cliente.nome.toLowerCase().includes(clienteNome)) {
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
                `);
            }
        });
    });

    $("#clienteEditarNome").on('keyup', function () { 
        let clienteNomeEditar = $("#clienteEditarNome").val().toLowerCase();

        $("#tabelaEdicaoClientes thead").empty().append(`
            <tr>
                <th>Cliente</th>
                <th>Rua</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>CPF</th>
                <th>Telefone</th>
                <th>E-mail</th>
            </tr>
        `);

        $("#tabelaEdicaoClientes tbody").empty();
        clientes.forEach(function (cliente, index) {
            if (cliente.nome.toLowerCase().includes(clienteNomeEditar)) {
                $("#tabelaEdicaoClientes tbody").append(`
                    <tr>
                        <td>${cliente.nome}</td>
                        <td>${cliente.rua}</td>
                        <td>${cliente.bairro}</td>
                        <td>${cliente.cidade}</td>
                        <td>${cliente.cpf}</td>
                        <td>${cliente.telefone}</td>
                        <td>${cliente.email}</td> 
                        <td>
                            <button class="btn btn-sm btn-primary edit-cliente-btn" data-index=${index}>Editar</button>
                        </td>
                    </tr>
                `);
            }
        });
    });

    $(document).on("click", '.edit-cliente-btn', function(event){
        event.preventDefault(); 
        let indexVenda = $(this).data('index');

        $("#nomeEdit").val(clientes[indexVenda].nome);
        $("#ruaEdit").val(clientes[indexVenda].rua);
        $("#bairroEdit").val(clientes[indexVenda].bairro);
        $("#cidadeEdit").val(clientes[indexVenda].cidade);
        $("#cpfEdit").val(clientes[indexVenda].cpf);
        $("#telefoneEdit").val(clientes[indexVenda].telefone);
        $("#emailEdit").val(clientes[indexVenda].email);
        $("#idCliente").val(clientes[indexVenda].id);
    })

});

function resetaFormEditar(){
    $("#formEditar").reset();

}

resetaFormEditar();