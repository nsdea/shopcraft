import json
import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/balance', methods=['POST', 'GET'])
def balance():
    if flask.request.method == 'POST':
        item_id = flask.request.form.to_dict()['code']
        items = json.loads(open('shop.json').read())

        for item in items:
            if str(item['id']) == item_id:
                return flask.render_template('balance.html', type=item['type'], id=item['id'], balance=item['balance'])
        return flask.render_template('error.html')

    return flask.render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1313)
