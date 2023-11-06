# MercaLife: Um Sistema de Mercearia

# Sobre o Projeto

MercaLife é uma aplicação web voltada para controle de vendas, estoque e caixa de uma mercearia ou pequeno negócio. [Visualize a aplicação aqui](https://sistema-mercearia-production.up.railway.app/).

## Funcionalidades 

* Controle de Estoque, adicione e remova itens ao estoque, altere seus informações conforme necessidade do usuário.
* Controle de Vendas, realize vendas adicionando produtos ao carrinho e depois informando a forma de pagamento, após a finalização da venda.
* Controle de Caixa, realize controle de caixa ao final do dia, informe a quantidade de dinheiro em caixa e o sistema irá calcular o quanto foi faturado no dia separando os valores recebidos por dinheiro ou cartão, após isso retornando o saldo do caixa.
* Consulta de Relatórios, realize consultas para saber quanto foi vendido em determinado dia ou qual o valor do caixa em determinado em dia. Esses relatórios são salvos automaticamente ao serem realizadas vendas ou controle de caixa.

# Tecnologias

## Back-End
* Python
* Django

## Front-End 
* JavaScript
* HTML
* CSS

## Banco de Dados
* PostgreSQL

## HomePage
![HomePage MercaLife](https://github.com/DiogoMelloDM7/Sistema-Mercearia/assets/136912625/bb6ae150-dc9a-4398-a4b7-02026528732b)

## Baixando e rodando a aplicação localmente

Para começar, siga estas etapas para baixar o código-fonte do projeto localmente:

1. Abra o terminal no seu computador.
2. Navegue até o diretório onde deseja armazenar o projeto.
3. Use o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/DiogoMelloDM7/Sistema-Mercearia.git
```

### Configurando ambiente

Antes de executar a aplicação localmente, você precisa configurar o ambiente. Siga estas etapas:

1. Abra o terminal e navegue até o diretório raiz do projeto.
2. Execute o seguinte comando para instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Executando a aplicação localmente

Após a configuração do ambiente, você pode iniciar a aplicação localmente. Siga estas etapas:

1. No terminal, navegue até o diretório raiz do projeto.
2. Execute o seguinte comando para aplicar migrações do banco de dados, se necessário:

```bash
python manage.py migrate
```

1. Inicie o servidor de desenvolvimento com o seguinte comando:

```bash
python manage.py runserver
```

