from math import ceil
suger = 950
flour = 750
number_easter_cake = int(input())
total_need_sugar = 0
total_need_flour = 0
max_sugar_spend = 0
max_flour_spend = 0
for cake in range(number_easter_cake):
    sugar_cake = int(input())
    flour_cake = int(input())
    total_need_sugar += sugar_cake
    total_need_flour += flour_cake

    if sugar_cake > max_sugar_spend:
        max_sugar_spend = sugar_cake

    if flour_cake > max_flour_spend:
        max_flour_spend = flour_cake
cake_s = ceil(total_need_sugar / suger)
cake_f = ceil(total_need_flour / flour)

print(f"Sugar: {cake_s}")
print(f"Flour: {cake_f}")
print(f"Max used flour is {max_flour_spend} grams, max used sugar is {max_sugar_spend} grams.")
# max used sugar is {максимално количество грамове захар, използвани за правенето на козунак} grams.")
# •	"Sugar: {брой нужни пакети захар}"
# •	"Flour: {брой нужни пакет брашно}"
# •	"Max used flour is {максимално количество грамове брашно, използвани за правенето на козунак} grams,
# max used sugar is {максимално количество грамове захар, използвани за правенето на козунак} grams."