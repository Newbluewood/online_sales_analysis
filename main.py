from product_manager import ProductManager
from product import Product

Manager1 = ProductManager()

p1_laptop = Product("Laptop", 350, 20)
p2_TV = Product("TV Samsung", 480, 15)

Manager1.add_product_to_avaliable_product_list(p1_laptop)
Manager1.add_product_to_avaliable_product_list(p2_TV)


p1_laptop.product_info()
p2_TV.product_info()

Manager1.show_avaliable_products()
Manager1.total_of_products()