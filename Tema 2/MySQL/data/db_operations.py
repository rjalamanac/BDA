import mysql.connector
from model.partido import Partido

class Database:
    def __init__(self, host, user, password, database,port):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Partido (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name NVARCHAR(255),
            estadio NVARCHAR(255),
            golesVisitante INT,
            golesLocal INT,
            fechaInicioPartido datetime,
            fechaFinalPartido datetime        
        )
        """    
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self, partido):
        insert_query = "INSERT INTO Partido (name, estadio,golesVisitante,golesLocal,fechaInicioPartido,fechaFinalPartido) VALUES (%s,%s,%s, %s, %s,%s)"
        data = (partido.name, partido.estadio,partido.golesVisitante, partido.golesLocal,partido.fechaInicioPartido,partido.fechaFinalPartido)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        return (partido.name, partido.estadio, partido.golesVisitante, self.cursor.lastrowid)

    def get_all_data(self):
        select_all_query = "SELECT * FROM Partido"
        self.cursor.execute(select_all_query)
        result = self.cursor.fetchall()
        partidos = []
        for row in result:
            partido = (row[1], row[2], row[3], row[0])  
            partidos.append(partido)
        return partidos

    def update_data(self, partido):
        update_query = "UPDATE Partido SET name=%s WHERE id=%s"
        data = (partido[1],partido[0])
        self.cursor.execute(update_query, data)
        self.connection.commit()

    def delete_data(self, employee_id):
        delete_query = "DELETE FROM Partido WHERE id=%s"
        data = (employee_id,)
        self.cursor.execute(delete_query, data)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
