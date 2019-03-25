from account import Account

if __name__ == "__main__":
    acc = Account(100)

    acc.pay(200)
    print(acc.show_balance())
    acc.take(301)
    print(acc)
    acc.take(300)
    print(acc)
