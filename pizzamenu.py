#nom-prix-ingredients-végétarienne

class Pizza:
    def __init__(self,nom,prix,ingredients,vegetarienne=False) :
        self.nom=nom
        self.prix=prix
        self.ingredients=ingredients
        self.vegetarienne=vegetarienne
        
    
    def display(self):
        info_optionnel=""
        
        info_de_base=f"Pizza :   {self.nom} : {self.prix} €"

        if self.vegetarienne:
            info_optionnel=" - Végétarienne"
            print(info_de_base+info_optionnel)
        else:
            print(info_de_base)
        

        print(f"ingrédients: ",", ".join(self.ingredients))
        print("")

class PizzaPersonnalisa(Pizza):
    PRIX_DE_BASE=9
    PRIX_INGREDIENT=1.2
    DERNIER_NUM=0

    def __init__(self ):
        PizzaPersonnalisa.DERNIER_NUM+=1
        self.numero=PizzaPersonnalisa.DERNIER_NUM
        super().__init__("Personnalisé "+str(self.numero),0, [])
        self.ask_ingredients()
        self.pricePersonnalisa()
        
    
    def ask_ingredients(self):
        print()
        print(f"Ingrédient pour la pizza Personnalisé {self.numero}")
        while True:
            ingredient=input(f"Ajoutez un ingrédient pour la pizza personnalisé  ( ou ENTER sans rien écrire pour terminer) : ")
            if ingredient=="":
                self.numero+=1
                return
            
            self.ingredients.append(ingredient)
            
            print(f"Vous avez {len(self.ingredients)} ingrédient(s): {', '.join(self.ingredients)}")
    def pricePersonnalisa(self):
       self.prix=self.PRIX_DE_BASE+(len(self.ingredients)*self.PRIX_INGREDIENT)
      
            



pizzas=[
        Pizza("4 Fromages",12.5, ("Base crème","gorgonzola","mozzarella","chèvre","brie")),
        Pizza("Margherita",9,("Base tomate","mozzarella","basilic")),
        Pizza("Paysanne",14,("Base crème","roblochon","patate","lardon","ognion")),
        Pizza("Raclette",14,("Base crème","raclette","patate","lardon","ognion","salade")),
        Pizza("4 saison",9.5,("Base tomate","aubergine","ognion","mozzarella","artichaut"),True),
        Pizza("Regina",13,("Base tomate","champignon","jambon","mozzarella","olive")),
        Pizza("Neptune",12,("Base tomate","thon","capre","mozzarella")),
        Pizza("Hawai",9.5,("Base tomate","ananas","ognion","mozzarella"),True),
        PizzaPersonnalisa(),
        PizzaPersonnalisa()
]

for pizza in pizzas:
   pizza.display()
"""
print()
print()
print("---Pizza Végétarienne---")
print()
print()
#exo tierce 1
#afficher seulement les pizza végétarienne


for pizza in pizzas:
    if pizza.vegetarienne:
        pizza.display()
 
 #afficher seulement les pizza non_végétarienne
print()
print()
print("---Pizza non-végétarienne---")
print()
print()

 
for pizza in pizzas:
    if not pizza.vegetarienne:
        pizza.display()

print()
print()
print()
print("---Pizza Avec de la tomate---")
print()
print()

for pizza in pizzas:
    if  "tomate" in pizza.ingredients:
        pizza.display()

print()
print()
print("---Pizza à moins de 10€---")
print()
print()

for pizza in pizzas:
    if  pizza.prix<10:
        pizza.display()

print()
print()
print("---Pizza trier par ordre Alphabétique---")
print()
print()

def tri(e):
    return e.nom

pizzas.sort(key=tri)

for pizza in pizzas:
    pizza.display()

print()
print()
print("---Pizza trier par prix---")
print()
print()

def price(e):
    return e.prix

pizzas.sort(key=price)

for pizza in pizzas:
    pizza.display()
"""