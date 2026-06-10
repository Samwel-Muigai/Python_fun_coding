def calculate_product_cost():
    try:
        price = float(input("Enter product price: "))
        quantity = float(input("Enter product quantity: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    cost = price * quantity

    if cost < 1000:
        discount_percent = 0
    elif 1000 <= cost <= 10000:
        discount_percent = 3
    elif 10001 <= cost <= 100000:
        discount_percent = 5
    else:
        discount_percent = 8

    discount_amount = (discount_percent / 100) * cost
    final_cost = cost - discount_amount

    print(f"\nInitial Cost:      ${cost:,.2f}")
    print(f"Discount Rate:     {discount_percent}%")
    print(f"Discount Amount:   ${discount_amount:,.2f}")
    print(f"Final Total Cost:  ${final_cost:,.2f}")


if __name__ == "__main__":
    calculate_product_cost()
