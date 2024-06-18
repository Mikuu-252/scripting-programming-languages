product_list = {}

def create_product(id:int, name:str, price:float, quantity:int):
    if id in product_list:
        print("Error: Produkt znajduje sie w magazynie")
        return
    
    product_list[id] = {
        'name': name,
        'price': price,
        'quantity': quantity
    }

def read_products():
    print(product_list)

def read_product(id):
    try:
        print(product_list[id])
    except KeyError:
        print('Error: Produkt nie istnieje w bazie')

def delete_product(id):
    try:
        product_list.pop(id)
    except KeyError:
        print('Error: Produkt nie istnieje w bazie')

def update_product(id, new_quantity):
    try:
        product_list[id].update({'quantity':new_quantity})
    except KeyError:
        print('Error: Produkt nie istnieje w bazie')

def sell_product(id, number):
    try:
        if product_list[id]['quantity'] < number:
            raise

    except KeyError:
        print('Error: Produkt nie istnieje w bazie')

def import_products(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                create_product(line, next(file), next(file))
    except FileNotFoundError:
            print(f"Plik {filename} nie istnieje")

def export_products(filename):
    try:
        with open(filename, 'w+', encoding='utf-8') as file:
            for i in range(1, len(product_list)+1):
                file.write(str(product_list[i]['name']) + '\n')
                file.write(str(product_list[i]['price']) + '\n')
                file.write(str(product_list[i]['quantity']) + '\n')
    except FileNotFoundError:
            print(f"Plik {filename} nie istnieje")

# create_product(1, 'Laptop', 2500.0, 10)
# create_product(2, 'Smartphone', 1200.0, 20)
# create_product(3, 'Tablet', 800.0, 15)

# export_products('magazyn_produkty.txt')

import_products('magazyn_produkty.txt')
read_products()


