import requests
from bs4 import BeautifulSoup
from collections import Counter
import string
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
import datetime

# Example usage
# The script only works if all the links in urls.txt are from the same website,
# per example, all links are from https://www.vagas.com.br/ or https://www.gupy.io or https://www.indeed.com.br.....
# Find the html tags by inspecting the website youre trying to scrape.

# urls file name:
file_path = "urls.txt"

def ask_user_input():
    """
    Creates a simple GUI to ask the user for start_tag, end_tag, and number of most common words.
    Returns:
        tuple: A tuple containing the start_tag, end_tag, and number of most common words.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.title("Keyword Finder")  # Set the title of the window

    start_tag = simpledialog.askstring("Input", "Enter start tag:", parent=root)
    end_tag = simpledialog.askstring("Input", "Enter end tag:", parent=root)
    num_words = simpledialog.askinteger("Input", "Enter the number of most common words:", parent=root)

    return start_tag, end_tag, num_words

def get_time_since_last_modification(file_path):
    last_modified_time = os.path.getmtime(file_path)
    last_modified_date = datetime.datetime.fromtimestamp(last_modified_time)
    current_time = datetime.datetime.now()
    time_diff = current_time - last_modified_date
    return time_diff.days  # Returns the time difference in days

def show_file_age_warning(file_path):
    days_old = get_time_since_last_modification(file_path)
    message = f"Please always use new links, as they expire very fast. \nThis url was updated {days_old} days ago"
    if days_old != 0:  # If the file is older than 0 days, show the warning
        tk.messagebox.showinfo("File Age Warning", message)

def read_urls_from_file(file_path):
    """
    Reads URLs from a file, with one URL per line.
    
    Args:
    file_path (str): The path to the file containing URLs.

    Returns:
    list: A list of URLs.
    """
    with open(file_path, 'r') as file:
        # Read each line and strip whitespace, ignore empty lines
        urls = [line.strip() for line in file if line.strip()]
    return urls

def extract_section(soup):
    """
    Extracts text content from a specified section of a BeautifulSoup object.
    The section starts from the first <h2> tag and ends at the next <li> tag.
    
    Args:
    soup (BeautifulSoup): BeautifulSoup object of the webpage content.

    Returns:
    str: Extracted text content from the specified section.
    """
    content = [] 
    start_element = soup.find(start_tag)  # Find the first <h2> tag
    
    if start_element:
        # Loop through siblings of <h2> until <li> is encountered
        for sibling in start_element.next_siblings:
            if sibling.name == end_tag:  # Stop at the next <li> tag
                break
            if sibling.name:
                # Append text of the sibling element
                content.append(sibling.get_text(strip=True))
    
    return ' '.join(content)

def get_text_from_url(url):
    """
    Fetches the content of a webpage and extracts text from a specific section.

    Args:
    url (str): URL of the webpage to fetch.

    Returns:
    str: Extracted text content from the webpage.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text from a specific section
        section_text = extract_section(soup)
        return section_text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

Filter_words = ['região', 'ensino', 'técnica', 'técnico', 'atividades', 'será', 'novos', 'como',
                'sua', 'suas', 'será', 'está', 'outro', 'outros', 'nível', 'visando', 'garantir', 'atuação',
                'realizar','para', 'pela', 'seus', 'superior', 'completo', 'junto', 'através', 'acordo',
                'áreas', 'residir', 'disponibilidade', 'visitas', 'requisitos', 'sejam', 'melhor', 'objetivos',
                'habilidades', 'ferramentas', 'entregas', 'contribuir', 'dúvidas', 'sobre']

def clean_and_split_text(text):
    """
    Cleans and splits text into words. Filters out punctuation and words with less than 4 letters.

    Args:
    text (str): Text to be cleaned and split.

    Returns:
    list: List of cleaned and filtered words.
    """
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    # Filter out words with less than 4 letters
    words = [word for word in words if len(word) >= 4 ]
    words = [word for word in words if not word in Filter_words]
    return words

def get_most_common_words(urls, num_words=10):
    """
    Determines the most common words across multiple webpages.

    Args:
    urls (list): List of URLs to analyze.
    num_words (int): Number of top common words to return.

    Returns:
    list: A list of tuples with the most common words and their frequencies.
    """
    all_words = []
    for url in urls:
        # Get text from each URL and split into words
        text = get_text_from_url(url)
        words = clean_and_split_text(text)
        all_words.extend(words)

    # Count the frequency of each word
    word_counts = Counter(all_words)
    # Return the most common words and their counts
    return word_counts.most_common(num_words)



def plot_word_frequencies(word_counts):
    """
    Plots the word frequencies using a horizontal bar chart.

    Args:
    word_counts (list): A list of tuples with words and their frequencies.
    """
    # Unpacking words and their counts
    words, counts = zip(*word_counts)

    # Creating the horizontal bar plot
    plt.figure(figsize=(10, 8))
    y_pos = range(len(words))
    plt.barh(y_pos, counts, color='skyblue')
    plt.yticks(y_pos, words)
    plt.gca().invert_yaxis()  # Invert y-axis to have the most frequent word on top
    plt.xlabel('Frequency')
    plt.title('Word Frequency')

    # Adding the counts at the end of each bar
    for index, value in enumerate(counts):
        plt.text(value, index, f' {value}')

    plt.show()


# Main part of your script
if __name__ == "__main__":
    file_path = "urls.txt"

    show_file_age_warning(file_path)

    start_tag, end_tag, num_words = ask_user_input()

    urls = read_urls_from_file(file_path)
    most_common_words = get_most_common_words(urls, num_words)
    plot_word_frequencies(most_common_words)