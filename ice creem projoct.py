

print ("************************************")
print ("*      Welcome To Harilicius       *")
print ("************************************")

container = 0
flavour = 0
scoop = 0
toppings = 0

while (True):
    c = input ("\nCone .. Rs.10\nCup ... Rs.05\nEnter your Choich : ")
    c.lower ()
    
    if (c == "cone"):
        container = 10
        break
    elif (c == "cup"):
        container = 5
        break
    else :
        print ("\n\tEnter valid input !")
        continue
    
while (True):
    print ("\n1 Buttersctoch ... Rs.40\t\n2 Strawberry ..... Rs.35\t\n3 Chocolate ...... Rs.30\t\n4 Vanilla ........ Rs.25")
    f = input ("\nEnter your Flavour : ")

    if (f == "1"):
        flavour = 40
        break
    elif (f == "2"):
        flavour = 35
        break
    elif (f == "3"):
        flavour = 30
        break
    elif (f == "4"):
        flavour = 25
        break
    else :
        print ("\n\tEnter valid input !")
        continue

while (True):
    s = input ("\nEnter how many Scoop you want (1 to 4) : ")

    if (s == "1"):
        scoop = flavour * 1
        break
    elif (s == "2"):
        scoop = flavour * 2
        break
    elif (s == "3"):
        scoop = flavour * 3
        break
    elif (s == "4"):
        scoop = flavour * 4
        break
    else :
        print ("\n\tEnter valid input !")
        continue

while (True):
    print ("\n1 Hot Fudge \n2 Sprinkles\n3 Nuts\n4 No need")
    t = input ("\nEnter Toppings : ")

    if (t == "1" or t == "2" or t == "3"):
        toppings = 5
        break
    elif (t == "4"):
        toppings = 0
        break
    else :
        print ("\n\tEnter valid input !")
        continue
    
amount = container + scoop + toppings

print ("-"*13,"Bill","-"*14)
print (f"\nContiner ................. Rs.{container}")
print (f"Ice cream ...........{s}*{flavour}. Rs.{scoop}")
print (f"Topping .................. Rs.{toppings}")
print (f"\nTotal .................... Rs.{amount}\n")
print ("******THANKS FOR PURCHERSING*****")
print ("           Visit Again")
print ("*"*33)
