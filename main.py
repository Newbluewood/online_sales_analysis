from product_manager import ProductManager
from product import Product

ProductManager1 = ProductManager()

p1_laptop = Product("Laptop", 750, 20)
p2_TV = Product("TV Samsung 90''", 980, 15)

ProductManager1.add_product_to_avaliable_product_list(p1_laptop)
ProductManager1.add_product_to_avaliable_product_list(p2_TV)
