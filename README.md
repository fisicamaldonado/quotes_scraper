# Web Scraping and Word Count Analysis

This script quotes_scraper.py scrapes quotes from a website, calculates the average word count for each author, and generates a table and histogram based on the word counts.

It's is based on the Scrapy project tutorial you can find here: [Scrapy Tutorial](https://github.com/fisicamaldonado/quotesbot)

![quotes_authors](img/quotes_authors.png)

## Dependencies
The following dependencies are required to run the script:

- Python 3.x
- BeautifulSoup (beautifulsoup4)
- Requests (requests)
- pandas (pandas)
- matplotlib (matplotlib)

## Usage
1. Install the required dependencies by running the following command:

```
pip install bs4 requests pandas matplotlib
```

2. Save the script as quotes_scraper.py.

3. Run the script using the following command:

```
python quotes_scraper.py
```

## Output
The script will display the table with the average word count for each author and generate a histogram to visualize the word counts. The table will be printed in the console, and the histogram will be displayed as a plot.

![quotes_table](img/quotes_table.png)

![quotes_histogram](img/quotes_histogram.png)

The script starts by defining the scrape_quotes function, which takes a URL as input and uses the requests library to retrieve the HTML content of the webpage. It then uses BeautifulSoup to parse the HTML and extract the quotes. The function returns a list of BeautifulSoup elements representing the quotes.

The calculate_word_counts function takes the list of quotes as input and calculates the average word count for each author. It iterates over the quotes, extracts the text and author information, and counts the number of words. The word counts are stored in a dictionary, where the keys are the authors and the values are lists containing the total word count and the number of quotes by that author. The function then calculates the average word count for each author and updates the dictionary accordingly. Finally, it returns the word counts dictionary.

The generate_table_and_histogram function takes the word counts dictionary as input. It creates a pandas DataFrame from the dictionary and formats it as a table. The table is printed in the console. The function then generates a histogram using matplotlib, plotting the authors on the x-axis and the average word counts on the y-axis. The plot is displayed using plt.show().
