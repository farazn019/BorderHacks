from flask import Flask, render_template, request, url_for, redirect # Imports the flask framework.
from flask_bootstrap import Bootstrap
from . forms import TicketForm
from . iata_code_scraper import country_code
import re

app = Flask(__name__)
app.secret_key = "SECRET"
Bootstrap(app)


@app.route('/', methods=("GET", "POST"))
@app.route('/home', methods=("GET", "POST"))
def homepage():

    ticket_form = TicketForm()

    if request.method == "POST":
        departure_location = request.form['current_city']
        departure_city = re.split(', ', departure_location)[0]
        departure_country = re.split(", ", departure_location)[1]
        country_code(departure_country)

        destination = request.form['destination_location']
        destination_city = re.split(', ', destination)[0]
        destination_country = re.split(', ', destination)[1]
        country_code(destination_country)

        departure_date = request.form['leave']
        return_date = request.form['returning']

        return redirect(url_for('prices_page'))
    return render_template('webpage.html', form=ticket_form)


@app.route('/prices', methods=("GET", "POST"))
def prices_page():
    return render_template('pricespage.html')

if __name__ == 'main':
    app.run(debug=True)