# Paranneltu ja päivitetty versio RSS tutoriaalista.
# Mm. sivuston osoite muuttunut jossain vaiheessa ja viikonlopun käsittely nyt hoidettu.
# Tee komento pip install feedparser, mutta datetime kuuluu Pythoniin muutenkin.
# Jos käyttää noita värillisiä tulosteita niin pip install termcolor

import feedparser
import datetime
from termcolor import colored

url = "https://menu.arkea.fi/AromieMenus/FI/Default/Arkea/KERTTUL/Rss.aspx?Id=d49df877-d242-4ec5-91cb-30ace62c8dd5&DateMode=2"

feed = feedparser.parse(url)

day = datetime.datetime.today().weekday()

weekdays = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
print('\n')
print(colored('********************************************************************', 'yellow'))
print(colored('******************* R U O K A L I S T A ****************************', 'yellow'))
print(colored('********************************************************************', 'yellow'))

# ohjelma hakee ruoan vain jos ei ole viikonloppu
if(day < 5):
    print(f'Nyt on {weekdays[day]}')

    food = feed.entries[day].summary_detail.value
    
    mainfood = food.split('<br />')[0]
    vegefood = food.split('<br />')[1]

    print(mainfood)
    print(colored(vegefood, 'green'))
    
else:
    print(f'Nyt on {weekdays[day]}. Ruokaa ei tarjoilla viikonloppuisin')
    



