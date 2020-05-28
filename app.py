from flask import Flask, render_template, request
from scripts.prep import *


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():

    errors = []
    results = {}
    text = None
    if request.method == "POST":

        if request.form['submit_button'] == 'learn':
            article = None
            try:
                # article = request.form['text']
                article = request.form['textarea']
                print(article)
            except:
                errors.append("<p> Wrong Format, enter text !</p>")

            if article:
                text = Text(article)
                results['top_words'] = text.get_top_words()
                results['vocab'] = text.get_vocab()
                results['lexical_richness'] = text.get_lexical_richness()
                results['average_length'] = text.average_word_length()
                results['questions'] = text.generate_questions()

        if request.form['submit_button'] == 'generate questions':
            pass
            results['questions'] = text.generate_questions()

        return render_template("index.html", errors=errors, results=results)

            # results = [top_words, vocab, lexical_richness, average_length]

    return render_template("index.html", errors=errors, results=results)


if __name__ == '__main__':
    app.run(debug=True)
