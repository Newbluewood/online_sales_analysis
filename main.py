from product_manager import ProductManager
from product import Product
from cart import Cart

print("\nFaza 3.\n")
# kreiranje instance ProductManagera
ProductManager1 = ProductManager()

# hardkodovano kreiranje proizvoda:
p1_laptop = Product("Laptop", 350, 20)
p2_TV = Product("TV Samsung", 480, 15)

# hardkodovano dodavanje proizvoda u listu dostupnih proizvoda instance ProductManagera
ProductManager1.add_product_to_avaliable_product_list(p1_laptop)
ProductManager1.add_product_to_avaliable_product_list(p2_TV)

# pozivanje metode product_info instance Product
p1_laptop.product_info()
p2_TV.product_info()

#pozivanje metoda show_avaliable_products i total_of_products instance ProductManager
ProductManager1.show_avaliable_products()
ProductManager1.total_of_products()

# pozivanje dodate metode remove_product_from_list instance ProductManager
print("\nFaza 4.\n")
ProductManager1.remove_product_from_list("Laptop")
ProductManager1.show_avaliable_products()

# testiranje dodate klase Cart i nenih metoda
print("\nFaza 6. \n")
cart1 = Cart()
cart1.add_product_to_cart(p1_laptop, 1)
cart1.add_product_to_cart(p1_laptop, 3)
cart1.show_product_in_cart()
cart1.total_of_products_in_cart()