name_movie = input()
type_hall = input()
amount_of_bought_ticket = int(input())
price = 0
# A Star Is Born	7.50 лв.	10.50 лв.	13.50 лв.
if name_movie == "A Star Is Born":
    if type_hall == "normal":
        price = 7.50
    elif type_hall == "luxury":
        price = 10.50
    elif type_hall == "ultra luxury":
        price = 13.50

# Bohemian Rhapsody	7.35 лв.	9.45 лв.	12.75 лв.
elif name_movie == "Bohemian Rhapsody":
    if type_hall == "normal":
        price = 7.35
    elif type_hall == "luxury":
        price = 9.45
    elif type_hall == "ultra luxury":
        price = 12.75

# # Green Book	8.15 лв.	10.25 лв.	13.25 лв.
elif name_movie == "Green Book":
    if type_hall == "normal":
        price = 8.15
    elif type_hall == "luxury":
        price = 10.25
    elif type_hall == "ultra luxury":
        price = 13.25

# The Favourite	8.75 лв.	11.55 лв.	13.95 лв.
elif name_movie == "The Favourite":
    if type_hall == "normal":
        price = 8.75
    elif type_hall == "luxury":
        price = 11.55
    elif type_hall == "ultra luxury":
        price = 13.95

total_price = amount_of_bought_ticket * price
print(f"{name_movie} -> {total_price:.2f} lv.")






# На конзолата трябва да се отпечата един ред:
# "{име на филма} -> {приходи от прожекцията на филма} lv."
# Приходите да бъдат закръглени до втория знак след десетичната запетая.




# •	Първи ред – име на филм – текст ("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite")
# •	Втори ред– вид на залата – текст ("normal", "luxury" или "ultra luxury")
# •	Трети ред – брой на закупените билети – цяло число в интервала [1…100]