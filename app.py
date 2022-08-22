from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
    
def multiplying():
    multiply= [multi* 2 for multi in x]  
    return multiply 