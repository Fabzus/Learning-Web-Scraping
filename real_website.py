from bs4 import BeautifulSoup
import requests as req

query=str(input("Search for remote jobs in what field? :")).replace(" ","-")

html = req.get(f'https://www.bestjobs.eu/ro/locuri-de-munca/{query}')
html_text = html.text

soup = BeautifulSoup(html_text, 'lxml')
cards = soup.find_all('div', class_="card")

for index, card in enumerate(cards):

    try:
        location = card.find_all('a')[1]['aria-label']
    except NameError:
        location = card.find('span',class_='stretched-link-exception text-nowrap overflow-hidden').text
    except KeyError:
        location = card.find('span',class_='stretched-link-exception text-nowrap overflow-hidden').text
    except IndexError:
        pass
    except AttributeError:
        pass

    if location == "De la distanta" :
        try:
            title = card.find('small').text.strip()
        except AttributeError:
            pass
        try:
            link = card.find('a',class_='js-card-link')['href']
        except TypeError:
            pass
        with open(f'posts/{index}.txt', 'w') as f:
            f.write(f"{title} Is offering a remote job for {query.replace('-',' ')}!\nCheck them out!\n{link}")
            print(f"I found something from {title}, check out: {index}.txt")
    else:
        try:
            title = card.find('small').text.strip()
        except AttributeError:
            pass
        print(f"I'm sorry, it seems like {title}, does not have any remote positions avialable")