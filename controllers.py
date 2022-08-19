# Creado por

from asyncio.windows_events import NULL
from app import app
from flask import render_template
import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='facturacion')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/")
def index():
    return render_template('index.html', titulo='Home')

@app.route("/usuarios")
def usuarios():
    return render_template('users.html', titulo='Control Usuarios')

def obtener_productos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_producto, nombre_producto, valor_unitario, unidad_medida, cantidad_stock, id_categoria FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos

@app.route("/productos")
def productos():
    productos = obtener_productos()
    return render_template('productos.html', titulo='Gestión de Productos', lista_productos=productos)

@app.route("/crear_producto")
def crear_producto():
    return render_template('crear_producto.html', titulo='Nuevo Producto')