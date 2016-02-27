# GEw
GEw is a Old School Runesacpe Grand Exchange API wrapper.

---
How to Use
---

install the pip package:
    
    pip install gew


add this to the top of your program:

     import gew
    
---

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
    item = gew.exchange.Item(4151)
    
    print(item.price) # 2.4m
    print(item.name)  # "Abbysal Whip"
    print(item.SixMonth_trend) # "positive"
    print(item.SixMonth_change) # "+9.0%"

---
Additionally you can use the ItemList module to match item IDs to names.

     item_id = gew.ItemList.get_id("Bucket of wax") # 30
     item_name = gew.ItemList.get_name(30) # "Bucket of wax"
  
---
TODO
---
 
  

  

