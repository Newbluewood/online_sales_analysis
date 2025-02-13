class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_product_to_cart(self, product, quantity):
        if len(self.cart_items) > 0: # ispitivnje dali je korpa prazna i da li vec sadrzi proizvod koji dodajemo
            for item in self.cart_items:
                if item["product"].name == product.name:
                    if item.quantity < quantity:
                        print(" Zao mi je, nemamo toliko na stanju !") # ako kolicina prelazi lager
                        break
                    else:
                        item["quantity"] += quantity # ako sadrzi, samo korigujemo kolicinu
                        item.quantity - quantity
                        break
            else:
                self.cart_items.append({"product":product, "quantity":quantity})
        else:
            self.cart_items.append({"product":product, "quantity":quantity})
        
    def total_of_products_in_cart(self):
        total = sum(item["product"]._price * item["quantity"] for item in self.cart_items)
        return print(f" Total for all products in cart : {total} $ ")
    
    def show_product_in_cart(self):
        for item in self.cart_items:
            print(f"- Item: {item["product"].name}, price: {item["product"]._price} $, quantity: {item["quantity"]}")
        