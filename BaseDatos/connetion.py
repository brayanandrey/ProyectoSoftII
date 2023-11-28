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

def insertar_colaborador(Cargo, Documento, email, nombre, password):
    try:
        connection = conectar()
        cursor = connection.cursor()
        
        # Verificar si el colaborador ya existe
        query_verificacion = "SELECT * FROM colaboradores WHERE Documento = %s"
        data_verificacion = (Documento,)
        cursor.execute(query_verificacion, data_verificacion)

        if cursor.fetchone():
            print(f"El colaborador con Documento {Documento} ya existe en la base de datos.")
            return False

        # Query para la inserción
        query = "INSERT INTO colaboradores (Cargo, Documento, email, nombre, password) VALUES (%s, %s, %s, %s, %s)"
        data = (Cargo, Documento, email, nombre, password)

        # Ejecutar la inserción
        cursor.execute(query, data)
        connection.commit()
        
        print("Colaborador insertado correctamente")
        return True

    except pymysql.Error as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        connection.rollback()
        return False

    finally:
        cerrar_conexion(connection, cursor)


#get document from colaborador by email
def obtener_ID_colaborador(email):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener el documento del colaborador
        query = "SELECT Documento FROM colaboradores WHERE Email = %s"
        cursor.execute(query, (email,))

        # Obtiene el resultado de la consulta
        result = cursor.fetchone()

        return result

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)
        
def obtener_datos_incapacidades(ID_Colaborador):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades
        query = "SELECT Estado, Tipo_incapacidad, nombre_archivo FROM incapacidades WHERE ID_Colaborador = %s"
        cursor.execute(query, (ID_Colaborador,))

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)
        
import pymysql

def verificar_credenciales(email, password):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener la contraseña del email dado
        query = "SELECT password FROM colaboradores WHERE Email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # Verifica si se encontró el email y compara las contraseñas
        if result and result[0] == password:
            print("Credenciales válidas")
            return True
        else:
            print("Credenciales inválidas")
            return False

    except pymysql.Error as e:
        print(f"Error al verificar credenciales: {e}")
        return False

    finally:
        cerrar_conexion(connection, cursor)


