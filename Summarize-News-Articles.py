import tkinter as tk
from datetime import datetime
from newspaper import Article
import nltk
from textblob import TextBlob


def summarize():
    # Fetch the target URL from the entry textbox
    url = utext.get('1.0', "end").strip()

    # Download, parse, and process the article content via NLP
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Temporarily unlock all output boxes so python can insert data
    authors.config(state='normal')
    title.config(state='normal')
    publish_date.config(state='normal')
    sentiment.config(state='normal')
    summary.config(state='normal')
    
    # Clear old data and insert freshly scraped metadata
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors.delete('1.0', 'end')
    authors.insert('1.0', ", ".join(article.authors) if article.authors else "Unknown")

    publish_date.delete('1.0', 'end')
    if article.publish_date:
        publish_date.insert('1.0', str(article.publish_date))
    else:
        publish_date.insert('1.0', "N/A")

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Perform Lexicon-based Sentiment Analysis using TextBlob
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', "end")
    
    # Calculate polarity score and assign a human-readable label
    polarity = analysis.polarity
    sentiment_label = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    sentiment.insert('1.0', f'Polarity: {polarity:.2f}, Sentiment: {sentiment_label}')

    # Re-lock all output fields to make them read-only for the user
    title.config(state='disabled')
    authors.config(state='disabled')
    publish_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# ==================

root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

# --- Component Elements (Labels & Text Fields) ---

# Article Title Field
tlabel = tk.Label(root, text="Title", font=("Helvetica", 10, "bold"))
tlabel.pack()
title = tk.Text(root, height=2, width=140, state="disabled", bg="#dddddd")
title.pack(pady=2)

# Authors Field
alabel = tk.Label(root, text="Authors", font=("Helvetica", 10, "bold"))
alabel.pack()
authors = tk.Text(root, height=2, width=140, state="disabled", bg="#dddddd")
authors.pack(pady=2)

# Publication Date Field
plabel = tk.Label(root, text="Publication Date", font=("Helvetica", 10, "bold"))
plabel.pack()
publish_date = tk.Text(root, height=2, width=140, state="disabled", bg="#dddddd")
publish_date.pack(pady=2)

# AI Summary Field
slabel = tk.Label(root, text="Summary", font=("Helvetica", 10, "bold"))
slabel.pack()
summary = tk.Text(root, height=15, width=140, state="disabled", bg="#dddddd")
summary.pack(pady=2)

# Sentiment Metrics Field
selabel = tk.Label(root, text="Sentiment Analysis", font=("Helvetica", 10, "bold"))
selabel.pack()
sentiment = tk.Text(root, height=2, width=140, state="disabled", bg="#dddddd")
sentiment.pack(pady=2)

# User URL Entry Field
uelabel = tk.Label(root, text="Enter URL Below:", font=("Helvetica", 11, "bold"), fg="blue")
uelabel.pack(pady=(10, 0))
utext = tk.Text(root, height=2, width=140, state="normal", bg="#ffffff", relief="sunken")
utext.pack(pady=2)

# Action Trigger Button
btn = tk.Button(root, text='Summarize Article', command=summarize, bg="#4CAF50", fg="black", font=("Helvetica", 10, "bold"))
btn.pack(pady=10)

# Start the application loop
root.mainloop()
