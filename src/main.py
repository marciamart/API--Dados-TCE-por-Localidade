from fastapi import  FastAPI, HTTPException, Query
from externo import APIexterna

app = FastAPI(
    title='Dados TCE Ceará',
    description='Resumo de alguns dos dados distribuidos pela API de dados abertos do TCE-CE (https://api-dados-abertos.tce.ce.gov.br/docs)',
    version='1.0.0'
)   

apiexterna = APIexterna()

@app.get('/empenho_de_gastos/{municipio}', tags=['Resumo'], summary='Retorna gastos empenhados por município')
def notas_gastos(municipio: str , 
                 orgao: str = Query(description='Nome do orgão que deseja saber o destino dos seus empenhos'),
                 date: str = Query(description='Forneça o ano e mês que deseja verificar no formato yyyymm'), 
                 natureza: str = Query(None, description='Nome da natureza do empenho que deseja')):
    try:
        cod_municipio = apiexterna.getCodMunicipio(municipio)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Município '{municipio}' não encontrado: {e}")

    try:
        cod_orgao = apiexterna.getCodOrgao(cod_municipio, apiexterna.tratarData(date, 'ano'), orgao)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Órgão '{orgao}' não encontrado para o município '{municipio}': {e}")

    try:
        if natureza:
            resultado = apiexterna.getInfoEmpenhos(cod_municipio, date, cod_orgao, natureza)
        else:
            resultado = apiexterna.getInfoEmpenhos(cod_municipio, date, cod_orgao)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter dados de empenhos: {e}")

@app.get('/agentes_publicos', tags=['Resumo'], summary='Resumo dos funcionários por determinada orgão')
def agentes(municipio: str = Query(description='Nome do município'), 
            orgao: str = Query(description='Nome do orgão que deseja saber o destino dos seus empenhos'), 
            date: str = Query(description='Forneça o ano e mês que deseja verificar no formato yyyymm'), 
            ordenar: str = 'ordem alfabetica'):
    try:
        cod_municipio = apiexterna.getCodMunicipio(municipio)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Município '{municipio}' não encontrado: {e}")

    try:
        cod_orgao = apiexterna.getCodOrgao(cod_municipio, apiexterna.tratarData(date, 'ano'), orgao)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Órgão '{orgao}' não encontrado para o município '{municipio}': {e}")

    try:
        resultado = apiexterna.getFiltrarOrdenarAgentes(cod_municipio, orgao, cod_orgao, apiexterna.tratarData(date, 'ano'))
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter dados de agentes públicos: {e}")