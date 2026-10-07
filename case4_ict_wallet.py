# ==========================================================
# CASE 4: UNIVERSITY ICT SERVICE WALLET
# ==========================================================

# -----------------------------
# Input values
# -----------------------------
opening_balance = 2500

top_up = 1000
top_up_fee_rate = 0.015

black_white_pages = 75
black_white_rate = 5

colour_pages = 8
colour_rate = 25

documents_bound = 2
binding_rate = 80

internet_hours = 6
internet_rate = 40

scholarship_discount_rate = 0.12
scholarship_eligibility = 1

minimum_emergency_balance = 500

# -----------------------------
# Wallet calculations
# -----------------------------

# Calculate top-up service fee
top_up_fee = top_up * top_up_fee_rate

# Available balance after top-up and fee
available_balance = (
    opening_balance + top_up - top_up_fee
)

# Printing costs
black_white_cost = (
    black_white_pages * black_white_rate
)

colour_printing_cost = (
    colour_pages * colour_rate
)

total_printing_before_discount = (
    black_white_cost + colour_printing_cost
)

# Scholarship discount
scholarship_discount = (
    total_printing_before_discount
    * scholarship_discount_rate
    * scholarship_eligibility
)

# Printing cost after discount
printing_cost_after_discount = (
    total_printing_before_discount
    - scholarship_discount
)

# Binding cost
total_binding_cost = (
    documents_bound * binding_rate
)

# Internet cost
total_internet_cost = (
    internet_hours * internet_rate
)

# Total amount spent
total_amount_spent = (
    printing_cost_after_discount
    + total_binding_cost
    + total_internet_cost
)

# Remaining balance
remaining_balance = (
    available_balance - total_amount_spent
)

# -----------------------------
# Budget analysis
# -----------------------------

printing_percentage = (
    printing_cost_after_discount
    / available_balance
) * 100

binding_percentage = (
    total_binding_cost
    / available_balance
) * 100

internet_percentage = (
    total_internet_cost
    / available_balance
) * 100

# Maximum additional pages using all remaining money
additional_pages = (
    int(remaining_balance // black_white_rate)
)

# Maximum pages while keeping KES 500 emergency balance
safe_additional_pages = int(
    (remaining_balance - minimum_emergency_balance)
    // black_white_rate
)

# -----------------------------
# Boolean expressions
# -----------------------------

positive_balance = remaining_balance > 0

emergency_balance_preserved = (
    remaining_balance >= minimum_emergency_balance
)

printing_greater_than_other_services = (
    printing_cost_after_discount
    > (total_binding_cost + total_internet_cost)
)

can_print_100_pages = (
    remaining_balance >= (100 * black_white_rate)
)

can_print_100_and_keep_emergency = (
    remaining_balance
    >= (100 * black_white_rate)
    + minimum_emergency_balance
)

qualifies_and_printed_more_than_50 = (
    scholarship_eligibility == 1
    and black_white_pages + colour_pages > 50
)

# -----------------------------
# Display results
# -----------------------------

print("=" * 50)
print("CASE 4: UNIVERSITY ICT SERVICE WALLET")
print("=" * 50)

print(f"Top-up service fee: KES {top_up_fee:.2f}")
print(
    f"Available balance after top-up and fee: "
    f"KES {available_balance:.2f}"
)

print(
    f"Black-and-white printing cost: "
    f"KES {black_white_cost:.2f}"
)

print(
    f"Colour printing cost: "
    f"KES {colour_printing_cost:.2f}"
)

print(
    f"Total printing before discount: "
    f"KES {total_printing_before_discount:.2f}"
)

print(
    f"Scholarship discount: "
    f"KES {scholarship_discount:.2f}"
)

print(
    f"Printing cost after discount: "
    f"KES {printing_cost_after_discount:.2f}"
)

print(
    f"Total binding cost: "
    f"KES {total_binding_cost:.2f}"
)

print(
    f"Total internet cost: "
    f"KES {total_internet_cost:.2f}"
)

print(
    f"Total amount spent: "
    f"KES {total_amount_spent:.2f}"
)

print(
    f"Remaining wallet balance: "
    f"KES {remaining_balance:.2f}"
)

print("\nBUDGET ANALYSIS")

print(
    f"Percentage spent on printing: "
    f"{printing_percentage:.2f}%"
)

print(
    f"Percentage spent on binding: "
    f"{binding_percentage:.2f}%"
)

print(
    f"Percentage spent on internet: "
    f"{internet_percentage:.2f}%"
)

print(
    f"Maximum additional black-and-white pages: "
    f"{additional_pages}"
)

print(
    f"Maximum additional pages while keeping "
    f"KES 500 emergency balance: "
    f"{safe_additional_pages}"
)

print("\nLOGICAL TESTS")

print(f"Does the wallet have a positive balance? {positive_balance}")

print(
    f"Has the emergency balance been preserved? "
    f"{emergency_balance_preserved}"
)

print(
    f"Is printing more expensive than binding and internet combined? "
    f"{printing_greater_than_other_services}"
)

print(
    f"Can the student print another 100 black-and-white pages? "
    f"{can_print_100_pages}"
)

print(
    f"Can the student print another 100 pages and keep "
    f"the emergency balance? "
    f"{can_print_100_and_keep_emergency}"
)

print(
    f"Does the student qualify for the discount and have "
    f"printed more than 50 pages? "
    f"{qualifies_and_printed_more_than_50}"
)

# ==========================================================
# DEBUGGING CHALLENGE
# ==========================================================

# Incorrect expression
incorrect_printing_cost = (
    black_white_pages
    + black_white_rate
    + colour_pages
    + colour_rate
)

# Correct expression
correct_printing_cost = (
    black_white_pages * black_white_rate
    + colour_pages * colour_rate
)

print("\nDEBUGGING CHALLENGE")

print(
    f"Incorrect printing cost: "
    f"KES {incorrect_printing_cost:.2f}"
)

print(
    f"Correct printing cost: "
    f"KES {correct_printing_cost:.2f}"
)

print(
    "\nThe incorrect expression uses addition instead of "
    "multiplication."
)

# Another incorrect expression
incorrect_remaining_balance = (
    available_balance
    - printing_cost_after_discount
    + total_binding_cost
    + total_internet_cost
)

# Correct expression
correct_remaining_balance = (
    available_balance
    - (
        printing_cost_after_discount
        + total_binding_cost
        + total_internet_cost
    )
)

print(
    f"\nIncorrect remaining balance: "
    f"KES {incorrect_remaining_balance:.2f}"
)

print(
    f"Correct remaining balance: "
    f"KES {correct_remaining_balance:.2f}"
)



