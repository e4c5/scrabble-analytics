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

def get_results(soup, players):
    outer_table = soup.find('table')

    player = None
    for i, results in enumerate(outer_table.find_all('tr', recursive=False)):
        inner = results.find('table')
        if inner:
            for j, row in enumerate(inner.find_all('tr')):
                if j > 0:
                    cells = row.find_all('td')
                    name = cells[1].text.strip()
                    if name != 'Average:':
                        opponent = players[name]
                        score = int(cells[4].text)
                        players[player]['scores'].append(score)
                        players[player]['opponents'].append(opponent)
        else:
            cells = results.find_all('td')
            if cells:
                player = cells[3].text.strip()

def get_player_names(soup):
    """
    This function prints the names of players from a HTML string.
    It finds an outer table in the HTML, then iterates over every second row in this table 


    Args:
        soup (beautifulsoup): The HTML converted to beautiful soup

    Returns:
        players : a dictionary of player info

    """

    # Find the outer table in the HTML
    outer_table = soup.find('table')

    players = {}
    for i, row in enumerate(outer_table.find_all('tr', recursive=False)):

        if i % 2 == 1:
            # Find all the cells in this row
            cells = row.find_all('td')
            players[cells[3].text.strip()] = {
                'seed': int(cells[2].text), 'scores' : [],
                'opponents' : [],
                'old': int(cells[8].text), 'new' : int(cells[9].text)
            }
            
    return players

if __name__ == '__main__':
    with open('wespa/data/tournaments_1.html') as fp:
        html = fp.read()
        soup = BeautifulSoup(html, 'html.parser')
        names = get_player_names(soup)
        get_results(soup, names)
        print(names)