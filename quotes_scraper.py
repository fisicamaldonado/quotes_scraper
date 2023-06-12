# -*- coding: utf-8 -*-
"""
Web Scraping and Word Count Analysis

quotes_scraper.py scrapes quotes from a website, calculates the average word count for each author,
and generates a table and histogram based on the word counts.

Author: Pablo Vaz
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


def scrape_quotes(url):
    """
    Scrape quotes from the specified URL.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list: A list of BeautifulSoup elements representing the quotes.
    """
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    return quotes


def calculate_word_counts(quotes):
    """
    Calculate the average word count for each author.

    Args:
        quotes (list): A list of BeautifulSoup elements representing the quotes.

    Returns:
        dict: A dictionary containing the average word count for each author.
    """
    word_counts = {}
    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        word_count = len(text.split())

        if author in word_counts:
            word_counts[author][0] += word_count
            word_counts[author][1] += 1
        else:
            word_counts[author] = [word_count, 1]

    for author, counts in word_counts.items():
        total_words = counts[0]
        num_quotes = counts[1]
        average_words = round(total_words / num_quotes)
        word_counts[author] = average_words

    return word_counts


def generate_table_and_histogram(word_counts):
    """
    Generate a table and histogram based on the word counts.

    Args:
        word_counts (dict): A dictionary containing the average word count for each author.
    """
    words_df = pd.DataFrame(list(word_counts.items()), columns=['Author', 'Word Count'])
    title = "Number of words in quotes by author"

    print(title)
    print(words_df.to_string(index=False))
    #Store the dataset in CSV file (this is optional)
    #df.to_csv('quotes.csv', index=False)

    plt.bar(words_df['Author'], words_df['Word Count'])
    plt.xticks(rotation=30)
    plt.xlabel('Author')
    plt.ylabel('Number of Words')
    plt.title(title)
    plt.tight_layout()
    plt.show()


# Main execution
URL = 'http://quotes.toscrape.com/'
url_quotes = scrape_quotes(URL)
quotes_word_counts = calculate_word_counts(url_quotes)
generate_table_and_histogram(quotes_word_counts)
