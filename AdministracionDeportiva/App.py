from urllib import request
from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
import config
import smtplib



app = Flask(__name__)

#conexion con oracle
'''
connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # imprime la version de la base de datos
    print("conectado",connection.version)
    cursor= connection.cursor()
    sentencia=cursor.execute("SELECT * FROM prueba")
    rows = cursor.fetchall()
    print(rows)

    #oracle = oracle(app)
    for row in rows:
        print(row)
except cx_Oracle.Error as error:
    print(error)

finally:
    # release the connection
    if connection:
        print("cerrar conexion")
        #connection.close()
'''
# configuracion de session
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    #cursor = connection.cursor()
    #cursor.execute('SELECT idempleado, nombre, apellido, nombrecargo FROM empleado e, cargo c where e.idcargo = c.idcargo')
    data = [['1','juan','perro','esclavo']]
    #cursor.execute('SELECT * FROM cargo')
    cargos = [['1','esclavo']]
    print(data)
    return render_template('index.html', datos = data, cargos = cargos)

@app.route('/empleados', methods=['POST'] )
def empleados():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        idcargo = request.form['cargos']
        #cursor = connection.cursor()
        #cursor.execute('INSERT INTO empleado(nombre, apellido, idcargo) VALUES (:nombre, :apellido, :idcargo )',[nombre, apellido, idcargo])
        #connection.commit()
        flash('Empleado agregado')
        return redirect(url_for('Index'))

@app.route('/eliminar/<idempleado>')
def eliminarEmpleado(idempleado):
   # cursor = connection.cursor()
    #cursor.execute('DELETE FROM empleado WHERE idempleado = :idempleado',[idempleado])
    #connection.commit()
    flash('Empleado eliminado')
    return redirect(url_for('Index'))

@app.route('/editar/<idempleado>')
def editarEmpleado(idempleado):
    #cursor = connection.cursor()
    #cursor.execute('SELECT * FROM empleado WHERE idempleado = :idempleado',[idempleado])
    data = [['1','juan','perro','esclavo']]
    #cursor.execute('SELECT * FROM cargo')
    cargos = [['1','esclavo']]
    return render_template('editarEmpleado.html',dato = data[0], cargos = cargos)

@app.route('/actualizarEmpleado/<idempleado>', methods=['POST'] )
def actualizarEmpleado(idempleado):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        idcargo = request.form['cargos']
        #cursor = connection.cursor()
        #cursor.execute('UPDATE empleado SET nombre = :nombre, apellido = :apellido, idcargo = :idcargo WHERE idempleado = :idempleado',[nombre, apellido, idcargo, idempleado])
        #connection.commit()
        flash('Empleado actualizado')
        return redirect(url_for('Index'))

if __name__=='__main__':
    app.run(port = 3000, debug = True)