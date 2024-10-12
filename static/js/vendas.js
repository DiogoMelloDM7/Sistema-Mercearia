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
        $("#tabelaClientes tbody").empty();
    clientes_venda.forEach(function(cliente, index){
        $("#tabelaClientes tbody").append(`
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
    $("#listaDeProdutos thead").empty().append(`
        <tr>
            <th>NOME</th>
            <th>RUA</th>
            <th>BAIRRO</th>
            <th>CIDADE</th>
            <th>CPF</th>
        </tr>
        <tr>
            <th>${clientes_venda[indexCliente].nome}</th>
            <th>${clientes_venda[indexCliente].rua}</th>
            <th>${clientes_venda[indexCliente].bairro}</th>
            <th>${clientes_venda[indexCliente].cidade}</th>
            <th>${clientes_venda[indexCliente].cpf}</th>
        </tr>
    `);

    $('#btn-close-modal').trigger('click');
    clienteSelecionado = clientes_venda[indexCliente]
    localStorage.setItem('clienteSelecionado',JSON.stringify(clienteSelecionado))

});
    

$(document).on('click', '.btn-prosseguir-vendas', function(){
    let clienteSelecionadoLocal = JSON.parse(localStorage.getItem('clienteSelecionado'))
    console.log(clienteSelecionadoLocal)

    $("#idCliente").val(clienteSelecionadoLocal.id)
    console.log($("#idCliente").val());
})

function confereClienteEMontaCabecalho(){
    clienteSelecionado = JSON.parse(localStorage.getItem('clienteSelecionado'))
    if(clienteSelecionado){
        console.log("entrou", clienteSelecionado)
        $("#listaDeProdutos thead").empty().append(`
            <tr>
                <th>NOME</th>
                <th>RUA</th>
                <th>BAIRRO</th>
                <th>CIDADE</th>
                <th>CPF</th>
            </tr>
            <tr>
                <th>${clienteSelecionado.nome}</th>
                <th>${clienteSelecionado.rua}</th>
                <th>${clienteSelecionado.bairro}</th>
                <th>${clienteSelecionado.cidade}</th>
                <th>${clienteSelecionado.cpf}</th>
            </tr>
        `);
    }
    console.log("chamou");
}

$("#buscaClienteVenda").on("keyup", function(){
    let valorPesquisa = $(this).val().toLowerCase();
    let tabelaClientes = $("#tabelaClientes tbody")
    tabelaClientes.empty();

    clientes_venda.forEach(function(cliente, index){
        if(cliente.nome.toLowerCase().includes(valorPesquisa)){
            tabelaClientes.append(`
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
            `)
        }
        
    })
})

$(document).ready(function(){
    confereClienteEMontaCabecalho();
})

    
