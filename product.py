class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name:str = name
        self._price:float = price  # Protected
        self._quantity:int = quantity # Protected
        
    # Info - instancna metoda
    
    def product_info(self):
        return print(f" Product: {self.name}, Price: {self._price} $, Avaliable: {self._quantity} pcs ")
        
    ## Metode za azuriranje kolicina ##
    
    # instancne metode :
    
    # Getter za kolicine
    def get_quantity(self):
        return self._quantity
    
    # Setter za kolicine
    def set_quantity(self, new_quantity):
        if new_quantity < 0:
            return print("Kolicina memoze biti negativan broj!")
        else:
            self._quantity = new_quantity
            
    # dodavanje kolicina 
    def increase_quantity(self, value):
        if self._quantity + value > 100000:
            return print(" Kolicina prelazi dozvoljenu granicu od 100 000 jeinica !")
        else:
            self._quantity += value

    # smanjivanje kolicina
    def decrease_quantity(self, value):
        if self._quantity - value < 0:
            return print(" Kolicina bi bila negativan broj. Unesite manju vrednost!")
        else:
            self._quantity -= value  