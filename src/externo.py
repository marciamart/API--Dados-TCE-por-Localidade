import requests

class APIexterna:
    def __init__(self):
        pass

    def tratarData(self, data, acao=None):
        if acao == 'ano':
            return int(data[:4]+'00')
        return int(data)

    def getCodMunicipio(self, municipio):
        url = 'https://api-dados-abertos.tce.ce.gov.br/municipios?nome_municipio={}'.format(municipio)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data'][0]["codigo_municipio"]
        else:
            return None
    
    def getCodOrgao(self, cod_municipio, date, nome):
        url = 'https://api-dados-abertos.tce.ce.gov.br/orgaos?codigo_municipio={}&exercicio_orcamento={}&nome_orgao={}'.format(cod_municipio, date, nome)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data'][0]['codigo_orgao']
        else:
            return None
        
    def getNomeCodNatureza(self,acao, cod_municipio, date, natureza):
        if acao == 'Nome':#tenho codigo da natureza
            url = 'https://api-dados-abertos.tce.ce.gov.br/despesa_categoria_economica?codigo_municipio={}&exercicio_orcamento={}&codigo_elemento_despesa={}'.format(cod_municipio, date, natureza)
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['data'][0]['nome_elemento_despesa']
            else:
                return None
        else: #tenho o nome da natureza
            url = 'https://api-dados-abertos.tce.ce.gov.br/despesa_categoria_economica?codigo_municipio={}&exercicio_orcamento={}'.format(cod_municipio, date)
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for item in data['data']:
                    if item['nome_elemento_despesa'] == natureza:
                        return item['codigo_elemento_despesa']
            else:
                return None


    def getInfoEmpenhos(self, cod_municipio, date, cod_orgao, natureza=None):
        if natureza != None:
            cod_natureza = self.getNomeCodNatureza('Cod', cod_municipio,self.tratarData(date, 'ano'),natureza)
            url = 'https://api-dados-abertos.tce.ce.gov.br/notas_empenhos?codigo_municipio={}&data_referencia_empenho={}&codigo_orgao={}&quantidade=100&deslocamento=0'.format(cod_municipio, date, cod_orgao)
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                #nome natureza, descrição, valor,data
                resultado = {'data':[]}
                for i in range(data['data']['length']):
                    if data['data']['data'][i]['codigo_elemento_despesa'] == cod_natureza:
                        resultado['data'].append(
                            {
                                'natureza_da_despesa': natureza,
                                'valor_empenhado': data['data']['data'][i]['valor_empenhado'],
                                'descricao_empenho': data['data']['data'][i]['descricao_empenho'],
                                'data_emissao_empenho': data['data']['data'][i]['data_emissao_empenho']
                            }
                        )
            else:
                return None
        else:
            url = 'https://api-dados-abertos.tce.ce.gov.br/notas_empenhos?codigo_municipio={}&data_referencia_empenho={}&codigo_orgao={}&quantidade=100&deslocamento=0'.format(cod_municipio, date, cod_orgao)
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                #nome natureza, descrição, valor,data
                resultado = {'data':[]}
                for i in range(data['data']['length']):
                        resultado['data'].append(
                            {
                                'natureza_da_despesa': self.getNomeCodNatureza('Nome', cod_municipio, self.tratarData(date, 'ano'),data['data']['data'][i]['codigo_elemento_despesa']),
                                'valor_empenhado': data['data']['data'][i]['valor_empenhado'],
                                'descricao_empenho': data['data']['data'][i]['descricao_empenho'],
                                'data_emissao_empenho': data['data']['data'][i]['data_emissao_empenho']
                            }
                        )
            else:
                return None
        return resultado
    
    def getFiltrarOrdenarAgentes(self, cod_municipio, orgao, cod_orgao, date):
        url = 'https://api-dados-abertos.tce.ce.gov.br/agentes_publicos?codigo_municipio={}&exercicio_orcamento={}&quantidade=100&deslocamento=0&codigo_orgao={}'.format(cod_municipio, date, cod_orgao)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            resultado = {f'{orgao}':[]}
            for i in range(data['data']['length']):
                resultado[f'{orgao}'].append(
                    {f'{data['data']['data'][i]['nome_servidor']}': [
                        {
                            'tipo_cargo': data['data']['data'][i]['nm_tipo_cargo'],
                            'valor_carga_horaria': data['data']['data'][i]['valor_carga_horaria']
                        }
                    ]}
                )
                resultado[f'{orgao}'] = sorted(resultado[f'{orgao}'], key=lambda x: list(x.keys())[0])
            return resultado
        else:
            return None