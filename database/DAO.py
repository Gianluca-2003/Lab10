from database.DB_connect import DBConnect
from model.Country import Country


class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getAllNodes(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query = """select DISTINCT c.StateAbb, c.CCode, c.StateNme
                from country c, contiguity c2 
                where (c.CCode = c2.state1no or c.CCode = c2.state2no) 
                       and c2.`year` <= %s 
                order by c.StateNme"""


        cursor.execute(query,(year,))

        for row in cursor:
            res.append(Country(**row))

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getAllEdges(idMap,year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query = """SELECT DISTINCT 
               LEAST(c.state1no, c.state2no) AS stateA, 
               GREATEST(c.state1no, c.state2no) AS stateB
        FROM contiguity c
        WHERE c.`year` <= %s AND c.conttype = 1;"""


        cursor.execute(query,(year,))

        for row in cursor:
            if row['stateA'] in idMap and row['stateB'] in idMap:
                res.append((idMap[row['stateA']],idMap[row['stateB']]))

        cursor.close()
        cnx.close()
        return res




