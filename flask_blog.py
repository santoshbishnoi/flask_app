from flask import Flask, render_template
app = Flask(__name__)

posts=[
    {
        "name":"santosh",
        "age":12
    },
    {
        "name":"maya",
        "age":"9"
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')

