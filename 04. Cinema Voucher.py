voucher_price = int(input())
tickets_count = 0
other_purchase = 0
command = input()
while command != 'End':

    if len(command) > 8:
        voucher_price -= ord(command[0]) + ord(command[1])
        if voucher_price < 0:
            break

        tickets_count += 1
    else:
        voucher_price -= ord(command[0])

        if voucher_price < 0:
            break

        other_purchase += 1

    command = input()

print(f"{tickets_count}")
print(f"{other_purchase}")

# •	"{брои закупени билети}"
# •	"{брой закупени други покупки}"
# Ако името на покупката съдържа повече от 8 символа, то тя е билет за филм, а нейната цена представлява сумата на
# ASCII символите от първите ѝ два символа. Ако името на покупката съдържа 8 или по-малко символа, нейната цена е
# равна на стойността на първия ASCII символ в името. Любо въвежда името на покупките,
# които желае, докато не въведе "End" или не въведе покупка, чиято стойност е по-голяма от останалата сума на ваучера.
