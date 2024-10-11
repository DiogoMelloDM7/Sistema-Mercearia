console.log(clientes_venda)

let clienteSelecionado = null;

function carregaTabelaClientes(){
    $("#tabelaClientes thead").empty().append(`
            <tr>
                <th>Nome</th>
                <th>Rua</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>CPF</th>
                <th>Telefone</th>
                <th>Email</th>
                <th>Código</th>
                <th>Ação</th>
            </tr>
        `);

    clientes_venda.forEach(function(cliente, index){
        $("#tabelaClientes tbody").empty().append(`
            <tr>
                <td>${cliente.nome}</td>
                <td>${cliente.rua}</td>
                <td>${cliente.bairro}</td>
                <td>${cliente.cidade}</td>
                <td>${cliente.cpf}</td>
                <td>${cliente.telefone}</td>
                <td>${cliente.email}</td>
                <td>${cliente.id}</td>
                <td>
                    <button class="btn btn-success btn-sm select-cliente" data-index=${index}>Selecionar</button>
                </td>
            </tr>
            `);
    
    });
}

$(document).on('click', '.select-cliente', function(){
    indexCliente = $(this).data('index');
    $("#tabelaVendas thead").empty().append(`
        <tr>
            <th>NOME</th>
            <th>RUA</th>
            <th>BAIRRO</th>
            <th>CIDADE</th>
            <th>CPF</th>
            <th>TELEFONE</th>
        </tr>
        <tr>
            <th>${clientes_venda[indexCliente].nome}</th>
            <th>${clientes_venda[indexCliente].rua}</th>
            <th>${clientes_venda[indexCliente].bairro}</th>
            <th>${clientes_venda[indexCliente].cidade}</th>
            <th>${clientes_venda[indexCliente].cpf}</th>
            <th>${clientes_venda[indexCliente].telefone}</th>
        </tr>
    `);

    $('#btn-close-modal').trigger('click');
    clienteSelecionado = clientes_venda[indexCliente]

});
    

$(document).on('click', '.btn-prosseguir-vendas', function(){
    $("#idCliente").val(clienteSelecionado.id)
    console.log($("#idCliente").val());
})
    
