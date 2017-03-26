from happy_tweet import User

if __name__ == '__main__':
    username = input("What's your name, user?")
    subject = User(username)
    list_of_others = {}
    username_list = ['']
    for x in username_list:
        a = User(x)
        list_of_others[x] = x["emotions"]


