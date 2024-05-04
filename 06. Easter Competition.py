number_of_bakers = int(input())

winner_name = ""
winner_point = 0
# interate the number of bakers and getting the name and assign the point
for amount in range(number_of_bakers):
    chef_name = input()
    point = 0

    while True:
        command = input()

        if command == "Stop":
            break

        point += int(command)
    # read the command and convert in integer till receiving stop
    print(f"{chef_name} has {point} points.")
    # checking weather baker has bigger point from rest of the participants
    if point > winner_point:
        winner_name = chef_name
        winner_point = point
        print(f"{chef_name} is the new number 1!")

print(f"{winner_name} won competition with {winner_point} points!")







# Initially, the console reads the number of Ester Cake  - an integer in the interval [1… 100]
# Then read for each Ester Cake:
# •name of the baker who bake the Ester cake
# Till received stop continue read it
# o	point for the Ester cake   – integer of interval  [1... 10]