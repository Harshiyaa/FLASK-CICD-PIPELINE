from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello Interns! CI/CD Working!"
if __name__ == "__main__":
   app.run()