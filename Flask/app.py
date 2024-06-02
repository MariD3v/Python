from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

app = Flask(__name__) 

@app.route('/') #En la direccion / se ejecutará la función de debajo
def index():
    return 'hola mundo'

@app.route('/publicaciones/<id_publicacion>') #Hemos definido la variable id_publicacion que se usa en la función de debajo.
def publicaciones(id_publicacion):
    return 'El id de esta publicación es '+ id_publicacion

@app.route('/metodos', methods=['GET', 'POST']) #Los métodos de HTTP son: GET, POST, PUT, PATCH, DELETE
def metodos():
    if request.method == 'GET':
        return 'Se ha accedido a esta página con el método GET'
    else:
        return 'Se ha accedido a esta página con el método POST'
    
@app.route('/formulario', methods=['POST']) 
def formulario():
    print(request.form) #Para hacer la petición ponemos en la terminal curl -d "llave1=data1&llave2=data2" -X POST http://localhost:5000/formulario
    print(request.form['llave1']) #Para obtener solo 1 dato de la petición
    print(url_for('publicaciones', id_publicacion=2)) #Asi construimos una url para redireccionar al usuario cuando haga una peticion
    return 'Esto es un ejemplo de formulario'

@app.route('/redireccionar')
def redireccionar():
    #abort(403) #Muestra en pantalla el error que queramos, se puede usar para modificar esa página de error y mostrarla más bonita, cuando el usuario tenga algun error.
    return redirect(url_for('publicaciones', id_publicacion=3)) #Así se redireccionar a otro @app.route

@app.route('/pantillas')
def pantillas():
    return render_template('plantilla.html') #Para importar plantillas html, creamos la carpeta "templates", donde meteremos nuestros archivos 

@app.route('/json')
def json():
    return { #Asi se retorna un json (diccionario)
        "nombre":'Mari',
        "edad": 23
    }

@app.route('/mensaje', methods=['GET'])
def mensaje():
    return render_template('mensaje.html', mensaje='Soy un mensaje pasado desde .py') #Así pasamos un mensaje desde .py a html

@app.route('/plantillaextendida') #Aqui pasamos parámetros desde una plantilla hijo a una plantilla base
def plantillaextendida():
    return render_template('plantillahijo.html', mensaje= 'Soy un mensaje pasado desde un .py a la plantilla hijo y de la plantilla hijo a la plantilla base')

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='CEEF91493AFC41C7DF70CBB417A888E51706632561BA6FAEDA4287FE3DAF8D4E',
    database='prueba'
)
cursor = midb.cursor() #Si entre () ponemos dictionary = True, nos devuelve los datos en forma de diccionario
cursor.execute('select * from Usuario')
usuario = cursor.fetchall()

@app.route('/basededatos') #Aqui pasaremos parámetros de ls bd a nuestra web
def basededatos():
    return render_template('basededatos.html', usuarios = usuario) #Pasamos el parámetro usuario a el html

@app.route('/creardataenbd', methods = ['GET', 'POST'])
def creardataenbd():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into Usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('basededatos'))
    return render_template('creardata.html')