from bs4 import BeautifulSoup
import json

def html_to_json(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Find the player's name
    name = soup.find('a').text

    # Find all the rows in the scores table
    rows = soup.find_all('tr')

    # Extract the opponents and scores
    opponents = []
    scores = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        opponent = cells[1].find('a')['href'].split('/')[-1].split('.')[0]
        score = cells[4].text
        opponents.append(opponent)
        scores.append(score)

    # Create the JSON object
    data = {
        'name': name,
        'opponents': opponents,
        'scores': scores,
        'p12': [],
        'rank': [],
        'newr': [],
        'off': False,
        'seed': 0,
        'old_rating': "0"
    }

    return json.dumps(data, indent=2)

def player_names(html):

    outer_table = soup.find('table')
    for i, row in enumerate(outer_table.find_all('tr', recursive=False)):
        if i % 2 == 1:
            cells = row.find_all('td')
            print(cells[2].text, cells[3].text, cells[8].text, cells[9].text)

    
if __name__ == '__main__':
    with open('data/tournaments_1.html') as fp:
        html = fp.read()
        soup = BeautifulSoup(html, 'html.parser')
        player_names(soup)
