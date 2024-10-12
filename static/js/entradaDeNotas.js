console.log(lista_fornecedores);
console.log(lista_produtos);

function constroiTabelaProdutos(){
    $("#tabelaProdutos thead").empty().append(`
        <tr>
            <th>Nome</th>
            <th>Valor de Venda</th>
            <th>Valor de Custo</th>
            <th>Quantidade</th>
            <th>Grupo</th>
            <th>Ação</th>
        </tr>
    `)

    $("#tabelaProdutos tbody").empty();
    lista_produtos.forEach(function(produto, index){
        $("#tabelaProdutos tbody").append(`
            <tr>
                <td>${produto.nome}</td>    
                <td>${produto.valor_venda}</td>    
                <td>${produto.valor_custo}</td>    
                <td>${produto.quantidade}</td>    
                <td>${produto.grupo}</td>
                <td>
                    <button class="btn btn-sm btn-success add-produto-btn" data-index="${index}">Adicionar</button>
                </td>    
            </tr>
        `)
    })
}

function constroiTabelaFornecedores(){
    $("#tabelaFornecedor thead").empty().append(`
        <tr>
            <th>Nome</th>
            <th>CNPJ</th>
            <th>IE</th>
            <th>Endereço</th>
            <th>Cidade</th>
            <th>Estado</th>
            <th>CEP</th>
            <th>Telefone</th>
            <th>E-mail</th>
            <th>Ação</th>

        </tr>
    `);

    $("#tabelaFornecedor tbody").empty();
    lista_fornecedores.forEach(function(fornecedor, index){
        $("#tabelaFornecedor tbody").append(`
            <tr>
                <td>${fornecedor.nome_empresa}</td>    
                <td>${fornecedor.cnpj}</td>    
                <td>${fornecedor.inscricao_estadual}</td>    
                <td>${fornecedor.endereco}</td>    
                <td>${fornecedor.cidade}</td>
                <td>${fornecedor.estado}</td>
                <td>${fornecedor.cep}</td>
                <td>${fornecedor.telefone}</td>
                <td>${fornecedor.email}</td>
                <td>
                    <button class="btn btn-sm btn-success add-fornecedor-btn" data-index="${index}">Adicionar</button>
                </td>   
            </tr> 
        `);console.log(fornecedor)
    });
}

$(document).on("click", "#btn-Fornecedor", function(){
    constroiTabelaFornecedores();
    console.log("chamou")
})

$(document).on("click", "#btn-Produto", function(){
    constroiTabelaProdutos();
})

$("#inputFornecedor").on("keyup",function(){
    let nomeFornecedor = $("#inputFornecedor").val().toLowerCase();

    $("#tabelaFornecedor thead").empty().append(`
        <tr>
            <th>Nome</th>
            <th>CNPJ</th>
            <th>IE</th>
            <th>Endereço</th>
            <th>Cidade</th>
            <th>Estado</th>
            <th>CEP</th>
            <th>Telefone</th>
            <th>E-mail</th>
            <th>Ação</th>

        </tr>
    `);

    $("#tabelaFornecedor tbody").empty();
    lista_fornecedores.forEach(function(fornecedor, index){

        if(fornecedor.nome_empresa.toLowerCase().includes(nomeFornecedor)){
            $("#tabelaFornecedor tbody").append(`
                <tr>
                    <td>${fornecedor.nome_empresa}</td>    
                    <td>${fornecedor.cnpj}</td>    
                    <td>${fornecedor.inscricao_estadual}</td>    
                    <td>${fornecedor.endereco}</td>    
                    <td>${fornecedor.cidade}</td>
                    <td>${fornecedor.estado}</td>
                    <td>${fornecedor.cep}</td>
                    <td>${fornecedor.telefone}</td>
                    <td>${fornecedor.email}</td>
                    <td>
                        <button class="btn btn-sm btn-success add-fornecedor-btn" data-index="${index}">Adicionar</button>
                    </td>   
                </tr> 
            `);
        }
        
    });
});


$("#inputProduto").on("keyup",function(){
    let nomeProduto = $("#inputProduto").val().toLowerCase();

    $("#tabelaProdutos thead").empty().append(`
        <tr>
            <th>Nome</th>
            <th>Valor de Venda</th>
            <th>Valor de Custo</th>
            <th>Quantidade</th>
            <th>Grupo</th>
            <th>Ação</th>
        </tr>
    `)

    $("#tabelaProdutos tbody").empty();
    lista_produtos.forEach(function(produto, index){
        if(produto.nome.toLowerCase().includes(nomeProduto)){
            $("#tabelaProdutos tbody").append(`
                <tr>
                    <td>${produto.nome}</td>    
                    <td>${produto.valor_venda}</td>    
                    <td>${produto.valor_custo}</td>    
                    <td>${produto.quantidade}</td>    
                    <td>${produto.grupo}</td>
                    <td>
                        <button class="btn btn-sm btn-success add-produto-btn" data-index="${index}">Adicionar</button>
                    </td>    
                </tr>
            `)
        }
        
    });

});