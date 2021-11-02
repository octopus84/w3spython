import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='192.168.1.20',
        port=3306,
        user='sensor',
        password='sensor',
        db='sensores'
    )    
    try:
        if conexion.is_connected():
            print("Conexión exitosa.")
            infoServer = conexion.get_server_info()
            print("Info del servidor:", infoServer)
    except Error as ex:
        print("Error durante la conexión:", ex)
    finally:
        if conexion.is_connected():
            conexion.close()  # Se cerró la conexión a la BD.
            print("La conexión ha finalizado.")
except Error as ex:
    print("Error durante la conexión:", ex)