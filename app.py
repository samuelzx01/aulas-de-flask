#introdução ao flask - frmework python para aplicações web
#ruqisiçoes web -GRT E POST
#instalando biblioteca -> pip install flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    #enviando variaveis para o html
    nome = 'joão'
    idade = 30
    email = 'joaosilva@gmail.com'
    return render_template("index.html", name = nome, idade = idade,email = email)

@app.route('/dicionarios')
def dicionarios():
    # enviando dicionarios para o html
    usuario = {
    "nome": "joao",
    "idade": 20,
    "email": "joaosilva@gmail.com"
    }

    return render_template('dicionarios.html', usuario = usuario)


@app.route('/condicionais')
def condicionais():
    nota = 10
    logado = True
    usuario = {
    "nome": "joao",
    "idade": 20,
    "email": "joaosilva@gmail.com"
    }

    return render_template('condicionais.html', logado = logado,usuario = usuario,nota = nota)
    

@app.route('/listas')
def listas():
    listaUsuarios = ['maria', 'joao', 'andre', 'sara']


    return render_template('listas.html', listaUsuarios = listaUsuarios)
    



    
if __name__ == '__main__':
    app.run(debug=True)