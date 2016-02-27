import gew.ItemList # the ItemList module is used to search for different IDs.

# if either return None, the ID or name was invalid
def main():

    item_name = gew.ItemList.get_id("Guthan's warspear")
    item_id = gew.ItemList.get_name(243)

    print(item_name) # 4726
    print(item_id) # Blue dragon scale


if __name__ == '__main__':
    main()
