from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This page will display the PDF directly
    return render_template('view_pdf.html')

if __name__ == '__main__':
    app.run(debug=True)
