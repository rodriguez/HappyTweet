from happy_tweet import get_user

if __name__ == '__main__':
    other_emotions = {}
    username_list = ["JMills21478", "Lynds_eey", "Duuuval", "Norphsidee", "beingmesince96", "april_aries17", "Moliblog",
                     "_stayygorgeous", "JulioCN93", "Hipcheck1967", "SirAWilliams80", "His_SmokingGun",
                     "elirosstheboss",
                     "ThiahArmani_", "MDCPS", "DannyEspinalHD", "ThiahArmani_", "ijump14", "_Whiitneey", "dominictw",
                     "yesimbby", ]
    # for username in username_list:
    #     user = get_user(username)
    #     tweets = user['tweets']
    #     emotions = [tweet['emotions'] for tweet in tweets]
    #     print(emotions)
    user = get_user(username_list[0])
    tweets = user['tweets']
    emotions = [tweet['emotions'] for tweet in tweets]
    print(emotions)
