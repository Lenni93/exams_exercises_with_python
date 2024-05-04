number_easter_cake = float(input())
eggs_shells = float(input())
weight_cookies = float(input())
easter_cake = 3.20
eggs = 4.35
cookies = 5.40
paint_for_eggs = 0.15

total_easter_cake = number_easter_cake * easter_cake
total_eggs = eggs_shells * eggs
total_cookies = cookies * weight_cookies
for_paint_eggs = eggs_shells * 12 * paint_for_eggs
total_consume = total_easter_cake + total_eggs + total_cookies + for_paint_eggs
print(f"{total_consume:.2f}")


# •	Брой козунаци - цяло число в интервала [0 … 99]
# •	Брой кори с яйца - цяло число в интервала [0 … 99]
# •	Килограми курабии - цяло число в интервала [0 … 99]
# •	Козунак  – 3.20 лв.
# •	Яйца –  4.35 лв. за кора с 12 яйца
# •	Курабии – 5.40 лв. за килограм
# •	Боя за яйца - 0.15 лв. за яйце