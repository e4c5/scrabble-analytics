import requests
import time
import random

def scrape_pages(start, end):
    for i in range(start, end+1):
        url = f"https://www.wespa.org/aardvark/html/tournaments/{i}.html"
        response = requests.get(url, verify=False)
        
        # Save the content to a file
        with open(f"data/tournaments_{i}.html", "w") as file:
            file.write(response.text)
        
        print(f"Scraped page {i}")
        
        # Sleep for a random interval between 30 and 60 seconds
        time.sleep(random.randint(30, 60))


if __name__ == '__main__':
    scrape_pages(1, 1033)
