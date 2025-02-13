from product_manager import ProductManager
from product import Product
from cart import Cart
# uvoz PY modula za sucajni izbor :
import random 

print("\nFaza 3.\n")
# kreiranje instance ProductManagera
ProductManager1 = ProductManager()

p1_laptop = Product("Laptop", 750, 20)
p2_TV = Product("TV Samsung 90''", 980, 15)

# hardkodovano dodavanje proizvoda u listu dostupnih proizvoda instance ProductManagera
ProductManager1.add_product_to_avaliable_product_list(p1_laptop)
ProductManager1.add_product_to_avaliable_product_list(p2_TV)
ProductManager1.add_product_to_avaliable_product_list(Product("Smartphone", 450, 50))
ProductManager1.add_product_to_avaliable_product_list(Product("Headphones", 75, 30))
ProductManager1.add_product_to_avaliable_product_list(Product("Camera", 600, 10))
ProductManager1.add_product_to_avaliable_product_list(Product("Tablet", 300, 25))
ProductManager1.add_product_to_avaliable_product_list(Product("Smartwatch", 150, 40))


# pozivanje metode product_info instance Product
p1_laptop.product_info()
p2_TV.product_info()

#pozivanje metoda show_avaliable_products i total_of_products instance ProductManager
ProductManager1.show_avaliable_products()
ProductManager1.total_of_products()

# pozivanje dodate metode remove_product_from_list instance ProductManager
print("\nFaza 4.\n")
print(" Izbacijemo proizvod 'Laptop' sa liste dostupnih proizvoda !")
ProductManager1.remove_product_from_list("Laptop")
ProductManager1.show_avaliable_products()

# testiranje dodate klase Cart i nenih metoda
print("\nFaza 6. \n")
cart1 = Cart()
# cart1.add_product_to_cart(p1_laptop, 1) # test 
# cart1.add_product_to_cart(p1_laptop, 3) # test ponovljeni proizvod

# random izbor za Cart
random_product_from_list = random.sample(ProductManager1.avaliable_product_list,3)
for add_item in random_product_from_list:
    cart1.add_product_to_cart(add_item, random.randint(1,10)) # dodavanje slucajno izabranog Produkta i slucajan izbor kolicine ( 1-10 )
    
cart1.show_product_in_cart()
cart1.total_of_products_in_cart()