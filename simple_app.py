#Importamos FLask
from flask import Flask
#importar una variable global que tenga toda la info de nuestra request
#esta va a tener toda la informacion que viene de nuestra peticion http
from flask import request
#Importamos render_template para organizar nuestras temples y separar
#el codigo hmtl en otro archivo.
from flask import render_template

#Lo siguiente se encarga de lidear con los lines spaces en python.
#Le indica a FLask que si esto lo corres directamente es lo que se va a
#ejecutar en la consola, hace que esta aplicacion se apunte a si misma
#Esta aplicacion apunte a si misma.
app = Flask(__name__)

                                #VISTAS
#route  o rutas se utilizan para decirle a flask que vistas y listas son las
#que hay que cargar. Cuando pones "/" indica que sera la vista principal
#cuando los usuarios no ponen nada mas
#"/<name>" todo lo que venga despues de nuestra "/" lo muestre como name,
#asi evitamos urls demasiado largas trabajando con sus querys.
#Esto es netamente visial.
#Podemos asignar mas de una ruta a la misma vista "def".
@app.route("/")
@app.route("/<name>")
def index(name = "Mundo"):
    #Buscamos Obtener .get los argumentos .args del request cuyo parametro
    #sea "name".
    #name = request.args.get("name",name)
    #cambiamos name por context
    context = {"name" : name}
    return render_template("index.html", **context)

@app.route("/add/<float:num1>/<float:num2>")
@app.route("/add/<int:num1>/<int:num2>")
@app.route("/add/<int:num1>/<float:num2>")
@app.route("/add/<float:num1>/<int:num2>")
def add(num1,num2):
    #creamos un diccionario "contexto" para pasar las variables juntas.
    context = {"num1" : num1,"num2" : num2}
    return render_template("add.html", **context)

#Siempre que se ejecuta un script de flask se le llama aplicacion.
#debug = True,queremos que nos muestre todos los errores, si los hay.
#port es el puerto 8000 por lo general libre
#host 0.0.0.0 va a escuchar a todas las conexiones que se pueden conectar
#a nuestra computadora, sino poner 127.0.0.1,solo va a escuchar conexiones
#locales
app.run(debug = True, port = 8000, host = "0.0.0.0")
