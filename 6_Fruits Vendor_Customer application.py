import sys
from termcolor import colored, cprint
from colored import fg, bg,attr
def main_menu():
    print("-----Main Menu-----")
    print("1.Create Fruits Stock")
    print("2.Edit fruits stock")
    print("3.Removing Unavailable fruits from Stock")
    print("4.Search fruits in the Stock")
    print("5.Good bye")
    
main_menu()

menu = dict()
#number = int(input("Choose from menu:"))
while (1):
    number = int(input("Choose number from main menu:"))
    print()
    if number==1:
        no_of_fruits = int(input("Please the Enter the Number of fruits to be available in stock:"))
        print()
        for i in range(no_of_fruits):
            choice=input("Enter fruit name followed by prices (please enter comma in between fruit name and price):")
            print("\n")
            fruit,prices = choice.split(',')
            menu[fruit] = [prices]
        print(f"Current Stock:\n{menu}\n")

    elif number ==2:
        fruit = input("Enter the fruit name:")
        prices = input("Enter the fruit prices:")
        menu[fruit] = [prices]
        print(f"Current Stock:\n{menu}\n")
        print()

    elif number==3:
        fruit = input("Please enter the fruit name that you want to remove from the stock:")
        menu.pop(fruit)
        print(f"Current Stock:\n{menu}\n")
        print()
    elif number ==4:
#def search(menu,fruit)
        #fruit = input("Enter the fruit name to see the availability in stock:")
        #def search(list,fruit):
            #for i in range(len(list)):
                #if list[i] == fruit:
                    #return True
            #return False
        fruit = input("Enter the fruit name to see the availability in stock:")
        print()
        if fruit in menu:
            #text = colored('Item is available in the stock','red')
            print('%s Item is available in the stock %s' % (fg(1), attr(0)))
            print("\n")
        else:
            print('%s Item is not available in the stock %s' % (fg(1), attr(0)))
            print()
    elif number ==5:
        print("Good Bye.... See you again\n")
        #quit
        break
    main_menu()

    
        
