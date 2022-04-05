# Importo todo de la libreria 'Sqlite'
import sqlite3

# Función conectar a la base de datos
def conectar():
    conexion = sqlite3.connect("BD/agenda.sqlite3")
    cursor = conexion.cursor()
    return conexion, cursor

# Función para crear la tabla con sus respectivos campos
def crearTabla():
    conexion, cursor = conectar()
    sql = """
    CREATE TABLE IF NOT EXISTS agenda(
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Nombre TEXT NOT NULL,
    Apellido TEXT NOT NULL,
    Telefono TEXT NOT NULL,
    Direccion TEXT NOT NULL) """
    if(cursor.execute(sql)):
        print("Tabla creada con éxito")
    else:
        print("Ha ocurrido un error al crear la tabla")
    conexion.close()

# Función para insertar registros
def insertar(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO agenda(Nombre, Apellido, Telefono, Direccion)
    VALUES (?, ?, ?, ?) """
    if (cursor.execute(sql, datos)):
        print("Datos guardados con éxito")
    else:
        print("Ha ocurrido un error al guardar los datos")
    conexion.commit()
    conexion.close()

# Función para consultar los registros
def consultar():
    conexion, cursor = conectar()
    sql = "SELECT Id, Nombre, Apellido, Telefono, Direccion FROM agenda"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)
    listado.sort()
    conexion.close()
    return listado

# Función para actualizar registros
def modificar(id, nombre, apellido, telefono, direccion):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET Nombre='"+nombre+"',Apellido='"+apellido+"', Telefono='" + \
        telefono+"', Direccion='"+direccion + \
        "' WHERE Id="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

# Función para borrar registros
def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE FROM agenda WHERE Id="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
