from flask import Flask,request,jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
print("Iniciando el servidor en el puerto por defecto 5000")

@app.route("/")
def hello_world():
    return jsonify({"MSG":"Hola a todos esto es de parte de flask"})  
#Ejemplo
#http://localhost:5000/UsuarioConectado?nombreUser=Oscar Leon
@app.route("/UsuarioConectado",methods=['GET'])
def UsuarioConectado():
    nombreUser = request.args.get('nombreUser')
    return jsonify({"Nombre":nombreUser})  


@app.route("/ObtenerDatos",methods=['POST'])
def ObtenerDatos():
    perfil = request.get_json()
    print(perfil)
    if perfil["id"]==1:

        return jsonify({"MSG":"Usuario bloqueado, Juan debe dinero"})  
    return jsonify({"MSG":"Tu si puedes pasar"})  