# GE_wrapper
GE_wrapper is a Old School Runesacpe Grand Exchange API wrapper.

---
How to Use
---

clone the repository:
    
    git clone https://github.com/Blankpanda/GE_wrapper.git

add this to the top of your program:
    
    import exchange
    
(be sure to add items.json to a resource folder)
create an Exchange object:
   
    item = exchange.Exchange(<ITEM_ID>)
(item IDS can be found in res/items.json)

the following generic properties will be retrieved from the api:
  1. icon
  2. icon_large
  3. id
  4. type
  5. typeIcon
  6. name
  7. description
  8. members
  9. price
  
properties about marketing trends:
  
  * **today**
    1. today_trend
    2. today_price
  * **current**
    1. current_trend
    2. current_price
  * **three months ago**
    1. ThreeMonths_trend
    2. ThreeMonths_change
  * **six months ago**
    1. SixMonth_trend
    2. SixMonth_change
  
---
Example
---
    item = Exchange.exchange(4151)
    
    print(item.price) # 2.4m
    print(item.name)  # "Abbysal Whip"
    print(item.SixMonth_trend) # "positive"
    print(item.SixMonth_change) # "+9.0%"
    

---
TODO
---
  * fix Items.py so that its able to retrieve IDS from inputing a name from names.json to make it easier to match item ids to names
  

  

