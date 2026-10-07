# ==========================================================
# CASE 1: NYERI-NAIROBI MATATU OPERATIONS
# Programming Laboratory
# ==========================================================

# Vehicle capacity stored as a constant
VEHICLE_CAPACITY = 14

# -----------------------------
# Input values
# -----------------------------
distance = 150
passengers = 12
fare_per_passenger = 800

parcels = 5
charge_per_parcel = 200

fuel_litres = 24
fuel_price = 190

driver_allowance = 1200
conductor_allowance = 700
other_expenses = 450

sacco_levy_rate = 0.05
mobile_money_percentage = 0.75
mobile_money_transaction_rate = 0.015

target_profit = 3000

# -----------------------------
# Trip calculations
# -----------------------------

# Passenger revenue
passenger_revenue = passengers * fare_per_passenger

# Parcel revenue
parcel_revenue = parcels * charge_per_parcel

# Gross revenue
gross_revenue = passenger_revenue + parcel_revenue

# Vehicle occupancy percentage
occupancy_percentage = (passengers / VEHICLE_CAPACITY) * 100

# Amount received through mobile money
mobile_money_amount = gross_revenue * mobile_money_percentage

# Mobile money transaction cost
mobile_money_cost = mobile_money_amount * mobile_money_transaction_rate

# SACCO levy
sacco_levy = gross_revenue * sacco_levy_rate

# Fuel cost
fuel_cost = fuel_litres * fuel_price

# Total operating cost
total_operating_cost = (
    fuel_cost
    + driver_allowance
    + conductor_allowance
    + other_expenses
    + mobile_money_cost
    + sacco_levy
)

# Net trip profit
net_profit = gross_revenue - total_operating_cost

# Profit per passenger
profit_per_passenger = net_profit / passengers

# Profit per kilometre
profit_per_kilometre = net_profit / distance

# -----------------------------
# Boolean expressions
# -----------------------------

made_profit = net_profit > 0

met_target = net_profit >= target_profit

at_least_80_percent_occupied = occupancy_percentage >= 80

profitable_and_80_percent_occupied = (
    made_profit and at_least_80_percent_occupied
)

passengers_exceeded_capacity = passengers > VEHICLE_CAPACITY

# -----------------------------
# Display results
# -----------------------------

print("=" * 50)
print("CASE 1: NYERI-NAIROBI MATATU OPERATIONS")
print("=" * 50)

print(f"Passenger revenue: KES {passenger_revenue:.2f}")
print(f"Parcel revenue: KES {parcel_revenue:.2f}")
print(f"Gross trip revenue: KES {gross_revenue:.2f}")
print(f"Vehicle occupancy: {occupancy_percentage:.2f}%")
print(f"Mobile money amount: KES {mobile_money_amount:.2f}")
print(f"Mobile money transaction cost: KES {mobile_money_cost:.2f}")
print(f"SACCO levy: KES {sacco_levy:.2f}")
print(f"Fuel cost: KES {fuel_cost:.2f}")
print(f"Total operating cost: KES {total_operating_cost:.2f}")
print(f"Net trip profit: KES {net_profit:.2f}")
print(f"Profit per passenger: KES {profit_per_passenger:.2f}")
print(f"Profit per kilometre: KES {profit_per_kilometre:.2f}")

print("\nBOOLEAN TESTS")
print(f"Did the matatu make a profit? {made_profit}")
print(f"Did the matatu meet the KES 3,000 target? {met_target}")
print(f"Was occupancy at least 80%? {at_least_80_percent_occupied}")
print(
    f"Was the trip profitable AND at least 80% occupied? "
    f"{profitable_and_80_percent_occupied}"
)
print(
    f"Did passengers exceed vehicle capacity? "
    f"{passengers_exceeded_capacity}"
)

# ==========================================================
# FUEL PRICE SIMULATION
# ==========================================================

# Store the original values before changing them
original_fuel_price = fuel_price
original_profit = net_profit

# Increase fuel price by 8% using compound assignment
fuel_price *= 1.08

# Recalculate fuel cost
new_fuel_cost = fuel_litres * fuel_price

# Recalculate operating cost
new_total_operating_cost = (
    new_fuel_cost
    + driver_allowance
    + conductor_allowance
    + other_expenses
    + mobile_money_cost
    + sacco_levy
)

# Recalculate profit
new_net_profit = gross_revenue - new_total_operating_cost

# Difference between original and new profit
profit_difference = original_profit - new_net_profit

# Check if the new profit still meets the target
still_meets_target = new_net_profit >= target_profit

print("\nFUEL PRICE SIMULATION")
print(f"Original fuel price: KES {original_fuel_price:.2f}")
print(f"New fuel price: KES {fuel_price:.2f}")
print(f"New fuel cost: KES {new_fuel_cost:.2f}")
print(f"New net profit: KES {new_net_profit:.2f}")
print(f"Difference in profit: KES {profit_difference:.2f}")
print(f"Still meets target profit? {still_meets_target}")

# ==========================================================
# OPERATOR PRECEDENCE INVESTIGATION
# ==========================================================

# Incorrect expression
incorrect_profit = (
    gross_revenue
    - fuel_litres * fuel_price
    + driver_allowance
    + conductor_allowance
    + other_expenses
)

# Correct expression using parentheses
correct_profit = gross_revenue - (
    fuel_litres * fuel_price
    + driver_allowance
    + conductor_allowance
    + other_expenses
    + mobile_money_cost
    + sacco_levy
)

print("\nOPERATOR PRECEDENCE INVESTIGATION")
print(f"Incorrect expression result: KES {incorrect_profit:.2f}")
print(f"Correct expression result: KES {correct_profit:.2f}")

print("\nThe incorrect expression does not group all operating")
print("costs together for subtraction from gross revenue.")
print("Parentheses make the intended calculation clear.")