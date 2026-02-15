from flask import Flask, render_template

app = Flask(__name__)

# मेन होम पेज (जहाँ 4 कैटेगरी दिखेंगी)
@app.route('/')
def home():
    return render_template('index.html')

# साड़ियों वाला पेज
@app.route('/sarees')
def sarees():
    return "<h1>Elegant Indian Sarees</h1><p>Amazon links will go here!</p>"

# घड़ियों वाला पेज
@app.route('/watches')
def watches():
    return "<h1>Luxury Watches</h1><p>Amazon links will go here!</p>"

# ब्यूटी और शूज के लिए भी ऐसे ही राउट्स हम बाद में ऐड कर लेंगे

if __name__ == '__main__':
    app.run(debug=True)