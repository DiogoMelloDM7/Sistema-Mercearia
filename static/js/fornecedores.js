function exibeFormEdicao(){
    constroiTabelaDeEdicao();
    $('#tabelaDeFornecedores').hide();
    $('#formCadastro').hide();
    $('#formEditar').show();
    resetaFormEditar();
    
}

function exibeFormCadastro(){

    $('#tabelaDeFornecedores').hide();
    $('#formEditar').hide();
    $('#formCadastro').show();
}

function exibeFornecedores(){
    constroiTabelaDeExibicao();
    $('#formCadastro').hide();
    $('#formEditar').hide();
    $('#tabelaDeFornecedores').show();
    resetaFormEditar();
}

function constroiTabelaDeExibicao(){
    $('#tabelaFornecedores thead').empty().append(`
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
        </tr>    
    `)
    $('#tabelaFornecedores tbody').empty();
    lista_fornecedores.forEach(function(fornecedor){
        $('#tabelaFornecedores tbody').append(`
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
            </tr>
        `)
    })
}

function constroiTabelaDeEdicao(){
    $('#tabelaEdicaoFornecedores thead').empty().append(`
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
            <th>Ações</th>
        </tr>    
    `)

    $("#tabelaEdicaoFornecedores tbody").empty();
    lista_fornecedores.forEach(function(fornecedor, index){
        $("#tabelaEdicaoFornecedores tbody").append(`
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
                    <button class="btn btn-sm btn-primary edit-fornecedor-btn" data-index=${index}>Editar</button>
                </td>
            </tr>
        `);
    })
    
}

$(document).ready(function(){

    $('#fornecedorNome').on('keyup',function(){

        let fornecedorNome = $("#fornecedorNome").val().toLowerCase();

        $("#tabelaFornecedores thead").empty().append(`
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
        </tr> 
        `)

        $('#tabelaFornecedores tbody').empty();
        lista_fornecedores.forEach(function(fornecedor){
            if(fornecedor.nome_empresa.toLowerCase().includes(fornecedorNome)){
                $('#tabelaFornecedores tbody').append(`
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
                    </tr>
                `);
            } 
        });
    });

    $('#fornecedorEditarNome').on('keyup',function(){

        let fornecedorEditarNome = $("#fornecedorEditarNome").val().toLowerCase();

        $("#tabelaEdicaoFornecedores thead").empty().append(`
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
            <th>Ações</th>
        </tr> 
        `)

        $('#tabelaEdicaoFornecedores tbody').empty();
        lista_fornecedores.forEach(function(fornecedor, index){
            if(fornecedor.nome_empresa.toLowerCase().includes(fornecedorEditarNome)){
                $('#tabelaEdicaoFornecedores tbody').append(`
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
                            <button class="btn btn-sm btn-primary edit-fornecedor-btn" data-index='${index}'>Editar</button>
                        </td>
                    </tr>
                `);
            } 
        });
    });

    $(document).on("click", ".edit-fornecedor-btn", function(event){
        event.preventDefault();
        let indexFornecedor = $(this).data('index');

        $("#nomeEdit").val(lista_fornecedores[indexFornecedor].nome_empresa)
        $("#cnpjEdit").val(lista_fornecedores[indexFornecedor].cnpj)
        $("#ieEdit").val(lista_fornecedores[indexFornecedor].inscricao_estadual)
        $("#enderecoEdit").val(lista_fornecedores[indexFornecedor].endereco)
        $("#cidadeEdit").val(lista_fornecedores[indexFornecedor].cidade)
        $("#estadoEdit").val(lista_fornecedores[indexFornecedor].estado)
        $("#cepEdit").val(lista_fornecedores[indexFornecedor].cep)
        $("#telefoneEdit").val(lista_fornecedores[indexFornecedor].telefone)
        $("#emailEdit").val(lista_fornecedores[indexFornecedor].email)
        $("#idFornecedor").val(lista_fornecedores[indexFornecedor].id)
    });

});

function resetaFormEditar(){
    $("#formEditar")[0].reset();
}

resetaFormEditar();

document.getElementById('cepEdit').addEventListener('input', function (e) {
    // Remove qualquer caractere que não seja número
    let cep = e.target.value.replace(/\D/g, '');

    // Limita a entrada a 8 números
    if (cep.length > 8) {
        cep = cep.slice(0, 8);
    }

    // Formata como XXXXX-XXX se houver 8 números
    if (cep.length >= 5) {
        cep = cep.slice(0, 5) + '-' + cep.slice(5);
    }

    // Atualiza o valor no input
    e.target.value = cep;
});

document.getElementById('cepAdd').addEventListener('input', function (e) {
    // Remove qualquer caractere que não seja número
    let cep = e.target.value.replace(/\D/g, '');

    // Limita a entrada a 8 números
    if (cep.length > 8) {
        cep = cep.slice(0, 8);
    }

    // Formata como XXXXX-XXX se houver 8 números
    if (cep.length >= 5) {
        cep = cep.slice(0, 5) + '-' + cep.slice(5);
    }

    // Atualiza o valor no input
    e.target.value = cep;
});