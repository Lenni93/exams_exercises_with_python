from math import ceil
suger = 950
flour = 750
number_easter_cake = int(input())
total_sugar = 0
total_flour = 0
max_sugar_spend = 0
max_flour_spend = 0
for cake in range(number_easter_cake):
    sugar_cake = int(input())
    flour_cake = int(input())
    total_sugar += sugar_cake
    total_flour += flour_cake

    if sugar_cake > max_sugar_spend:
        max_sugar_spend = sugar_cake

    if flour_cake > max_flour_spend:
        max_flour_spend = flour_cake
cake_need_s = ceil(total_sugar / suger)
cake_need_f = ceil(total_flour / flour)

print(f"Sugar: {cake_need_s}")
print(f"Flour: {cake_need_f}")
print(f"Max used flour is {max_flour_spend} grams, max used sugar is {max_sugar_spend} grams.")
# max used sugar is {максимално количество грамове захар, използвани за правенето на козунак} grams.")
# •	"Sugar: {брой нужни пакети захар}"
# •	"Flour: {брой нужни пакет брашно}"
# •	"Max used flour is {максимално количество грамове брашно, използвани за правенето на козунак} grams,
# max used sugar is {максимално количество грамове захар, използвани за правенето на козунак} grams."