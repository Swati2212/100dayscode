from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    # Run the app into the debug mode to auto-mode
    app.run(debug=True)
