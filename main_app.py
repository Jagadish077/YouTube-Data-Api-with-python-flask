from flask import Flask, render_template, request
from data import YouTubeData

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        # getting the video details like images and channelid
        search = request.form['search']
        data = YouTubeData(search)
        snippet = data.get_channel_details(search)
        return render_template('search_page.html', message=snippet, search=search)
    else:
        return render_template('base.html')


@app.route('/get_more/<channelId>/<search>/<videoid>', methods=['GET', 'POST'])
def get_more(channelId, search, videoid):
    if request.method == 'GET':
        data = YouTubeData(search)
        content = data.get_channel_stats(channelId)

        snippet = data.get_videoDetails(videoid)

        stats = data.get_statistics(videoid)

        return render_template("moredata.html", subCount=content, statistics=stats, snippet=snippet)
    else:
        return "Page Not Found"


if __name__ == '__main__':
    app.run(debug=True)
