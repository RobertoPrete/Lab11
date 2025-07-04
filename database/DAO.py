from database.DB_connect import DBConnect
from model.arco import Arco
from model.product import Product


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

    @staticmethod
    def getAllProducts():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select *
                    from go_products gp """
        cursor.execute(query)
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(color):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select *
                    from go_products gp 
                    where gp.Product_color = %s """
        cursor.execute(query, (color, ))
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(color, year, idMapProducts):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select t1.Retailer_code, t1.Product_number as p1, t2.Product_number as p2, t1.`Date`
                    from  (select gds.*
		                    from go_daily_sales gds, go_retailers gr, go_products gp 
		                    where gds.Retailer_code = gr.Retailer_code and gds.Product_number = gp.Product_number
		                    and gp.Product_color = %s
		                    and YEAR(`Date` ) = %s
		                    order by gds.Retailer_code, gds.Product_number) as t1
                    left join (select gds.*
			                    from go_daily_sales gds, go_retailers gr, go_products gp 
			                    where gds.Retailer_code = gr.Retailer_code and gds.Product_number = gp.Product_number
			                    and gp.Product_color = %s
			                    and YEAR(`Date` ) = %s
			                    order by gds.Retailer_code, gds.Product_number) as t2
                    on t1.Retailer_code=t2.Retailer_code and t1.`Date`=t2.`Date`
                    where  t1.Product_number<t2.Product_number  or t2.Product_number  is null
                    group by t1.Retailer_code, t1.Product_number,t2.Product_number, t1.`Date`
                    order by t1.Retailer_code, t1.Product_number, t1.`Date`, t2.Retailer_code, t2.Product_number"""
        cursor.execute(query, (color, year, color, year, ))
        for row in cursor:
            result.append(Arco(row["Retailer_code"], idMapProducts[row["p1"]], idMapProducts[row["p2"]], row["Date"]))
        cursor.close()
        conn.close()
        return result

if __name__ == "__main__":
    print(DAO.getColors())
    print(DAO.getYears())
