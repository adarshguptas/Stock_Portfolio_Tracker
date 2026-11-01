from django.shortcuts import render


STOCKS = {
    "tcs": 3500,
    "infosys": 1800,
    "reliance": 2900,
    "hdfc": 1700,
    "wipro": 500,
    "itc": 450,
    "sbi": 850,
    "adani": 2500,
}


def home(request):

    result = None
    error = None

    if request.method == "POST":

        stock_name = request.POST.get("stock_name", "").strip().lower()
        quantity = request.POST.get("quantity", "").strip()

        if stock_name not in STOCKS:
            error = "Stock not found. Please enter a valid stock name."

        elif not quantity:
            error = "Please enter the quantity."

        else:
            try:
                quantity = int(quantity)

                if quantity <= 0:
                    error = "Quantity must be greater than 0."

                else:
                    price = STOCKS[stock_name]
                    total = price * quantity

                    result = {
                        "stock_name": stock_name.upper(),
                        "price": price,
                        "quantity": quantity,
                        "total": total,
                    }

            except ValueError:
                error = "Please enter a valid quantity."

    context = {
        "stocks": STOCKS,
        "result": result,
        "error": error,
    }

    return render(request, "portfolio/index.html", context)