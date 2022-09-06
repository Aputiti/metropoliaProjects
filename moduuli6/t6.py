import math

# diameter = pi*radius^2
# 1 cm^2 = 0,0001 m^2

pizza1Diam = float(input("Pizza-1 diameter (cm): "))
pizza1Price = float(input("Pizza-1 price (eur): "))
pizza2Diam = float(input("Pizza-2 diameter (cm): "))
pizza2Price = float(input("Pizza-2 price (eur): "))


def pizza_area_price(pizza_diam, pizza_price):
    pizza_area_m2 = (math.pi * (pizza_diam / 2) ** 2) / 10000
    pizza_area_eur = pizza_price / pizza_area_m2
    return pizza_area_eur


print(f"\nPizza-1 price (eur/m2): {pizza_area_price(pizza1Diam, pizza1Price):6.2f}" +
      f"\nPizza-2 price (eur/m2): {pizza_area_price(pizza2Diam, pizza2Price):6.2f}")

if pizza_area_price(pizza1Diam, pizza1Price) > pizza_area_price(pizza2Diam, pizza2Price):
    print("Pizza-2 has more bang for your buck!")
else:
    print("Pizza-1 has more bang for your buck!")
