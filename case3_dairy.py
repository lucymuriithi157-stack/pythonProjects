# ==========================================================
# CASE 3: DAIRY COOPERATIVE FARMER PAYMENT
# ==========================================================

# -----------------------------
# Input values
# -----------------------------
morning_milk = 18.5
evening_milk = 14

rejected_rate = 0.04

milk_price = 52
quality_bonus_rate = 0.06

transport_charge_per_litre = 2.50
cooperative_levy_rate = 0.015

animal_feed_deduction = 650
sacco_loan_deduction = 900

quality_score = 3.8
outstanding_loan = 8500

# -----------------------------
# Milk calculations
# -----------------------------

total_milk = morning_milk + evening_milk

rejected_milk = total_milk * rejected_rate

accepted_milk = total_milk - rejected_milk

basic_milk_earnings = accepted_milk * milk_price

quality_bonus = basic_milk_earnings * quality_bonus_rate

gross_milk_earnings = (
    basic_milk_earnings + quality_bonus
)

transport_charge = (
    accepted_milk * transport_charge_per_litre
)

cooperative_levy = (
    gross_milk_earnings * cooperative_levy_rate
)

total_deductions = (
    transport_charge
    + cooperative_levy
    + animal_feed_deduction
    + sacco_loan_deduction
)

net_daily_payment = (
    gross_milk_earnings - total_deductions
)

projected_30_day_payment = (
    net_daily_payment * 30
)

effective_earnings_per_litre = (
    net_daily_payment / accepted_milk
)

# -----------------------------
# Premium supplier tests
# -----------------------------

accepted_milk_requirement = accepted_milk >= 30

quality_requirement = quality_score >= 3.5

loan_requirement = outstanding_loan <= 10000

premium_supplier = (
    accepted_milk_requirement
    and quality_requirement
    and loan_requirement
)

at_least_one_requirement = (
    accepted_milk_requirement
    or quality_requirement
    or loan_requirement
)

# -----------------------------
# Display results
# -----------------------------

print("=" * 50)
print("CASE 3: DAIRY COOPERATIVE FARMER PAYMENT")
print("=" * 50)

print(f"Total milk delivered: {total_milk:.2f} litres")
print(f"Rejected milk: {rejected_milk:.2f} litres")
print(f"Accepted milk: {accepted_milk:.2f} litres")
print(f"Basic milk earnings: KES {basic_milk_earnings:.2f}")
print(f"Quality bonus: KES {quality_bonus:.2f}")
print(f"Gross milk earnings: KES {gross_milk_earnings:.2f}")
print(f"Transport charge: KES {transport_charge:.2f}")
print(f"Cooperative levy: KES {cooperative_levy:.2f}")
print(f"Total deductions: KES {total_deductions:.2f}")
print(f"Net daily payment: KES {net_daily_payment:.2f}")
print(
    f"Projected 30-day payment: "
    f"KEs {projected_30_day_payment:.2f}"
)
print(
    f"Effective earnings per accepted litre: "
    f"KES {effective_earnings_per_litre:.2f}"
)

print("\nPREMIUM SUPPLIER TESTS")
print(
    f"Accepted milk at least 30 litres? "
    f"{accepted_milk_requirement}"
)
print(
    f"Quality score at least 3.5? "
    f"{quality_requirement}"
)
print(
    f"Loan balance within permitted limit? "
    f"{loan_requirement}"
)
print(f"Premium supplier? {premium_supplier}")
print(
    f"Meets at least one requirement? "
    f"{at_least_one_requirement}"
)

# ==========================================================
# CHANGING MARKET CONDITIONS
# ==========================================================

# Store original values
original_rejected_rate = rejected_rate
original_milk_price = milk_price
original_transport_charge = transport_charge_per_litre
original_payment = net_daily_payment

# Rejection rate increases by 5 percentage points
rejected_rate += 0.05

# Milk price decreases by KES 3
milk_price -= 3

# Transport charge increases by 10%
transport_charge_per_litre *= 1.10

# Recalculate values
new_rejected_milk = total_milk * rejected_rate

new_accepted_milk = (
    total_milk - new_rejected_milk
)

new_basic_earnings = (
    new_accepted_milk * milk_price
)

new_quality_bonus = (
    new_basic_earnings * quality_bonus_rate
)

new_gross_earnings = (
    new_basic_earnings + new_quality_bonus
)

new_transport_charge = (
    new_accepted_milk
    * transport_charge_per_litre
)

new_cooperative_levy = (
    new_gross_earnings
    * cooperative_levy_rate
)

new_total_deductions = (
    new_transport_charge
    + new_cooperative_levy
    + animal_feed_deduction
    + sacco_loan_deduction
)

new_net_payment = (
    new_gross_earnings
    - new_total_deductions
)

payment_change = (
    original_payment - new_net_payment
)

payment_change_percentage = (
    payment_change / original_payment
) * 100

# New premium supplier test
new_premium_supplier = (
    new_accepted_milk >= 30
    and quality_score >= 3.5
    and outstanding_loan <= 10000
)

print("\nCHANGING MARKET CONDITIONS")
print(f"New rejection rate: {rejected_rate * 100:.2f}%")
print(f"New milk price: KES {milk_price:.2f}")
print(
    f"New transport charge: "
    f"KES {transport_charge_per_litre:.2f}"
)
print(f"New net payment: KES {new_net_payment:.2f}")
print(f"Payment change: KES {payment_change:.2f}")
print(
    f"Payment change percentage: "
    f"{payment_change_percentage:.2f}%"
)
print(
    f"Still a premium supplier? "
    f"{new_premium_supplier}"
)

# ==========================================================
# EXPRESSION CORRECTION
# ==========================================================

# Incorrect if rejected_rate is entered as 4 instead of 0.04
rejection_rate_as_percentage = 4

incorrect_accepted_milk = (
    total_milk
    - total_milk * rejection_rate_as_percentage
)

# Correct approach when rate is stored as 4
correct_accepted_milk = (
    total_milk
    - total_milk * (rejection_rate_as_percentage / 100)
)

# Correct approach when rate is stored as 0.04
rejection_rate_decimal = 0.04

correct_accepted_milk_decimal = (
    total_milk
    - total_milk * rejection_rate_decimal
)

print("\nEXPRESSION CORRECTION")
print(
    f"Incorrect accepted milk: "
    f"{incorrect_accepted_milk:.2f} litres"
)
print(
    f"Correct accepted milk when rate = 4: "
    f"{correct_accepted_milk:.2f} litres"
)
print(
    f"Correct accepted milk when rate = 0.04: "
    f"{correct_accepted_milk_decimal:.2f} litres"
)