import math

price_of_tennis_racket = float(input())
amount_of_tennis_racket = int(input())
num_of_a_pair_of_sneakers = int(input())

count_price_racket = price_of_tennis_racket * amount_of_tennis_racket
count_of_sneakers = (price_of_tennis_racket / 6)
price_all_sneakers = count_of_sneakers * num_of_a_pair_of_sneakers
price_for_all_equipment = (count_price_racket + price_all_sneakers) * 0.2
total_price = count_price_racket + price_all_sneakers + price_for_all_equipment

print(f"Price to be paid by Djokovic {math.floor(total_price / 8)}")
print(f"Price to be paid by sponsors {(math.ceil(total_price * 7 / 8))}")

# •	"Price to be paid by Djokovic {1/8 от общата цена, закръглена към по-малкото цяло число}"
# •	"Price to be paid by sponsors {7/8 от общата цена, закръглена към по-голямото цяло число}"

