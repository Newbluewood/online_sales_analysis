class ProductManager:
    def __init__(self):
        self.avaliable_product_list = []
        
    # instancne metode:
    
    #dodavanje proizvoda u listu dostupnih proizvoda:
    def add_product_to_avaliable_product_list(self, product):
        self.avaliable_product_list.append(product)
        
    # ispis proizvoda u listi
    def show_avaliable_products(self):
        return print(f"\n - { [product.name for product in self.avaliable_product_list] } ")
    
    def total_of_products(self):
        total = sum(product._quantity * product._price for product in self.avaliable_product_list)
        return print(f" Total for all products in list : {total} $ ")
    
    # new function remove product fro list
    def remove_product_from_list(self, name):
        forremove = [product for product in self.avaliable_product_list if product.name == name]
        self.avaliable_product_list.remove(forremove[0])
        
    