from database.DB_connect import DBConnect


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getColors():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select distinct Product_color 
                    from go_products gp 
                    order by Product_color """
        cursor.execute(query)
        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select distinct YEAR(`Date` ) as year
                    from go_daily_sales gds 
                    order by YEAR(`Date`)"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["year"])
        cursor.close()
        conn.close()
        return result

if __name__ == "__main__":
    print (DAO.getColors())
    print (DAO.getYears())
