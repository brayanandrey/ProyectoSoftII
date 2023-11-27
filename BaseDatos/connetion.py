import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        # password='your_password',
        database='db_softwareii_final',
        port=3306
    )

def cerrar_conexion(connection, cursor):
    cursor.close()
    connection.close()

def insertar_incapacidad(descripcion, estado, Documento, Tipo_incapacidad):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Query para la inserción
        query = "INSERT INTO incapacidades (descripcion, estado, Documento, Tipo_incapacidad) VALUES (%s, %s, %s, %s)"
        data = (descripcion, estado, Documento, Tipo_incapacidad)

        # Ejecutar la inserción
        cursor.execute(query, data)
        connection.commit()
        print("Incapacidad insertada correctamente")

    except pymysql.Error as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        connection.rollback()

    finally:
        cerrar_conexion(connection, cursor)

def insertar_colaborador(Cargo, Documento, email, nombre):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Query para la inserción
        query = "INSERT INTO colaboradores (Cargo, Documento, email, nombre) VALUES (%s, %s, %s, %s)"
        data = (Cargo, Documento, email, nombre)

        # Ejecutar la inserción
        cursor.execute(query, data)
        connection.commit()
        
        print("Colaborador insertado correctamente")

    except pymysql.Error as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        connection.rollback()

    finally:
        cerrar_conexion(connection, cursor)
