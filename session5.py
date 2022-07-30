from tabulate import tabulate
def main():
    def banner():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enter initiative")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    banner()

    def init():
        #Adventurers
        azar = eval(input("Azar Ember: "))
        nick = eval(input("Nick Gurr: "))
        ben = eval(input("Ben O'verbitch: "))
        #monsters
        lost_sorrow1 = eval(input("Lost Sorrow (Purple d12): "))
        lost_sorrow2 = eval(input("Lost Sorrow (Red d12): "))
        cloakers = eval(input("Howler (Black d8): "))
        cave_fisher1 = eval(input("Cave Fisher 1: "))
        cave_fisher2 = eval(input("Cave Fisher 2: "))
        

        def order():
            order = (azar, nick, ben, lost_sorrow1, lost_sorrow2, cloakers, cave_fisher1, cave_fisher2)
            order = sorted(order, reverse = True)
            print(tabulate([[order]]))
        order()
    init()
main()