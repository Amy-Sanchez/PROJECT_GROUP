from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client['egresos']
collection = db['atendidos']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        provincia = request.form['provincia']
        clase = request.form['clase']
        sector = request.form['sector']
        mes = request.form['mes']
        sexo = request.form['sexo']
        edad = request.form['edad']
        dias_estadia = request.form['dias_estadia']
        
        document = {
            'id': id,
            'nombre': nombre,
            'provincia': provincia,
            'clase': clase,
            'sector': sector,
            'mes': mes,
            'sexo': sexo,
            'edad': edad,
            'dias_estadia': dias_estadia
        }
        
        collection.insert_one(document)
        
        return "Registro guardado exitosamente"
    
    return render_template('form.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    id = request.args.get('buscar_id')
    registro = collection.find_one({'id': id})
    return render_template('leer.html', registro=[registro])

@app.route('/eliminar', methods=['POST'])
def eliminar():
    id = request.form['id']
    collection.delete_one({'_id': ObjectId(id)})

    return "Registro eliminado exitosamente"


if __name__ == '__main__':
    app.run(debug=True)