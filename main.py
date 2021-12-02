from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO'

@app.route('/Home')
def bye():
    return 'Bye'

class Test:
    pass
Test.x=45
Test.foo=lambda self: print("Hello")
myobj=Test()
print(myobj.x)
myobj.foo()

if __name__=='__main__':
    app.run()