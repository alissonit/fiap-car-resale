# Fiap Car Resale
Projeto desenvolvido para a pós-graduação em Arquiteura de Software da FIAP.

## Objetivo
O objetivo deste projeto é criar um sistema de revenda de Veículos, onde o usuário poderá cadastrar Veículos para venda e também comprar Veículos.

## Funcionalidades
- Lista de Veículos
- Compra e venda de veículos
- Webhook para notificação de pagamento

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

3. importante crie um ambiente virtual para instalar as dependências
```bash
python -m venv .venv
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
```bash
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
DB_URI=
DB_MAX_POOL_SIZE=
```

6. Execute o projeto:
```bash
uvicorn main:app --port 7000 --reload
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

### CI/CD
- [ ] Implementar Github Actions
- [ ] Implementar SonarQube
- [x] Cobertura de testes unitários acima de 80%
- [x] Deploy no Openshift

### Infraestrutura
- [ ] Cluster Openshift Red Hat.
- [ ] Objetos do kubernetes (Deployment, Service, Ingress, ConfigMap, Secret).
- [x] Banco de dados PostgreSQL RDS AWS.

# Evidências

### Coberura de testes em 80%

![image](/images/fiap-car-resale-cov.png)

Link para o relatório de cobertura de testes:

[Cobertura de Testes](/tests/index.html)

### CI/CD

Github Actions:

![image](/images/actions.png)






