from flask import Flask, render_template, request
import openpyxl

app = Flask('app')


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    arquivo = request.files['arquivo']

    if arquivo:
      arquivo.save(arquivo.filename)
      
      return render_template("graphpage.html")

    else:
      return 'Nenhum arquivo selecionado'

  return render_template('index.html')

@app.route('/graph')
def graph():
  return render_template('graphpage.html')

if __name__ == "__main__":
  app.run(debug=True)