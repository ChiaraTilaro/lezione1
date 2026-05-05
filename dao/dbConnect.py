import mysql.connector


class DBConnect:

    @classmethod
    def getConnection(cls):

        try:
            cxn = mysql.connector.connect(
                user = "root",
                password = "passwordchiara",
                host = "127.0.0.1",
                database = "sw_gestionale")
            return cxn
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al db")
            print(err)
            return None
