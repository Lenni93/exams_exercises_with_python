annual_tax_per_year = int(input())

basketball_sneakers = annual_tax_per_year - (annual_tax_per_year * 0.4)
basketball_equipment = basketball_sneakers - (basketball_sneakers * 0.2)
basketball_ball = basketball_equipment / 4
basketball_accessories = basketball_ball / 5
total_price = (annual_tax_per_year + basketball_sneakers+ basketball_equipment + basketball_ball + basketball_accessories)
print(f"{total_price:.2f}")
