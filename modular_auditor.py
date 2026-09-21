inventory = 0
rejected_entries = 0
number_deliveries = 0


def get_valid_input():
    failed_attempts = 0
    while True:
        user_input = input("Enter a stock quantity or type 'quit' to exit: ")
        if user_input == "quit":
            return "quit", failed_attempts
        elif user_input.isdigit():
            return int(user_input), failed_attempts
        else:
            failed_attempts += 1
            print("Error: Please enter a non-negative whole number or type 'quit' to exit")


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("Total Units Processed: " + str(total_units) + " Number of Failed/Rejected Entries: " + str(failed_attempts))


# ---- main program ----
while True:
    value, failed = get_valid_input()
    rejected_entries += failed

    if value == "quit":
        break

    inventory = process_delivery(inventory, value)
    tax_amount = calculate_tax(value)
    number_deliveries += 1

    if inventory > 500:
        print("Overstock Alert!")
        break

generate_report(inventory, rejected_entries)