from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    # Retrieve data from the form
    data = request.form['data']
    
    # Process the data (e.g., store it in a database)
    # Your Python script code goes here
    
    # Redirect back to the index page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
