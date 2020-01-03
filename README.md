> Last updated: 3rd January 2020

---

# lol-data-scraper
As of right now the github contains:
- Web scapper for creating a csv file with all champion stats (Base health, health regen, mana, ad, etc..)

I have also added a `data/` folder that contains the most recent execution i have done personally for people who just want the dataset.

### Champion statistics scrapper
The python script called `champion-stats.py` contains the necessary code for creating a csv file that contains all of the champion statistics. The script requires `bs4` (BeautifulSoup, for parsing html) and `requests` (for web requests). This script also relies on the wikipedia page being up to date. To launch the scrapping clone the repository and type:

```bash
> python3 champion-stats.py [produced-file-name.csv]
```

You can choose the name of the produced csv file by passing a name in parameter (a name is required.)

A file is then created and you can manipulate it however you like. Have fun !

### Future

I will be adding a web scrapper for all items in league of legends in the near future. My ultimate goal is to be able to produce some statistics and tools for getting insights for the game. These insights will most likely be available of a jupyter notebook.

I will also be looking into getting a API Key for the official Riot Games API.

Thanks and have a nice day :)
