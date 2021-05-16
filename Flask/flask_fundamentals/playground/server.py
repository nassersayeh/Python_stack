from flask import Flask , render_template
app = Flask(__name__)
@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template("index.html")

@app.route('/play/<name>')          # The "@" decorator associates this route with the function immediately following
def play2(name): 
    return render_template('index.html', name = int(name))

@app.route('/play/<name>/<color>')          # The "@" decorator associates this route with the function immediately following
def play3(name,color):
    return render_template('index.html', name = int(name), color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 