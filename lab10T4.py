def calc_consumption(consumption, price, trip):
    fuel = (trip/100)*consumption
    cost = fuel*price
    return fuel, cost
    
    
trip = input("Enter trip length in km:")
price = input("Enter fuel price/liter:")
consumption = input("Enter fuel consumption/100 km:")
result = calc_consumption(float(consumption), float(price), float(trip))
print("Fuel: {:.2f} liter".format(result[0]))
print("Cost: {:.2f} €".format(result[1]))

