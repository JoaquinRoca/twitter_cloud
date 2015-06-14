__author__ = 'Alicia'
from os import path
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
from nltk.corpus import stopwords
import re
import psycopg2


for_word_cloud=[]

app = Flask(__name__)
app.config.from_object(__name__)

con=psycopg2.connect("dbname='twitterdb' user='ap' host='localhost' password='apowers411'")
cur=con.cursor()

@app.route('/')
def images():
    return render_template("wordcloud.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
