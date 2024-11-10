# ✅↓ Write your code here ↓✅
def number_of_bottles():
    num = 99
    while num >= 0:
        if num == 2:
            print(f"{num} bottles of milk on the wall, {num} bottles of milk. Take one down and pass it around, {num-1} bottle of milk on the wall.")
        elif num == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        elif num == 0:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(f"{num} bottles of milk on the wall, {num} bottles of milk. Take one down and pass it around, {num-1} bottles of milk on the wall.")
        num-=1

number_of_bottles()