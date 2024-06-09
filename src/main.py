from fastapi import  FastAPI
from externo import APIexterna

app = FastAPI(
    title='Dados TCE Ceará',
    description='Resumo de alguns dos dados distribuidos pela API de dados abertos do TCE-CE (https://api-dados-abertos.tce.ce.gov.br/docs)',
    version='1.0.0'
)   

apiexterna = APIexterna()

@app.get('/empenho_de_gastos/{municipio}', tags=['Resumo'], summary='Retorna gastos empenhados por município')
def notas_gastos(municipio:str,orgao:str, date:str, natureza:str = None):
    cod_municipio = apiexterna.getCodMunicipio(municipio)
    cod_orgao = apiexterna.getCodOrgao(cod_municipio, apiexterna.tratarData(date,'ano'), orgao)
    if natureza:
        resultado = apiexterna.getInfoEmpenhos(cod_municipio, date, cod_orgao, natureza)
    else:
        resultado = apiexterna.getInfoEmpenhos(cod_municipio, date, cod_orgao)
    return resultado

@app.get('/agentes_publicos', tags=['Resumo'], summary='Resumo dos funcionarios por determinada unidade')
def agentes(municipio:str, orgao:str, date:str, ordenar: str = 'ordem alfabetica'):
    cod_municipio = apiexterna.getCodMunicipio(municipio)
    cod_orgao = apiexterna.getCodOrgao(cod_municipio, apiexterna.tratarData(date,'ano'), orgao)
    resultado = apiexterna.getFiltrarOrdenarAgentes(cod_municipio, orgao, cod_orgao, apiexterna.tratarData(date,'ano'))
    return resultado