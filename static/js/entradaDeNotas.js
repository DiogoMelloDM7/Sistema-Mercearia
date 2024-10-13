console.log(lista_fornecedores);
console.log(lista_produtos);

let itensNota = [];
let fornecedorNota = [];
let valorTotalNota = 0
let qtde = 0;
let valorCusto = 0;
let valorTotalProduto = 0;

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
                <td>${produto.valor_venda.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</td>    
                <td>${produto.valor_custo.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</td>    
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
        `);
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
                    <td>${produto.valor_venda.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</td>    
                    <td>${produto.valor_custo.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</td>    
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

$(document).on("click", ".add-fornecedor-btn", function(){
    let indexFornecedor = $(this).data('index');
    fornecedorNota = lista_fornecedores[indexFornecedor]
    constroiTabelaItensNota();
})

$(document).on("click", ".add-produto-btn", function(){
    let indexProduto = $(this).data('index');
    itensNota.push(lista_produtos[indexProduto])
    lista_produtos[indexProduto].quantidadeInput = 0
    lista_produtos[indexProduto].valorTotalProdutoNota = 0
    console.log(itensNota)
    constroiTabelaItensNota();
})

function constroiTabelaItensNota(){
    $("#tabelaItensNota thead").empty().append(`
        <tr>    
            <th>Fornecedor</th>
            <th>CNPJ</th>
            <th>Endereço</th>
            <th>Cidade</th>
            <th>Estado</th>
        </tr>
        <tr>    
            <td>${fornecedorNota.nome_empresa}</td>
            <td>${fornecedorNota.cnpj}</td>
            <td>${fornecedorNota.endereco}</td>
            <td>${fornecedorNota.cidade}</td>
            <td>${fornecedorNota.estado}</td>
        </tr>
         <tr>    
            <th>Produto</th>
            <th>Grupo</th>
            <th>Preço de Venda</th>
            <th>Preço de Custo</th>
            <th>Quantidade</th>
           
        </tr>
    `)

    $("#tabelaItensNota tbody").empty()
    itensNota.forEach(function(item, index){
        $("#tabelaItensNota tbody").append(`
            <tr>
                <td>${item.nome}</td>
                <td>${item.grupo}</td>
                <td>${item.valor_venda.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</td>
                <td>${item.valor_custo.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</td>
                <td>
                    <input type="number" placeholder="Informe a qtde" class="qtde-input" data-index="${index}">
                </td>
            </tr>    
        `)
        $(document).on("click", ".qtde-input", function(){
            let indexInput = $(this).data("index");
            $(this).on("keyup", function(){
                qtde = parseFloat($(this).val())
                itensNota[indexInput].quantidadeInput = qtde
                valorCusto = parseFloat(itensNota[indexInput].valor_custo); 
                itensNota[indexInput].valorTotalProdutoNota = itensNota[indexInput].quantidadeInput * valorCusto
            })
        
        valorTotalNota += valorTotalProduto
        })
    })

    valorTotalNota = itensNota.reduce(function(acumulador, item) {
        return acumulador + item.valorTotalProdutoNota;
    }, 0);

    $("#tabelaItensNota tfoot").empty().append(`
        <tr>
            <th colspan="2">Valor Total</th>
            <th colspan="3" id="valorTotalNota">${valorTotalNota.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</th>
        </tr>
    `)
    console.log(valorTotalNota)
}



let valoresInputs = {};

// Antes de recriar a tabela, armazene os valores
function salvarValoresInputs() {
    $(".qtde-input").each(function() {
        let index = $(this).data("index");
        let valor = $(this).val();
        valoresInputs[index] = valor; // Armazena o valor no objeto valoresInputs
    });
}

// Depois de recriar a tabela, reatribua os valores
function restaurarValoresInputs() {
    $(".qtde-input").each(function() {
        let index = $(this).data("index");
        if (valoresInputs[index] !== undefined) {
            $(this).val(valoresInputs[index]); // Restaura o valor salvo
        }
    });
}

$(document).on("click", '.add-fornecedor-btn', function(){
    $('#btn-close-fornecedor').trigger('click');
    itensNota.forEach(function(item, index){
        let qtdeInput = $(`.qtde-input[data-index='${index}']`);
        qtdeInput.val(item.quantidadeInput)
    })
    salvarValoresInputs();
    restaurarValoresInputs();
})

$(document).on("click", '.add-produto-btn', function(){
    $('#btn-close-produto').trigger('click');
    salvarValoresInputs();
    restaurarValoresInputs();
    $('.add-fornecedor-btn').trigger('click');
})