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

def insertar_incapacidad(descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Query para la inserción
        query = "INSERT INTO incapacidades (descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo)

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
        
        # Verificar si el colaborador ya existe
        query_verificacion = "SELECT * FROM colaboradores WHERE Documento = %s"
        data_verificacion = (Documento,)
        cursor.execute(query_verificacion, data_verificacion)

        if cursor.fetchone():
            print(f"El colaborador con Documento {Documento} ya existe en la base de datos.")
            return  # Puedes decidir no realizar la inserción o manejarlo de otra manera

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
        
def obtener_datos_incapacidades():
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades
        query = "SELECT Estado, Tipo_incapacidad, nombre_archivo FROM incapacidades"
        cursor.execute(query)

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)

