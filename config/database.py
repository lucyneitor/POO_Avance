import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase que gestiona la conexión a la base de datos implementando 
    el patrón Singleton para evitar múltiples instancias innecesarias
    """
    _instance = None
    _db_path = "clinica.db"

    def __new__(cls): #cls clase en si
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls) #del padre llamamos pasamos la clase
        return cls._instance

    def get_connection(self) -> Connection: #conectarse y devolver la conexion y capacidad de consultar
        """
        Retorna una conexión a la base de datos SQLite
        """
        conn=sqlite3.connect(self._db_path)#path = ubicacion
        conn.row_factory = sqlite3.Row #Permite acceder a las columnas por nombre
        return conn

    def init_db(self) -> None:
        """
        Inicializa la base de datos creando las tablas necesarias
        """
        conn = self.get_connection() #inicializa
        try:
            cursor: Cursor = conn.cursor()

            #tabla Departamento (Integrer = entero)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamento (
                id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                piso INTEGER NOT NULL
            )
            """)

            #tabla paciente
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS paciente (
                rut TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                prevision TEXT NOT NULL,
                id_departamento INTEGER,
                FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento) ON DELETE SET NULL
            )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
        finally:#pasa independientemente si falla o no el programa
            conn.close() #cierra conexión

if __name__ == "__main__":
    db = Database()
    db.init_db()
    print("Base de datos inicializada correctamente.")

            

    