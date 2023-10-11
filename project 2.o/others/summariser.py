import tkinter as tk
from tkinter import scrolledtext
import requests
from gensim import summariser
from bs4 import BeautifulSoup

def summarize_website():
    url = url_entry.get()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        summary = summariser(text, ratio=0.2)  # Adjust the ratio for shorter or longer summaries
        summary_text.delete('1.0', tk.END)  # Clear previous text
        summary_text.insert(tk.END, summary)
    except Exception as e:
        summary_text.delete('1.0', tk.END)
        summary_text.insert(tk.END, f"Error: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Website Summarizer")
window.geometry("300x400")

# Create a label and entry for the URL
url_label = tk.Label(window, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a button to trigger summarization
summarize_button = tk.Button(window, text="Summarize", command=summarize_website)
summarize_button.pack()

# Create a scrolled text widget for the summary
summary_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
summary_text.pack()

# Start the Tkinter main loop
window.mainloop()
