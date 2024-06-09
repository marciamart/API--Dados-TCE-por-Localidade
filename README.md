## API - Resumo de dados do TCE-Ceará
### *Descrição:*
Aqui temos  a primeira versão de uma RESTFul API que irá resumir de modo geral os dados passados pela a API de dados abertos do TCE-CE (https://api-dados-abertos.tce.ce.gov.br/docs)

### ***Neste repositório estão:***
- Dockerfile: arquivo com as configurações do container
***src:*** pasta raiz contendo o código fonte da aplicação
arquivos:
    - main.py: apresenta as rotas e toda a lógica po trás da API
    - externo.py: possui a classe que lida com o tratamento dos dados tragos pela a API externa 

## *Tecnologias utilizadas:*
* Docker
* Python:
    * FastAPI
    * uvicorn (Documentação)

## *como utilizar:*
Há duas maneiras de utilizar a aplicação:
    - com o proprio terminal 
    - com container Docker

    ambas comecam com o mesmo passo:
    1. Clone o repsitório na sua máquina:
    ````
    git clone https://github.com/marciamart/API-Dados-TCE-CE

- com o proprio terminal
    2. garanta que todas as bibliotecas da do arquivo requeriments.txt estejam instaladas em seu aparelho:
    ````
    pip install <biblioteca_desejada>
    ````
    3. Entre na pasta ````src```` 
    4. E por último chame o comando para executar em sua máquina:
    ````
    uvicorn main:app --reload
    ````

    Assimm o uvicorn irá fornecer a url para a Aplicação.
    Para entrar na Documentação basta adicionar ao final da URL fornecida pelo uvicorn ````/docs````

- com container Docker
    2. garanta que o Docker esteja instalado em sua máquina e pronto para receber uma imagem:
    para mais informações acesse: https://docs.docker.com/

    3. Abra no terminal o arquivo clonado e crie uma imagem docker:
    ````
    docker build -t fastapi/simple .

    4. em seguida, rode a aplicação com o comando:
    ````
    docker run -p 8000:8000 fastapi/simple

    Agora você já pode acessar a API e sua documentação utilizando  http://localhost:8000/docs