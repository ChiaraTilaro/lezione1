import pathlib

import mysql.connector


class DBConnect:
    def __init__(self):
        # per implementare il pattern singleton ed impedire al chiamante di creare l'istanza di classe
        raise RuntimeError("Attenzione, non devi creare un'istanza di questa classe, usa i metodi di classe")

    _myPool = None
    @classmethod
    def getConnection(cls):
        if cls._myPool is None:

            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                   user = "root",
                   password = "passwordchiara",
                   host = "127.0.0.1",
                   database = "sw_gestionale",
                   pool_size= 3,
                   pool_name="myPool")
                #option_files = f"{pathlib.Path().resolve(__file__).parent}/connector.cfg" )
                return cls._myPool.get_connection()
            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            return cls._myPool.get_connection()
