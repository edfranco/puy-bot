import time
import products_db
from Stores import Stores 


# def find_stock():
#     bought = False
#     while bought is False:
#         for i in products_db.gpu_list:
#             time.sleep(1)
#             if i.price is not None and int(i.price) < i.max_price:
#                 print(test)
#                 test(i.url)
#                 print ("Found " + i.brand + " " + i.product_name + " on " + i.store + " in stock for " + str(i.price) )
#                 bought = True
#                 return
#             elif i.price is not None and int(i.price) > i.max_price:
#                 print ("Found " + i.brand + " " + i.product_name + " on " + i.store + " in stock for " + str(i.price) + " but is more than the max price of " + str(i.max_price) + " set for a " + i.product_name)
#             else:
#                 print ("Card:" + i.product_name + " Store:" + i.store + " Stock: " + 'Not in stock' )

def find_items(item_list):
    bought = False
    while (bought == False):
        for i in item_list:
            if i.store == 'Amazon':
                Stores.amazon_buy(i)
            elif i.store == 'Newegg':
                Stores.newegg_buy(i)
            elif i.store == 'Walmart':
                Stores.walmart_buy(i)
            elif i.store == 'Target':
                Stores.target_buy(i)
            elif i.store == 'Best Buy':
                Stores.best_buy(i)
            elif i.store == 'Gamestop':
                Stores.gamestop_buy(i)
            else:
                return print("Store: " + item_list.store + "not supported")


find_items(products_db.consoles_list)
