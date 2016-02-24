import exchange


def main():
    test = exchange.Exchange(4151)
    print(test.id)
    print(test.name)
    print(test.price)
    print(test.description)

main()
