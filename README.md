# API Shell Script (Linux bash)

Este projeto tem como objetivo demonstrar conhecimento em criação de API's utilizando a linguagem Python e processando arquivos usando shell script (Bash).

## Estrutura do Projeto

- `README`: Este arquivo de documentação.
- `app/Dockerfile`: Arquivo de configuração para criar uma imagem Docker do projeto.
- `docker-compose.yml`: Arquivo de configuração para orquestrar os serviços Docker.
- `app/requirements.txt`: Arquivo de dependências do projeto.

- `app/`: Diretório com o código fonte da aplicação.
- `app/main.py`: Arquivo principal da aplicação.
- `app/modules/`: Diretório com os módulos da aplicação.
- `app/routers/`: Diretório com os roteadores da aplicação.
- `app/schemas/`: Diretório com os schemas da aplicação.
- `app/scripts/`: Diretório com os scripts da aplicação.
- `app/services/`: Diretório com os serviços da aplicação.
- `app/settings/`: Diretório com as configurações da aplicação.
- `app/tmp/files`: Diretório com os arquivos temporários da aplicação.
- `app/utils/`: Diretório com as utilidades da aplicação.

- `app/htmlcov/`: Diretório com os relatórios de cobertura de testes.
- `app/tests/`: Diretório com os testes da aplicação.


## Instalação

Primeiramente, clone o repositório em sua máquina:
```bash
git clone https://github.com/edwildson/python-bash-users
```

### Configuração
Para configurar o projeto, primeiro você precisa criar um arquivo `.env` na raiz do projeto (dentro pasta app) com base no `.env.example`.
```bash	
cp .env.example .env
```

### Requisitos
Para rodar o projeto, você precisa ter o Docker e o Docker Compose instalados em sua máquina.

Para instalar as dependências do projeto, execute o seguinte comando na pasta acima da pasta `app` onde se encontra o arquivo `docker-compose.yml`:
```bash
docker-compose up --build
```

Após isso, a aplicação estará disponível em `http://localhost:8000`.
Para acessar a documentação da API, acesse `http://localhost:8000/docs` ou `http://localhost:8000/redoc`.

## Utilização da API

Para testar a API, para uma maior comodidade, você pode utilizar o arquivo input(./app/input) que contém um exemplo de arquivo de entrada e usar o endpoint http://localhost:8000/docs para enviar o arquivo e realizar as consultas.

### Arquivos

#### Enviar um arquivo
Para enviar um arquivo, acesse a rota `/files` com o método PUT e envie o arquivo no campo `file`.
```bash	
curl -X 'PUT' \
  'http://localhost:8000/files' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/file'
```

#### Listar arquivos
Para listar os arquivos enviados, acesse a rota `/files` com o método GET.
```bash
curl -X 'GET' \
  'http://localhost:8000/files' \
  -H 'accept: application/json'
```

### Usuários

#### Listar usuários pelo username (Email)
Para listar os usuários, acesse a rota `/users` com o método GET passando o nome do arquivo por parâmetro.

```bash
curl -X 'GET' \
  'http://localhost:8000/users?filename=example' \
  -H 'accept: application/json'
```

##### Parâmetros
- `filename`: Nome do arquivo a ser processado.
- `username`: Nome do usuário a ser filtrado.
- `order`: Ordem de ordenação dos usuários. Pode ser `asc` ou `desc`.
- `page`: Página a ser exibida.

Exemplo:

```bash
curl -X 'GET' \
  'http://localhost:8000/users?filename=example&username=eddie&order=asc&page=1' \
  -H 'accept: application/json'
```

#### Listar usuário com maior tamanho (Size)
Para listar os usuários, acesse a rota `/users/by_size` com o método GET passando o nome do arquivo por parâmetro.

```bash
curl -X 'GET' \
  'http://localhost:8000/users/by_size?filename=example' \
  -H 'accept: application/json'
```

##### Parâmetros
- `filename`: Nome do arquivo a ser processado.
- `order`: Exibe usuário com maior ou menor tamanho. Pode ser `min` ou `max`.

Exemplo:

```bash
curl -X 'GET' \
  'http://localhost:8000/users/by_size?filename=example&order=max' \
  -H 'accept: application/json'
```

#### Listar usuário pela quantidade de mensagens (Messages)
Para listar os usuários, acesse a rota `/users/by_messages` com o método GET passando o nome do arquivo por parâmetro.

```bash
curl -X 'GET' \
  'http://localhost:8000/users/by_messages?filename=example' \
  -H 'accept: application/json'
```

##### Parâmetros
- `filename`: Nome do arquivo a ser processado.
- `username`: Nome do usuário a ser filtrado.
- `min_messages`: Quantidade mínima de mensagens.
- `max_messages`: Quantidade máxima de mensagens.
- `page`: Página a ser exibida.

Exemplo:

```bash
curl -X 'GET' \
  'http://localhost:8000/users/by_messages?filename=example&min_messages=10&max_messages=20&page=1' \
  -H 'accept: application/json'
```

## Testes

O projeto possui 100% de cobertura de testes. Para rodar os testes, execute o seguinte comando:

```bash
coverage run -m pytest tests && coverage html --title="Cobertura de testes"
```

Após isso, acesse o diretório `app/htmlcov` e abra o arquivo `index.html` em seu navegador. Será exibido o relatório de cobertura de testes.

## Autor
Edwildson Coelho Rodrigues


