from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

#static images in static folder
#html+css files in templates
#shift refresh clears site cache - so static files reload
#can edit html in chrome in devtool - js - document.body.contenteditable=true and then save html file
    # can del files by devtool chrome - select tool - backspace

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__": #checks if this is imported module
    app.run(debug= True) #flask run in terminal same as this