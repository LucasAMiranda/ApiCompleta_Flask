from  flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
     'id': '0',
     'nome': 'Lucas',
     'habilidades': ['Python', 'Flask']
     },

    {
     'id': 1,
     'nome': 'Miranda',
     'habilidades': ['Python', 'Django']
     },
]

#Devolve um desenvolvedor por id e também deleta e altera os desenvolvedores
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desevolvedor(id):
    if request.method == 'GET':
         try:
             response = desenvolvedores[id]
         except IndexError:
             mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
             response = {'status': 'Error', 'mensagem': mensagem }
         except Exception:
             mensagem = 'Erro desconhecido . Procure o adm da API'
             response = {'status': 'Error',  'mensagem': mensagem}
         return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
         desenvolvedores.pop(id)
         return jsonify({'status': 'Success', 'mensagem': 'Registro excluído com sucesso'})

#Permite registrar um novo desenvolvedor e Lista todos os desenvolvedores
@app.route('/dev/', methods=['POST', 'GET'] )
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)