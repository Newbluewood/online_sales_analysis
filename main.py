from product_manager import ProductManager
from product import Product

ProductManager1 = ProductManager()

p1_laptop = Product("Laptop", 350, 20)
p2_TV = Product("TV Samsung", 480, 15)

ProductManager1.add_product_to_avaliable_product_list(p1_laptop)
ProductManager1.add_product_to_avaliable_product_list(p2_TV)


p1_laptop.product_info()
p2_TV.product_info()

ProductManager1.show_avaliable_products()
ProductManager1.total_of_products()

print("2")
ProductManager1.remove_product_from_list("Laptop")
ProductManager1.show_avaliable_products()