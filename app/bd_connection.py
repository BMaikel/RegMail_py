import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("app/profs_emails.db", check_same_thread=False)
        self.cursor = self.connection.cursor()


    def registrar_correo(self, email, nombre, curso):
        sql = f"""INSERT INTO emails (correo, nombre, curso) VALUES("{email}", "{nombre}","{curso}");"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    def ver_correos(self):
        sql = f"""SELECT * FROM emails"""
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall() #Todos los registros

        except Exception as e:
            raise
    

    def buscar_correo(self, id):
        sql = f"""SELECT * FROM emails WHERE id='{id}';"""
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone() #Todos los registros

        except Exception as e:
            raise
    

    def actualizar_correo(self, id, email, nombre, curso):
        sql = f"""UPDATE emails SET correo ="{email}", nombre = "{nombre}", curso = "{curso}" WHERE id = {id}"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    def eliminar_correo(self, id):
        sql = f"""DELETE FROM emails WHERE id='{id}';"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    def close(self):
        self.connection.close() #Es necesario terminar la conección con la base de datos