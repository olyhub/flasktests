from flask import Flask, render_template

app = Flask(__name__)

fruits = [{
    'type': 'Banana',
    'origin': 'Ireland',
    'colour': 'Green'
},
    {
        'type': 'Kiwi',
        'origin': 'Easteren Europe',
        'colour': 'Brown'
    },
    {
        'type': 'Pear',
        'origin': 'Peru',
        'colour': 'Purple'
    }
]


@app.route('/')
def get_index():
    return render_template('index.html', fruits=fruits)


if __name__ == '__main__':
    app.run()
