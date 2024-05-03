country = input()
instrument = input()


if country == "Russia":
    if instrument == 'ribbon':
        hardest = 9.100
        performance = 9.400
    elif instrument == 'hoop':
        hardest = 9.300
        performance = 9.800
    elif instrument == 'rope':
        hardest = 9.600
        performance = 9.000

if country == "Bulgaria":
    if instrument == 'ribbon':
        hardest = 9.600
        performance = 9.400
    elif instrument == 'hoop':
        hardest = 9.550
        performance = 9.750
    elif instrument == 'rope':
        hardest = 9.500
        performance = 9.400

if country == "Italy":
    if instrument == 'ribbon':
        hardest = 9.200
        performance = 9.500
    elif instrument == 'hoop':
        hardest = 9.450
        performance = 9.350
    elif instrument == 'rope':
        hardest = 9.700
        performance = 9.150

percent = 20 - (hardest + performance)
print(f"The team of {country} get {hardest + performance:.3f} on {instrument}.")
print(f"{percent / 0.20:.2f}%")
# конзолата трябва да се отпечатат два реда:
# •	Първи ред: "The team of {държава} get {обща оценка} on {уред}."
# •	Втори ред:  "{процентът, който не им достига до максималния брой точки}%"
# first row  - country(Russia", "Bulgaria" или "Italy")
# second row - instrument ("ribbon", "hoop" или "rope")
