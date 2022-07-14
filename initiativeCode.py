def main():
    def banner():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enter adventurers initiative")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    banner()

    def init():
        #Adventurers
        azar = eval(input("Azar Ember: "))
        nick = eval(input("Nick Gurr: "))
        ben = eval(input("Ben O'verbitch: "))
        #monsters
        skeleton = eval(input("Skeletons: "))
        chitine = eval(input("Chitines: "))
        annis_hag1 = eval(input("Annis Hag 1 (red d8): "))
        annis_hag2 = eval(input("Annis Hag 2 (blue d8): "))
        boneclaw = eval(input("Boneclaw (green d12): "))
        necro_wizard = eval(input("Necromancer Wizard (blue d12): "))
        larvae_mage = eval(input("Larvae Mage (green d20): "))

        def order():
            order = (azar, nick, ben, skeleton, chitine, annis_hag1, annis_hag2, boneclaw, necro_wizard, larvae_mage)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            order = sorted(order, reverse = True)
            print(order, "         |")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        order()
    init()
main()