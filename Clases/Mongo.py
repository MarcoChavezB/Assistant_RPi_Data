import pymongo
from sshtunnel import SSHTunnelForwarder

# Configuración de la conexión SSH
SSH_HOST = 'ssh_host'  # Dirección del servidor SSH
SSH_PORT = 22  # Puerto SSH
SSH_USER = 'ssh_username'  # Nombre de usuario SSH
SSH_KEY = 'path/to/ssh/key'  # Ruta a la clave privada SSH (si se usa la autenticación de clave)
MONGO_HOST = 'mongo_host'  # Dirección del servidor MongoDB en la red interna (generalmente 'localhost')
MONGO_PORT = 27017  # Puerto de MongoDB en el servidor interno

# Configuración de la conexión a MongoDB
MONGO_DB = 'database_name'  # Nombre de la base de datos MongoDB
MONGO_USER = 'mongo_username'  # Nombre de usuario de MongoDB (si es necesario)
MONGO_PASS = 'mongo_password'  # Contraseña de MongoDB (si es necesario)

# Configuración del túnel SSH
with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_pkey=SSH_KEY,  # Opcional si estás utilizando autenticación de clave SSH
    remote_bind_address=(MONGO_HOST, MONGO_PORT)
) as tunnel:
    # Establecer la conexión a MongoDB a través del túnel SSH
    client = pymongo.MongoClient('localhost', tunnel.local_bind_port)
    db = client[MONGO_DB]

    # Autenticar si es necesario
    if MONGO_USER and MONGO_PASS:
        db.authenticate(MONGO_USER, MONGO_PASS)

    # Ejemplo: consultar una colección
    collection = db['collection_name']
    for doc in collection.find():
        print(doc)
