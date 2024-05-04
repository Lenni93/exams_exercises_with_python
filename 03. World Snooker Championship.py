stage_of_championship = input()
type_of_ticket = input()
count_ticket = int(input())
picture = input()
tax_picture = 40
# •	Над 4000 лири има 25% отстъпка и безплатни снимки с трофея (ако  опцията за снимки е избрана,
# таксата от 40 лири за билет не се включва)
# •	Над 2500 лири има 10% отстъпка
price = {"Quarter final": {"Standard": 55.5, "Premium": 105.2, "VIP": 118.9},
         "Semi final": {"Standard": 75.88, "Premium": 125.22, "VIP": 300.4},
         "Final": {"Standard": 110.1, "Premium": 160.66, "VIP": 400}}

price = price[stage_of_championship][type_of_ticket] * count_ticket
if price > 4000:
    price *= 0.75
elif price > 2500:
    price *= 0.9
    if picture == 'Y':
        price += tax_picture * count_ticket
else:
    if picture == 'Y':
        price += tax_picture * count_ticket
print(f"{price:.2f}")
