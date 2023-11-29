import pymysql
from datetime import date

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

def insertar_incapacidad(descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo, fecha_entrega):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Query para la inserción
        query = "INSERT INTO incapacidades (descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo, Fecha_entrega) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo, fecha_entrega)

        # Ejecutar la inserción
        cursor.execute(query, data)
        connection.commit()
        print("Incapacidad insertada correctamente")

    except pymysql.Error as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        connection.rollback()

    finally:
        cerrar_conexion(connection, cursor)

def insertar_colaborador(Cargo, Documento, email, nombre, password, mensajes):
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
        query = "INSERT INTO colaboradores (Cargo, Documento, email, nombre, password, mensajes) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (Cargo, Documento, email, nombre, password, mensajes)

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
        
#get name from colaborador by document
def obtener_nombre_colaborador(Documento):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener el nombre del colaborador
        query = "SELECT nombre FROM colaboradores WHERE Documento = %s"
        cursor.execute(query, (Documento,))

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

def verificar_credenciales_jefe(email, password):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener la contraseña del email dado
        query = "SELECT password FROM jefe_inmediato WHERE Email = %s"
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
        
def obtener_incapacidades_jefe(Documento):
    try:
        connection = conectar()
        cursor = connection.cursor()
        
        query = "SELECT Estado, Tipo_incapacidad, ID_Colaborador, Fecha_Entrega, nombre_archivo FROM incapacidades WHERE ID_Colaborador = %s"
        # Realiza la consulta para obtener los datos de la tabla incapacidades
        cursor.execute(query, (Documento,))

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)
        

def obtener_datos_incapacidades_con_nombre(ID_Colaborador):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades con el nombre del colaborador
        query = """
            SELECT i.Estado, i.Tipo_incapacidad, i.nombre_archivo, c.nombre
            FROM incapacidades i
            JOIN colaboradores c ON i.ID_Colaborador = c.Documento
            WHERE i.ID_Colaborador = %s
        """
        cursor.execute(query, (ID_Colaborador,))

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)

""" def insertar_incapacidad(descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Agregar la fecha actual al registro
        fecha_registro = date.today()

        # Query para la inserción
        query = "INSERT INTO incapacidades (descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo, Fecha_Registro) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (descripcion, estado, ID_Colaborador, Tipo_incapacidad, documentacion, nombre_archivo, fecha_registro)

        # Ejecutar la inserción
        cursor.execute(query, data)
        connection.commit()
        print("Incapacidad insertada correctamente")

    except pymysql.Error as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        connection.rollback()

    finally:
        cerrar_conexion(connection, cursor) """

""" def obtener_datos_incapacidades(ID_Colaborador):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades
        query = "SELECT Estado, Tipo_incapacidad, nombre_archivo, Fecha_Registro FROM incapacidades WHERE ID_Colaborador = %s"
        cursor.execute(query, (ID_Colaborador,))

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor) """
        
def obtener_colaboradores():
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades
        query = "SELECT ID_Colaborador FROM incapacidades"
        cursor.execute(query)

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)
        
#update messages from colaborador
def actualizar_mensajes(Documento, mensajes):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades
        query = "UPDATE colaboradores SET mensajes = %s WHERE Documento = %s"
        cursor.execute(query, (mensajes, Documento))

        # Obtiene todos los resultados de la consulta
        connection.commit()
        print("Mensajes actualizados correctamente")

    except pymysql.Error as e:
        print(f"Error al actualizar datos de la base de datos: {e}")
        connection.rollback()

    finally:
        cerrar_conexion(connection, cursor)
        
#get message from colaborador
def obtener_mensajes(Documento):
    try:
        connection = conectar()
        cursor = connection.cursor()

        # Realiza la consulta para obtener los datos de la tabla incapacidades
        query = "SELECT mensajes FROM colaboradores WHERE Documento = %s"
        cursor.execute(query, (Documento,))

        # Obtiene todos los resultados de la consulta
        results = cursor.fetchone()

        return results

    except pymysql.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")

    finally:
        cerrar_conexion(connection, cursor)