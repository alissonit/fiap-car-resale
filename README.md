# Fiap Car Resale
Projeto desenvolvido para a pós-graduação em Arquiteura de Software da FIAP.

## Objetivo
O objetivo deste projeto é criar um sistema de revenda de carros, onde o usuário poderá cadastrar carros para venda e também comprar carros.

## Funcionalidades
- Login
- Cadastro de usuários
- Cadastro de carros
- Exclusão de carros

## Tecnologias
- Python
- FastAPI
- PostgreSQL
- Alembic

## Como executar
Para executar o projeto, siga os passos abaixo:
1. Clone este repositório:
```bash
git clone https://github.com/alissonit/fiap-car-resale.git
```
2. Acesse a pasta do projeto:
```bash
cd fiap-car-resale
```

3 importante crie um ambiente virtual para instalar as dependências
```bash
python -m venv .venv
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o projeto:
```bash
uvicorn src.main:app --reload
```

## Tipo de Arquitetura
A arquitetura utilizada foi a hexagonal, onde o core da aplicação é independente de frameworks e bibliotecas externas.

## Documentação
A documentação da API pode ser acessada em:
http://localhost:8000/api/v1/docs


### Entregas

- [x] Efetuar a venda de um veículo (CPF da pessoa que comprou e data da venda)
- [x] Listagem de veículos à venda, ordenada por preço, do mais barato para o mais caro
- [x] Listagem de veículos vendidos, ordenada por preço, do mais barato para o mais caro.
- [x] Disponibilizar um endpoint (webhook) para que a entidade que processa o pagamento
consiga, a partir do código do pagamento, informar se o pagamento foi efetuado ou
cancelado;



