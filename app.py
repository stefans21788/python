from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    name = input("Enter your name: ")
    return "Hello, " + name + "! Welcome to the Python app."

if __name__ == "__main__":
    app.run()
