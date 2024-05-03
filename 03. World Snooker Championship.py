stage_of_championship = input()
type_of_ticket = input()
count_ticket = int(input())
picture = input()
tax_picture = 40
# •	Над 4000 лири има 25% отстъпка и безплатни снимки с трофея (ако  опцията за снимки е избрана,
# таксата от 40 лири за билет не се включва)
# •	Над 2500 лири има 10% отстъпка
if stage_of_championship == 'Quarter final':
    if type_of_ticket == "Standard":
        ticket_price = 55.50
    elif type_of_ticket == "Premium":
        ticket_price = 105.20
    elif type_of_ticket == 'VIP':
        ticket_price = 118.90


if stage_of_championship == 'Semi final':
    if type_of_ticket == "Standard":
        ticket_price = 75.88
    elif type_of_ticket == "Premium":
        ticket_price = 125.22
    elif type_of_ticket == 'VIP':
        ticket_price = 300.40

if stage_of_championship == 'Final':
    if type_of_ticket == "Standard":
        ticket_price = 110.10
    elif type_of_ticket == "Premium":
        ticket_price = 160.66
    elif type_of_ticket == 'VIP':
        ticket_price = 400

price_of_all_ticket = ticket_price * count_ticket
if price_of_all_ticket > 4000:
    price_of_all_ticket -= price_of_all_ticket * 0.25
elif price_of_all_ticket >= 2500:
    price_of_all_ticket -= price_of_all_ticket * 0.10
elif price_of_all_ticket < 2500:
    price_of_all_ticket = price_of_all_ticket
elif picture == "Y":
    total_price = count_ticket * tax_picture
    price_of_all_ticket += total_price
print(f"{price_of_all_ticket:.2f}")
