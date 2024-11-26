from flask import Flask, request, jsonify
from main import db, app
from models.usuario import Usuario





@app.route('/')
def index():
 return "Conexão com o banco de dados "

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')
    print(email)
    print(senha)
  
  
    user = Usuario.query.filter_by(email=email).first()
    
    if user and user.senha == senha:
        return jsonify({'mensagem':'Login foi realizado com sucesso.'}),200
    else:
        return jsonify({'mensagem':'Seu login não foi realizado com sucesso'}),401


@app.route('/cadastro', methods = ['POST'])
def cadastro():
    data = request.json
    nome = data.get('nome')
    email = data.get ('email')
    senha = data.get ('senha')

    user = Usuario(nome= nome, email= email , senha= senha)
    db.session.add(user)
    db.session.commit()
    return jsonify({'mensagem':'Seu cadastro foi realizado com sucesso'}),201
   
