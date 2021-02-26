from flask import Flask, render_template,request
from tweet import *
from camelcase import CamelCase

c = CamelCase()

app = Flask(__name__)


@app.route('/trends', methods=["GET","POST"])
def get_tweets():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
    api = authentication()
    woeid = search_woeid(api,name)
    if woeid == 1:
        name = 'Worldwide'
    data = data_fetching(api,woeid)
    clean_data = data_cleaning(data)
    return render_template('index.html', data = clean_data, name = c.hump(name))

@app.route('/', methods=["GET"])
def search_country():
    return render_template('search.html')

if __name__ == '__main__' :
    app.run()