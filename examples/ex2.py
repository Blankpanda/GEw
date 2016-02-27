import exchange.ItemList # the ItemList module is used to search for different IDs.

# if either return None, the ID or name was invalid
def main():

    item_name = exchange.ItemList.get_id("Guthan's warspear")
    item_id = exchange.ItemList.get_name(243)

    print(item_name) # 4726
    print(item_id) # Blue dragon scale


if __name__ == '__main__':
    main()
