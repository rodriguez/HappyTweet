from happy_tweet import User

if __name__ == '__main__':
    username = input("What's your name, user?")
    subject = User(username)
    list_of_others = {}
    username_list = ["JMills21478", "Lynds_eey", "Duuuval", "Norphsidee", "beingmesince96", "april_aries17", "Moliblog",
                     "_stayygorgeous", "JulioCN93", "Hipcheck1967", "SirAWilliams80", "His_SmokingGun",
                     "elirosstheboss",
                     "ThiahArmani_", "MDCPS", "DannyEspinalHD", "ThiahArmani_", "ijump14", "_Whiitneey", "dominictw",
                     "yesimbby", ]
    for x in username_list:
        a = User(x)
        list_of_others[x] = x["emotions"]


