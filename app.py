from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')          
def default_board():
    return render_template("index.html", rows = 8, cols = 8, color1="brown", color2 = "beige", width1= str(40*8) + "px", height1= str(40*8) + "px")   

@app.route('/<x>')          
def num_board(x):
    return render_template("index.html", rows = int(x), cols = 8, color1="brown", color2 = "beige", width1= str(40*8) + "px", height1= str(40*int(x)) + "px")

@app.route('/<x>/<y>')          
def x_y_board(x, y):
    return render_template("index.html", rows = int(x), cols = int(y), color1="brown", color2 = "beige", width1= str(40*int(y)) + "px", height1= str(40*int(x)) + "px")

@app.route('/<x>/<y>/<color1>/<color2>')          
def x_y_color_board(x, y, color1, color2):
    return render_template("index.html", rows = int(x), cols = int(y), color1 = color1, color2 = color2, width1= str(40*int(y)) + "px", height1= str(40*int(x)) + "px")

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again"

if __name__=="__main__":    
    app.run(debug=True)    