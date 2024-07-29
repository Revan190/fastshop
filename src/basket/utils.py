def calculate_total_price(items):
    total = sum(item.price * item.quantity for item in items)
    return total

def format_currency(value):
    return "${:,.2f}".format(value)
