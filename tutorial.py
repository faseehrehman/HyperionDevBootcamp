from flask import Flask, request

app = Flask(__name__)

# initialize empty menu, stock, and price dictionaries
menu = {}
stock = {}
price = {}

# load inventory data from file (if it exists)
try:
    with open("inventory.txt", "r") as f:
        for line in f:
            item, stock_value, price_value = line.strip().split(",")
            menu[item] = None
            stock[item] = int(stock_value)
            price[item] = float(price_value)
except FileNotFoundError:
    pass

@app.route("/", methods=["GET", "POST"])
def display_results():
    # if a POST request is received, update the menu, stock, and price dictionaries
    if request.method == "POST":
        if request.form["action"] == "add":
            item = request.form["item"]
            price_value = float(request.form["price"])
            stock_value = int(request.form["stock"])

            menu[item] = None # add item to menu dictionary
            price[item] = price_value  # add price to price dictionary
            stock[item] = stock_value  # add stock to stock dictionary

        elif request.form["action"] == "remove":
            item = request.form["item"]

            if item in menu:
                del menu[item]
                del price[item]
                del stock[item]

        # save inventory data to file
        with open("inventory.txt", "w") as f:
            for item in menu:
                stock_value = stock[item]
                price_value = price[item]
                f.write(f"{item},{stock_value},{price_value}\n")

    # calculate total stock
    total_stock = sum(stock[item] * price[item] for item in menu)

    # display the results
    results = f"Menu: {list(menu.keys())}<br>Stock: {list(stock.values())}<br>Total stock worth: GBP {round(total_stock, 2)}"

    # add form for user input
    form = """
        <form method="POST">
            <label for="item">Item:</label>
            <input type="text" id="item" name="item"><br>
            <label for="price">Price:</label>
            <input type="text" id="price" name="price"><br>
            <label for="stock">Stock:</label>
            <input type="text" id="stock" name="stock"><br>
            <input type="submit" name="action" value="add">
            <input type="submit" name="action" value="remove">
        </form>
    """

    return f"{results}<br><br>{form}"

if __name__ == "__main__":
    app.run()

