from flask import Flask, render_template, request
import pandas as pd
import json
import datetime
from collections import defaultdict

db = {}

def serializar(obj):
    if isinstance(obj, datetime.time):
        return obj.strftime('%H:%M:%S')

# Função para calcular a média das horas
def converter_segundos(valor_segundos):
    if pd.isnull(valor_segundos):  # Verifica se é NaN
        return '00:00:00'
    return str(datetime.timedelta(seconds=valor_segundos))

app = Flask('app')


@app.route('/', methods=['GET', 'POST'])
def index():
    db = {}
    mediaSemana = ""
    mediaMes = ""
    mediaAno = ""
    QTMesTemp = 0
    listaTempo = []

    if request.method == 'POST':
        arquivo = request.files['arquivo']

        if arquivo:
            tabela = pd.read_excel(arquivo)
            for index, row in tabela.iterrows():
                if str(row.values[0]) != "nan":
                    ano = int(row["Ano"])
                    mes = str(row["Mês"])
                    QTMes = int(row["Qnt. trens mês"])
                    
                    prefixo = row["Prefixo"]

                    fila = serializar(row["Fila"])
                    agEncoste = serializar(row["Ag. Encoste"])
                    encoste =  serializar(row["Encoste"])
                    operacao =  serializar(row["Operação Brado"])
                    formacao =  serializar(row["Formação"])
                    partida =  serializar(row["Partida"])

                    # fila = row["Fila"]
                    # agEncoste = row["Ag. Encoste"]
                    # encoste = row["Encoste"]
                    # operacao = row["Operação Brado"]
                    # formacao = row["Formação"]
                    # partida = row["Partida"]
                    

                    if ano not in db:
                        db[ano] = {}        

                    if mes not in db[ano]:
                        db[ano][mes] = {"mediaSemana":mediaSemana, "mediaMes":mediaMes, "mediaAno":mediaAno, "QTMês":None, "locomotivas":[]}

                    if mes in db[ano]:
                        if QTMes > QTMesTemp:
                            QTMesTemp = QTMes
                        else:
                            db[ano][mes]["QTMês"] = QTMes

                        db[ano][mes]["locomotivas"].append({"prefixo":prefixo, "etapas":{"fila":fila, "ag.encoste":agEncoste, "encoste":encoste, "operação":operacao, "formação":formacao, "partida":partida}})

            # with open(r"database.json", "w+") as file:
            #     file.write(json.dumps(db)) 

            dados = []

            # Iterar sobre o dicionário para criar a lista de dados
            for ano, meses in db.items():
                for mes, dados_mes in meses.items():
                    for locomotiva in dados_mes.get("locomotivas", []):
                        prefixo = locomotiva["prefixo"]
                        etapas = locomotiva["etapas"]
                        dados.append({
                            "Ano": ano,
                            "Mês": mes,
                            "Prefixo": prefixo,
                            "Fila": etapas["fila"],
                            "Ag.Encoste": etapas["ag.encoste"],
                            "Encoste": etapas["encoste"],
                            "Operação": etapas["operação"],
                            "Formação": etapas["formação"],
                            "Partida": etapas["partida"]
                        })

            df = pd.DataFrame(dados)

            colunas_tempo = ["Fila", "Ag.Encoste", "Encoste", "Operação", "Formação", "Partida"]
            for coluna in colunas_tempo:
                df[coluna] = pd.to_timedelta(df[coluna])

            for coluna in colunas_tempo:
                df[coluna] = df[coluna].dt.total_seconds()


            agregacoes = {}
            for col in colunas_tempo:
                agregacoes[col] = "mean"

            media_mensal = df.groupby(["Ano", "Mês"]).agg(agregacoes)

            for col in colunas_tempo:
                media_mensal[col] = media_mensal[col].apply(converter_segundos)

            print(media_mensal)
                            
        return render_template("graphpage.html")

    return render_template('index.html')

@app.route('/graph')
def graph():
    return render_template('graphpage.html')

if __name__ == "__main__":
  app.run(debug=True)