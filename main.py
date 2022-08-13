import requests
import csv
import json
from fake_useragent import UserAgent

# getting access to the site
UserAgent().chrome
response = requests.get(url='https://www.detmir.ru/catalog/index/name/zdorovyj_perekus_pp/', headers={'User-Agent': UserAgent().chrome})

def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

# taking data from a json file
    with open(f'info_{product}.json','w') as file:
        json.dump(reponse.json(), file, indent=4, enscure_asii=False)

    for i in items:
        i_title = i.get('title').strip()
        i_price = i.get('price').strip()
        i_old_price = i.get('old price').strip()
        i_link = i.get('url')

        result.append(
            [i_title, i_old_price, i_price, i_link]

        )
    # Creating and writing to a csv file
    with open({product}.csv, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            'title',
            'old_price',
            'price',
            'url'
        )
        writer.writerows(
            i_title,
            i_old_price
            i_price,
            i_link
        )

if __name__=='__main__':
    main()
