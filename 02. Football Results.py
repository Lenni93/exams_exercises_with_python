result_first_match = input()
result_second_match = input()
result_third_match = input()
# initialize counter for won, lost and drawn
won = 0
lost = 0
drawn = 0

# check for the first match
if int(result_first_match[0]) > int(result_first_match[2]):
    won += 1

elif int(result_first_match[0]) < int(result_first_match[2]):
    lost += 1

else:
    drawn += 1

# check for the second match
if int(result_second_match[0]) > int(result_second_match[2]):
    won += 1

elif int(result_second_match[0]) < int(result_second_match[2]):
    lost += 1

else:
    drawn += 1

# check for the third match
if int(result_third_match[0]) > int(result_third_match[2]):
    won += 1

elif int(result_third_match[0]) < int(result_third_match[2]):
    lost += 1

else:
    drawn += 1
# result
print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
# •	"Team won {брой спечелени мачове} games."
# •	"Team lost {брой загубени мачове} games."
# •	" Drawn games: {брой равни мачове}"

# Team won 1 games.
# Team lost 1 games.
# Drawn games: 1
