# ==========================================================
# CASE 2: M-PESA AGENCY BALANCE RECONCILIATION
# ==========================================================

# -----------------------------
# Opening balances
# -----------------------------
cash_balance = 90000
electronic_float = 110000

# Daily transactions
customer_deposits = 75500
customer_withdrawals = 62300

cash_operating_expenses = 2000
float_purchased = 20000
float_purchase_fee = 200
commission = 1850

# Actual closing balances
actual_closing_cash = 80800
actual_closing_float = 118700

permitted_difference = 100

print("=" * 50)
print("CASE 2: M-PESA AGENCY RECONCILIATION")
print("=" * 50)

print(f"Opening cash balance: KES {cash_balance:.2f}")
print(f"Opening electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Process customer deposits
# -----------------------------
cash_balance += customer_deposits
electronic_float -= customer_deposits

print("\nAfter customer deposits:")
print(f"Cash balance: KES {cash_balance:.2f}")
print(f"Electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Process customer withdrawals
# -----------------------------
cash_balance -= customer_withdrawals
electronic_float += customer_withdrawals

print("\nAfter customer withdrawals:")
print(f"Cash balance: KES {cash_balance:.2f}")
print(f"Electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Deduct operating expenses
# -----------------------------
cash_balance -= cash_operating_expenses

print("\nAfter operating expenses:")
print(f"Cash balance: KES {cash_balance:.2f}")
print(f"Electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Purchase additional float
# -----------------------------
cash_balance -= float_purchased
electronic_float += float_purchased

print("\nAfter purchasing additional float:")
print(f"Cash balance: KES {cash_balance:.2f}")
print(f"Electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Deduct float purchase fee
# -----------------------------
cash_balance -= float_purchase_fee

print("\nAfter deducting float purchase fee:")
print(f"Cash balance: KES {cash_balance:.2f}")
print(f"Electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Add commission
# -----------------------------
electronic_float += commission

print("\nAfter adding commission:")
print(f"Cash balance: KES {cash_balance:.2f}")
print(f"Electronic float: KES {electronic_float:.2f}")

# -----------------------------
# Reconciliation calculations
# -----------------------------

total_customer_transactions = (
    customer_deposits + customer_withdrawals
)

expected_closing_cash = cash_balance
expected_closing_float = electronic_float

cash_discrepancy = actual_closing_cash - expected_closing_cash

float_discrepancy = actual_closing_float - expected_closing_float

total_expected_working_capital = (
    expected_closing_cash + expected_closing_float
)

total_actual_working_capital = (
    actual_closing_cash + actual_closing_float
)

overall_working_capital_discrepancy = (
    total_actual_working_capital
    - total_expected_working_capital
)

# -----------------------------
# Reconciliation tests
# -----------------------------

cash_difference_zero = cash_discrepancy == 0

float_difference_zero = float_discrepancy == 0

cash_within_limit = abs(cash_discrepancy) <= permitted_difference

float_within_limit = abs(float_discrepancy) <= permitted_difference

both_within_limit = cash_within_limit and float_within_limit

either_account_shortage = (
    cash_discrepancy < 0 or float_discrepancy < 0
)

both_balances_positive = (
    actual_closing_cash > 0 and actual_closing_float > 0
)

# -----------------------------
# Display results
# -----------------------------

print("\nRECONCILIATION RESULTS")
print(f"Total customer transactions: KES {total_customer_transactions:.2f}")
print(f"Expected closing cash: KES {expected_closing_cash:.2f}")
print(f"Expected closing float: KES {expected_closing_float:.2f}")
print(f"Cash discrepancy: KES {cash_discrepancy:.2f}")
print(f"Float discrepancy: KES {float_discrepancy:.2f}")
print(
    f"Total expected working capital: "
    f"KES {total_expected_working_capital:.2f}"
)
print(
    f"Total actual working capital: "
    f"KES {total_actual_working_capital:.2f}"
)
print(
    f"Overall working capital discrepancy: "
    f"KES {overall_working_capital_discrepancy:.2f}"
)

print("\nRECONCILIATION TESTS")
print(f"Cash discrepancy exactly zero? {cash_difference_zero}")
print(f"Float discrepancy exactly zero? {float_difference_zero}")
print(f"Cash discrepancy within KES 100? {cash_within_limit}")
print(f"Float discrepancy within KES 100? {float_within_limit}")
print(f"Both balances within permitted difference? {both_within_limit}")
print(f"Either account has a shortage? {either_account_shortage}")
print(f"Both closing balances are positive? {both_balances_positive}")

# -----------------------------
# Duplicate deposit correction
# -----------------------------

duplicate_deposit = 5000

# Correct the recorded deposit total
customer_deposits -= duplicate_deposit

print("\nDUPLICATE TRANSACTION CORRECTION")
print(f"Corrected customer deposits: KES {customer_deposits:.2f}")