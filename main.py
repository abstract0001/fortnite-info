from flask import Flask ,render_template ,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/weapon')
def weapon():
    return render_template('weapon.html')


@app.route('/weapon/c')
def common():
    return render_template('common.html')


@app.route('/weapon/u')
def uncommon():
    return render_template('uncommon.html')


@app.route('/weapon/r')
def rare():
    return render_template('rare.html')


@app.route('/weapon/e')
def epic():
    return render_template('epic.html')


@app.route('/weapon/l')
def legendary():
    return render_template('legendary.html')



@app.route('/healing')
def healing():
    return render_template('healing.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug = True)


