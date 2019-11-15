

def getCommand():
    command = input("Enter command: ")
    return command


def addToInventory(dict):
    invname = input("Enter name of item to add to inventory: ")
    qty = int(input("Enter quantity of item to add: "))

    dict[invname] = dict.get(invname, 0) + qty


def viewInventory(dict):
    print("%9s -- %s" % ("Item", "Qty"))
    for (k, v) in dict.items():
        print("%9s -- %d" % (k, v))

def removeInventory(dict):
    invname = input("Enter name of item to remove from inventory: ")
    qty = int(input("Enter quantity of item to remove: "))

    if invname in dict:
        #dict[invname]=dict[invname].remove(dict[invname][qty])
        dict[invname] -= qty
        if dict[invname] < 0:
            print("Not enough stock")
        elif dict[invname] == 0:
            print("Order filled, restock needed")
            del dict[invname]
        else:
            print(dict[invname])
    else:
        print("This item not in stock")



def main():

    print("Welcome to StuffMaster, v.0.47")

    inventory = {}  # empty dictionary

    while True:  # get command, process command; quit when selected below

        print("Commands are: ")
        print("'A' => Add to inventory")
        print("'V' => View existing inventory")
        print("'R' => Remove from inventory")
        print("'Q' => Quit after showing final inventory")

        # Get the command

        cmd = getCommand().upper()[0]

        # Call the appropriate function based on command

        if cmd is 'A':
            addToInventory(inventory)
        elif cmd is 'V':
            viewInventory(inventory)
        elif cmd is 'R':
            removeInventory(inventory)
        elif cmd is 'Q':
            break
        else:
            print("Unknown command: %s => try again." % cmd)

        # If unknown command, complain and prompt for reentry

    # here, we're quitting

    print("Quitting. Final version of inventory is:")

    # print out final version of inventory

    viewInventory(inventory)

    print("Exiting...")


main()
