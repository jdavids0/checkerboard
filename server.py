from flask import Flask, render_template
app = Flask(__name__)

#will display 8x8
@app.route('/')
def default():
    print('root route working')
    return render_template('index.html', rows = 8, columns = 8, color1 = "black", color2 = "red")

#integer passed will display rows
@app.route('/<int:rows>')
def changeRows(rows):
    return render_template('index.html', rows = rows, columns = 8, color1 = "black", color2 = "red")

#integers passed will display rows and columns
@app.route('/<int:x>/<int:y>')
def changeBoth(x, y):
     return render_template('index.html', rows = x, columns = y, color1 = "black", color2 = "red")

# couldn't get this one working - come back and try later
# @app.route('/<int:x>/<int:y>, <color_x>, <color_y>')
# def changeBoth(x, y, "color_one", "color_two")
#    return render_template('index.html', rows = x, columns = y, color_x = color_one, color_y = color_two)


if __name__=="__main__":  
    app.run(debug=True, port=5001)  