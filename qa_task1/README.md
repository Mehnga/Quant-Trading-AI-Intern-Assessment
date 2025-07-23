# Quantitative Developer GitHub Scraper

## Brief Summary of Approach
This project is a Python script that searches GitHub for repositories related to quantitative development using specific keywords and filters. It identifies developers who have contributed to popular Python or C++ repositories in the quant domain, aggregates their repository and star counts, and saves the qualified developer information to a CSV file (`developers.csv`) in the same directory as the script. The script uses the GitHub API and the `requests` library for data retrieval.

## Major Challenge Faced
The main challenge was handling the GitHub API's search limitations, such as rate limits and the restriction on the number of results returned per query. This required careful query construction and efficient filtering to ensure relevant and high-quality developer data was collected without exceeding API limits.

## One Improvement I'd Make if Hired
If hired, I would enhance the script to support pagination and more advanced keyword/language filtering, allowing for a more comprehensive and customizable search. Additionally, I would implement error handling for API failures and add logging to make the script more robust and production-ready. 