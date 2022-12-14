from bs4 import BeautifulSoup, element
import urllib
import pandas as pd
import numpy as np

pages = 19
rec_count = 0
rank = []
gname = []
platform = []
year = []
genre = []
publisher = []
sales_na = []
sales_eu = []
sales_jp = []
sales_ot = []

urlhead = 'http://www.vgchartz.com/gamedb/?page='
urltail = '&console=&region=All&developer=&publisher=&genre=&boxart=Both&ownership=Both'
urltail += '&results=1000&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0'
urltail += '&showpublisher=1&showvgchartzscore=0&shownasales=1&showdeveloper=1&showcriticscore=1'
urltail += '&showpalsales=0&showpalsales=1&showreleasedate=1&showuserscore=1&showjapansales=1'
urltail += '&showlastupdate=0&showothersales=1&showgenre=1&sort=GL'

for page in range(1, pages):
    surl = urlhead + str(page) + urltail
    r = urllib.request.urlopen(surl).read()
    soup = BeautifulSoup(r)
    print(f"Page: {page}")

    # search for <a> tags with game urls
    game_tags = list(filter(
        lambda x: 'href' in x.attrs and x.attrs['href'].startswith('https://www.vgchartz.com/game/'),
        soup.find_all("a")
    ))

    for tag in game_tags:

        # add name to list
        gname.append(" ".join(tag.string.split()))
        print(f"{rec_count + 1} Fetch data for game {gname[-1]}")

        # get different attributes
        # traverse up the DOM tree
        data = tag.parent.parent.find_all("td")
        rank.append(np.int32(data[0].string))
        platform.append(data[3].find('img').attrs['alt'])
        publisher.append(data[4].string)
        sales_na.append(
            float(data[9].string[:-1]) if
            not data[9].string.startswith("N/A") else np.nan)
        sales_eu.append(
            float(data[10].string[:-1]) if
            not data[10].string.startswith("N/A") else np.nan)
        sales_jp.append(
            float(data[11].string[:-1]) if
            not data[11].string.startswith("N/A") else np.nan)
        sales_ot.append(
            float(data[12].string[:-1]) if
            not data[12].string.startswith("N/A") else np.nan)
        release_year = data[13].string.split()[-1]
        # different format for year
        if release_year.startswith('N/A'):
            year.append('N/A')
        else:
            if int(release_year) >= 80:
                year_to_add = np.int32("19" + release_year)
            else:
                year_to_add = np.int32("20" + release_year)
            year.append(year_to_add)

        # go to every individual website to get genre info
        url_to_game = tag.attrs['href']
        site_raw = urllib.request.urlopen(url_to_game).read()
        sub_soup = BeautifulSoup(site_raw, "html.parser")
        # again, the info box is inconsistent among games so we
        # have to find all the h2 and traverse from that to the genre name
        h2s = sub_soup.find("div", {"id": "gameGenInfoBox"}).find_all('h2')
        # make a temporary tag here to search for the one that contains
        # the word "Genre"
        temp_tag = element.Tag
        for h2 in h2s:
            if h2.string == 'Genre':
                temp_tag = h2
        genre.append(temp_tag.next_sibling.string)

        rec_count += 1

columns = {
    'Rank': rank,
    'Name': gname,
    'Platform': platform,
    'Year': year,
    'Genre': genre,
    'Publisher': publisher,
    'NA_Sales': sales_na,
    'EU_Sales': sales_eu,
    'JP_Sales': sales_jp,
    'Other_Sales': sales_ot,
}
print(rec_count)
df = pd.DataFrame(columns)
print(df.columns)
df = df[[
    'Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher',
    'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]
df.to_csv("vgsales.csv", sep=",", encoding='utf-8', index=False)
