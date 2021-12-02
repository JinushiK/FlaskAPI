from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO'

@app.route('/Home')
def bye():
    return 'Bye'

if __name__=='__main__':
    app.run()