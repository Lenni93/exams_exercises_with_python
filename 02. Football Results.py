result_first_match = input().split(":")
result_second_match = input().split(":")
result_third_match = input().split(":")

if result_first_match > 3:
    print("Team won 1 games")

elif result_first_match < 0:
    print("Team lost 1 games")

elif result_third_match == 0:
    print("Drawn games: 1")



# Team won 1 games.
# Team lost 1 games.
# Drawn games: 1
