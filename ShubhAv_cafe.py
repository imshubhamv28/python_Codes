## My First project is Cafe Menu.
Menu = {
    "Cold_Coffie" : 90,
    "Pasta" : 70,
    "Tea" : 30,
    "Sendwich" : 80,
    "Burger" : 70,
    "Patis" : 50,
    "Pizza" : 125
}
print(Menu)

#Greetings
print("Wellcome to *SHUBHAV* Cafe")
print("Menu\n1.Cold_Coffie : Rs.90\n2.Pasta : Rs.70\n3.Sendwich : Rs.80\n4.Burger : Rs.70\n5.Patis : Rs.50\n6.Pizza : Rs.125")

Order_Total = 0

Item1 = input("Enter the name of item you want to Order :")
if Item1 in Menu:
    Order_Total += Menu[Item1]
    print("Your Fabourite item",Item1,"has been added to your Order")

else: 
    print("Ordered item",Item1,"is not available yet")
print("The total Amount of item is Rs.",Order_Total,"you need to pay")

Another_Order = input("Do you want to add Another Item ?  (Yes/No) :")
if Another_Order == "Yes" :
    Item2 = input("Enter the name of second item :")
    if Item2 in Menu :
        Order_Total += Menu[Item2]
        print("Your Fabourite item",Item2,"has been added to your Order")
    else : 
        print("Ordered item",Item2,"is not available yet")
else :
    print("Thanks for visiting *ShubhAv* Cafe\nPlease visit Again.")

print("The total Amount of item is Rs.",Order_Total,"you need to pay")

Another_Order = input("Do you want to add Another Item ?  (Yes/No) :")
if Another_Order == "Yes" :
    Item3 = input("Enter the name of second item :").strip()
    if Item3 in Menu :
        Order_Total += Menu[Item3]
        print("Your Fabourite item",Item3,"has been added to your Order")
    else : 
        print("Ordered item",Item3,"is not available yet")
else :
    print("Thanks for visiting *ShubhAv* Cafe\nPlease visit Again.")

print("The total Amount of item is Rs.",Order_Total,"you need to pay")

Another_Order = input("Do you want to add Another Item ?  (Yes/No) :").strip()
if Another_Order == "Yes" :
    Item4 = input("Enter the name of item :").strip()
    if Item4 in Menu :
        Order_Total += Menu[Item4]
        print("Your Fabourite item",Item4,"has been added to your Order")
    else : 
        print("Ordered item",Item4,"is not available yet")
else :
    print("Thanks for visiting *ShubhAv* Cafe\nPlease visit Again.")

print("The total Amount of item is Rs.",Order_Total,"you need to pay")

Another_Order = input("Do you want to add Another Item ?  (Yes/No) :")
if Another_Order == "Yes" :
    Item5 = input("Enter the name of item :").strip()
    if Item5 in Menu :
        Order_Total += Menu[Item5]
        print("Your Fabourite item",Item5,"has been added to your Order")
    else : 
        print("Ordered item",Item5,"is not available yet")
else :
    print("Thanks for visiting *ShubhAv* Cafe\nPlease visit Again.")

print("The total Amount of item is Rs.",Order_Total,"you need to pay")