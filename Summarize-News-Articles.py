import tkinter as tk
from newspaper import Article
import nltk
from textblob import TextBlob

def summarize():

    url=utext.get('1.0', "end").strip()

    article=Article(url)
    article.download()
    article.parse()

    article.nlp()

    authors.config(state='normal')
    title.config(state='normal')
    publish_date.config(state='normal')
    sentiment.config(state='normal')
    summary.config(state='normal')
    

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors.delete('1.0', 'end')
    authors.insert('1.0', article.authors)

    publish_date.delete('1.0', 'end')
    publish_date.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.config(state='disabled')
    authors.config(state='disabled')
    publish_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    analysis=TextBlob(article.text)
    sentiment.delete('1.0', "end")
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

root=tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

tlabel=tk.Label(root, text="Title")
tlabel.pack()

title=tk.Text(root, height=2, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel=tk.Label(root, text="Authors")
alabel.pack()

authors=tk.Text(root, height=2, width=140)
authors.config(state="disabled", bg="#dddddd")
authors.pack()

plabel=tk.Label(root, text="Publication Date")
plabel.pack()

publish_date=tk.Text(root, height=2, width=140)
publish_date.config(state="disabled", bg="#dddddd")
publish_date.pack()

slabel=tk.Label(root, text="Summary")
slabel.pack()

summary=tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel=tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment=tk.Text(root, height=2, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

uelabel=tk.Label(root, text="Enter URL")
uelabel.pack()

utext=tk.Text(root, height=2, width=140)
utext.config(state="normal", bg="#dddddd")
utext.pack()

btn=tk.Button(root, text='Summarize',command=summarize)
btn.pack()

root.mainloop()