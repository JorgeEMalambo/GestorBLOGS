import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        con.close()
sql_connection()

def crear_bd_blogs():
    conexion = sqlite3.connect("blogs.db")
    cursor = conexion.cursor()
    print("1")
    try:
        cursor.execute('''CREATE TABLE usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER UNIQUE NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                apellidos VARCHAR(100) NOT NULL, 
                correo VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL)
                ''')

    except sqlite3.OperationalError:
        print("La tabla de usuarios ya existe.")
    conexion.close()

crear_bd_blogs()

def crear():
    id_usuario= 9992
    usuario= 'angela2'
    apellidos= 'alarcon2'
    correo= 'correojmt.com2'
    password= '12342'

    agregar_usuario(id_usuario,usuario,apellidos,correo,password)
    '''AQUI SE DEBEN LLAMAR LOS CAMPOS Y ENVIARLOS POR REFERENCIA A LA FUNCION'''

def agregar_usuario(id_usuario,usuario,apellidos,correo,password):
    '''id_usuario = input("¿Documento del nuevo usuario?\n> ")
    usuario    = input("¿Nombre del nuevo usuario?\n> ")'''
    id_usuario=id_usuario
    usuario=usuario
    apellidos=apellidos
    correo=correo
    password=password

    conexion = sqlite3.connect("blogs.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO usuario VALUES (null, '{}' , '{}' , '{}' , '{}' , '{}')".format(
            id_usuario,usuario,apellidos,correo,password) )
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe.".format(usuario))
    else:
        print("USUARIO '{}' creado correctamente.".format(usuario))

    conexion.commit()
    conexion.close()
crear()

def mostrar_usuario():

    conexion = sqlite3.connect("blogs.db")
    cursor = conexion.cursor()

    user = cursor.execute("SELECT * FROM usuario").fetchall()
    print("user: ",user)

    conexion.close()
mostrar_usuario()