import pymysql

# Conexión a la base de datos
connection = pymysql.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    database='registro_incapacidades',
    port=3306  # Puerto predeterminado para MySQL
)

# Crear un objeto cursor para ejecutar consultas SQL
cursor = connection.cursor()

# Ejecutar consultas SQL
cursor.execute("SELECT * FROM registro_incapacidades")
results = cursor.fetchall()

# Procesar los resultados
for row in results:
    # Acceder a los datos de cada fila
    print(row)
    
# Cerrar cursor y conexión
cursor.close()
connection.close()