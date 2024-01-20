from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/copy-file.html')
def copyfile():
    return render_template("copy-file.html")

@app.route('/model-archi.html')
def modelarchi():
    return render_template("model-archi.html")

@app.route('/model.html')
def model():
    return render_template("model.html")

@app.route('/output-after.html')
def outputafter():
    return render_template("output-after.html")

@app.route('/output-afterm.html')
def outputafterm():
    return render_template("output-afterm.html")

@app.route('/output-before.html')
def outputbefore():
    return render_template("output-before.html")

@app.route('/pic-archi.html')
def picarchi():
    return render_template("pic-archi.html")

@app.route('/about-us.html')
def aboutus():
    return render_template("about-us.html")

if __name__ == '__main__':
    app.run(debug=True)