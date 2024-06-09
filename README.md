# API - Resumo de Dados do TCE-Ceará

## Descrição

Esta é a primeira versão de uma API RESTful que resume os dados fornecidos pela API de dados abertos do TCE-CE (https://api-dados-abertos.tce.ce.gov.br/docs).

## Conteúdo do Repositório

- **Dockerfile:** Arquivo com as configurações do container.
- **src:** Pasta raiz contendo o código fonte da aplicação:
  - **main.py:** Contém as rotas e a lógica da API.
  - **externo.py:** Classe responsável pelo tratamento dos dados fornecidos pela API externa.

## Tecnologias Utilizadas

- **Docker**
- **Python**:
  - **FastAPI**
  - **Uvicorn**

## Como Utilizar

Você pode utilizar a aplicação de duas maneiras:
1. **Terminal**
2. **Container Docker**

### 1. Usando o Terminal

1. Clone o repositório na sua máquina:
   ```
   git clone https://github.com/marciamart/API-Dados-TCE-CE

2. Garanta que todas as bibliotecas do arquivo ````requirements.txt```` estejam instaladas:
    ````
    pip install <biblioteca_desejada>
    ````
3. Entre na pasta ````src```` 
4. E por último, execute o comando para iniciar a aplicação:
    ````
    uvicorn main:app --reload

E assim o uvicorn irá fornecer a url para a Aplicação.
Para acessar a documentação, adicione ````/docs```` ao final da URL fornecida.

### 2. Usando Container Docker
1. Clone o repositório na sua máquina:
   ```
   git clone https://github.com/marciamart/API-Dados-TCE-CE

2. Certifique-se de que o Docker está instalado na sua máquina. Para mais informações, acesse: https://docs.docker.com/

3. Abra no terminal o arquivo clonado e crie uma imagem docker:
    ````
    docker build -t fastapi/simple .

4. Em seguida, execute a aplicação com o comando:
    ````
    docker run -p 8000:8000 fastapi/simple

Agora você já pode acessar a API e sua documentação utilizando  ````http://localhost:8000/docs````
