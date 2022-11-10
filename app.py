from decimal import Decimal, DecimalException

from flask import Flask, flash, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import (CurrencyCodes, CurrencyRates,
                                    RatesNotAvailableError)

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def ask_questions():
    """Generate and show form to ask countries currencies."""

    return render_template("form.html")


@app.route("/conversion", methods=["POST"])
def show_amount():
    """Show conversion result."""
    
    convert_from = request.form["convert_from"]
    convert_to = request.form["convert_to"]
    try:
        amount = Decimal(request.form["amount"])
    except DecimalException:
        flash("Amount Is Not Valid")
        return redirect("/")

    rate = CurrencyRates()
    code = CurrencyCodes()

    try:
        results = round(rate.convert(convert_from, convert_to, amount), 2)
        symbol = code.get_symbol(convert_to)
    except RatesNotAvailableError:
        flash("Invalid Currency Code")
        return redirect("/")
    """return the result"""
    return render_template("result.html", result=results, symbol =symbol)



