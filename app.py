from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

comments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        comments.append({
            'text': comment,
            'sentiment': sentiment
        })

    return render_template('index.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
