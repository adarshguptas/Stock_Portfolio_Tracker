document.addEventListener("DOMContentLoaded", function () {

    const stockInput = document.getElementById("stock_name");
    const quantityInput = document.getElementById("quantity");

    if (stockInput) {
        stockInput.focus();

        stockInput.addEventListener("input", function () {
            this.value = this.value.toLowerCase();
        });
    }


    if (quantityInput) {
        quantityInput.addEventListener("input", function () {

            if (this.value < 0) {
                this.value = "";
            }

        });
    }

});