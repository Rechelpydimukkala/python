from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Jenkins Tutorials</h1>"

if __name__ == '__main__':
    print("DEBUG: os module is loaded")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
