import os
print("DEBUG: os module loaded")

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Jenkins Tutorials</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0')
