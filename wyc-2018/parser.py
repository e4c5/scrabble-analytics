from bs4 import BeautifulSoup
import requests
import csv

with open('results.csv','w') as f:
    writer = csv.writer(f)
    for round_no in range(1,25):
        url = 'http://youthscrabble.org/wyc2018/results/a{0:02d}.html'.format(round_no)
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        for row in soup.table.find_all('tr')[1:]:
            cells = [round_no]
            cells.extend([cell.get_text() for i, cell in enumerate(row.find_all('td')) if i in (0,1,2,3,6,7)])
            try:
                score = cells[-1].split(":")
                cells[-1] = score[0]
                cells.append(score[1])
                if score[0] > score[1]:
                    cells.append('1')
                elif score[0] == score[1]:
                    cells.append('0.5')
                else:
                    cells.append('0')
            except IndexError:
                print('Walkover?')
                cells[-1] = 0
                cells.extend([100, 0])

            cells.append(cells[2][0:2])
            cells[2] = cells[2][3:]
            cells[5] = cells[5][3:]
                            
            writer.writerow(cells)
            