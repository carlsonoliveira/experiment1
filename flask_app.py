from flask import Flask, render_template, request, session
from flask_session import Session
from topicextraction import nmf_topic_extraction

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html", text="")

@app.route("/topicextraction", methods=["POST"])
def topicextraction(texto):
    termos = dict()
    dataset = texto.lower()
    n_samples = len(dataset)
    n_features = 4000
    n_topics = 12
    n_top_words = 20
    stopwords = carrega_stopwords('stopwords-port.txt')
    nmf, tfidf_feature_names = nmf_topic_extraction(dataset,
                                                        stopwords,
                                                        n_samples,
                                                        n_features,
                                                        n_topics,
                                                        n_top_words)
    return render_template("nuvem_termos.html",
                        termos=lista_top_words(nmf, tfidf_feature_names, n_top_words))


if __name__ == "__main__":
  app.run(debug=True)
