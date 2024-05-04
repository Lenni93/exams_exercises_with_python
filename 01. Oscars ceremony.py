rent_hall = int(input())

statistics = rent_hall - (rent_hall * 0.30)
catering = statistics - (statistics * 0.15)
voicing = catering / 2
total = rent_hall + statistics + catering + voicing
print(f"{total:.2f}")




# Да се отпечата на конзолата колко ще са разходите по организирането на церемонията.
# Сумата да бъде форматирана до втория знак след десетичния знак.
# •	Статуетки  – цената им е 30% по-малка от наема на залата
# •	Кетъринг – цената му е 15% по-малка от тази на статуетките
# •	Озвучаване – цената му е 1 / 2 от цената за кетъринг