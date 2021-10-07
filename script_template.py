# This seven lines of code initializes the web page
# this is the script exectuted  __name__="__main__"  
# This is the script imported __name__="script`" if you import this into another script
# The if statement looks for the name and returns true if triggered
# The current URL is '/' ex of different is '/about/' but when you look for the page use localhost:5000/about/

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Test - website home page goes here!"

@app.route('/about/')
def about():
    return "Test - About content goes here!"

if __name__=="__main__":
    app.run(debug=True)
# to run  use -->>  python .\script1.py
# then go to web page localhost:5000 and see the results