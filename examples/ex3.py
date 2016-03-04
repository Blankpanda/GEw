import gew.exchange
import gew.ItemList

def main():
    item = gew.exchange.Item(30)
    print(item.name)

    new_id = gew.ItemList.get_id('Dragon bones')
    item.get_new_item(new_id)

    print(item.name)



if __name__ == "__main__":
    main()
