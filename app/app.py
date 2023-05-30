from flask import Flask, render_template, request
import requests

# membuat nama app
app = Flask(__name__)

# Membuat route dan fungsi
@app.route('/')
def index():
    return render_template('index.html')

# ============= disini akan menjadi mesin ==================

@app.route('/tukar', methods=['POST'])
def convert():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        base_currency = request.form['base_currency']
        target_currency = request.form['target_currency']

        # Mengirim permintaan ke API untuk mendapatkan data kurs mata uang terbaru
        api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(api_url)
        data = response.json()
        target_rate = data['rates'][target_currency]

        converted_amount = amount * target_rate

    return render_template('index.html', amount=amount, base_currency=base_currency,
                           target_currency=target_currency, converted_amount=converted_amount)


# Membuat debug run menjalankan flask
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
