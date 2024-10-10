from flask import Flask
#used from when we need to impot something specific from a module
#like a particular class, funciton or variable
#in this case we're only importing the flask clas from the larger flask module
#if we had just used 
#      "import flask"
#we would have to refer to everything in the flask module with flask

app = Flask(__name__)

# The __name__ is a special variable in Python that holds the name of the current module. It helps Flask determine the root path of the app, which is important when loading resources like templates or static files.

@app.route('/')

# This tells Flask to handle requests to the root URL (/). Now, after this, we’ll define a function that runs whenever someone visits the homepage. Let me know when you’re ready for the next part


def homepage():
    return "Hello, World!"


if __name__== '__main__':
    app.run(debug=True)

    # The debug=True part is optional, but it’s useful during development because it will show helpful error messages if something goes wrong.