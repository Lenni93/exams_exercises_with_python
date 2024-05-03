import math

minute_manage = int(input())
second_manage = int(input())
length_of_meters = float(input())
second_reached_100_meters = int(input())

count_of_manage_of_second = (minute_manage * 60) + second_manage
count_how_many_times__increased_the_runner_time = length_of_meters / 120
total_increased_time = count_how_many_times__increased_the_runner_time * 2.5
time_of_the_runner = (length_of_meters / 100) * second_reached_100_meters - total_increased_time

if count_of_manage_of_second >= time_of_the_runner:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_of_the_runner:.3f}.")
else:
    need_time = abs(count_of_manage_of_second - time_of_the_runner)
    print(f"No, Marin failed! He was {need_time:.3f} second slower.")





# •	Ако времето на Марин е по-малко или равно на контролата:
# o	"Marin Bangiev won an Olympic quota!"
# o	"His time is {времето на Марин в секунди}."
# •	Ако времето на Марин е повече от това на контролата:
# o	 "No, Marin failed! He was {недостигащи секунди} second slower."
# Резултатът трябва да е форматиран до третия знак след десетичния знак.




# Ред 1.	Минути на контролата – цяло число в интервала [0…59]
# Ред 2.	Секунди на контролата – цяло число в интервала [0…59]
# Ред 3.	Дължината на улея в метри – реално число в интервала [0.00…50000]
# Ред 4.	Секунди за изминаване на 100 метра – цяло число в интервала [0…1000]


# контролата в минути,
# разстоянието на улея в метри за което той изминава 100 метра.
# и времето в секунди