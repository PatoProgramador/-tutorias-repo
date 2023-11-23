from config.connectdb import SqlConnector

dbConn = SqlConnector(hst="localhost", us="root", pas= "", db="tutorias")

dbConn.connector()