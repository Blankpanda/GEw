import exchange.GE # the GE module interfaces with the API

def main():
    item = exchange.GE.Item(30) # create and item object by inputing its ID
    print(item.name) # Bucket of wax

if __name__ == '__main__':
    main()
