print("Welcome to KFC Dhaka")

#Menu

Menu ={

    "Chicken Fried" : 300 ,
    "Frech Fries" : 149 ,
    "Chichen Popcorn" : 249 ,
    "Spicy Chicken": 399 ,
    "Ginger Burger" : 449 ,
    "Softy" : 89 ,
    "Cold Coffee" : 179,

}

while True:

   print("Available Menu")
   for item , price in Menu.items():
     print(f"{item} - {price} Taka" )

   order = input ("Enter Your Order(Select Only one Item) :")

   if order in Menu : 
     print(f"{order} Available ! Please Proceed The Payment. ")
     price = Menu.get(order)
     print(f"Your Total Bill {price} + 30.90 Taka Tax")
     print(f"{price+30.90} Taka")
     payment = input("Press Enter To make the payment")
     print("Payment Successful ! Please Collect Your order.")
   else:
     print(f"{order} not available.")