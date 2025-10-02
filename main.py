from pyscript import display, document

def create_order(e):
    name = document.getElementById("custom_name").value
    address = document.getElementById("custom_address").value
    contact = document.getElementById("custom_contact").value

    menu = {
        "2 Piece Fried Chicken": ("2 Piece Fried Chicken", 200),
        "Bucket": ("Bucket", 600),
        "Barbeque Crispy Fries": ("Barbeque Crispy Fries", 150),
        "Milkshake": ("Iced Tea", 60),
        "Water": ("Bottled Water", 30)
    }

    total = 0
    ordered_items = []

    for item_id, (label, price) in menu.items():
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            ordered_items.append(label)
            total += price

    items_list = ", ".join(ordered_items) if ordered_items else "No items selected"
    order_message = f"""
    Order for: {name}
    Address: {address}
    Contact number: {contact}
    Ordered Items: {items_list}
    Total: ₱ {total:.2f}
    """
    display("", target="output")
    display(order_message, target="output")
