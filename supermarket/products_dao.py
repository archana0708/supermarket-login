

from sql_connection import get_sql_connection


def get_all_products(connection):

    cursor = connection.cursor()

    query = ("select products.productid, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id" )
    cursor.execute(query)

    response=[]
    for (productid,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({'product_id':productid,'product_name':name,'uom_id':uom_id,'price_per_unit':price_per_unit,'uom_name':uom_name})
    
    return response



def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where productid= %s ")
    data=product_id
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()


    #--------Insert------------------------------------

    # print(insert_new_product(connection, {
    #     'product_name': 'detergent',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    # }))


    #--------Delete------------------------------------
    # print(delete_product(connection, [12]))


    print(get_all_products(connection))


