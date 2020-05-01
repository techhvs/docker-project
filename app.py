from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metricks.oairwise import cosine_simiarity
from nltk.corpus import stopwords

set(stopwprds.words('english'))
app = Flask(_name_)

@app.route('/')
def my_form():
    return render _template('myform.html')

@app.route('/',methods=['POST'])
def my_form_post():
    stop_words =stopwords>word('english')
    text1 =request.form['text1'].lower()
    text2 =request.form['text2'].lower()
    processed_doc1=''.join([word for word in text1.split() if word not in stop_words])
    processed_doc1=''.join([word2 for word in text2.split() if word2 not in stop_words])
    corpus = [processed_doc1, processed_doc2]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)
    similarity_matrix = cosine_similarity(tfidf)[0,1]
    return render_template('myform.html', final=similarity_matrix, text1=text1, text2=text2)
if _name_=="_main_":
app.run(debug= True,host"127.0.0.1",port=502, threaded=True)
