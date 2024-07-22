import requests
from bs4 import BeautifulSoup
import csv
import os

#s funkcemi fetch_page  a parse_html mi pomohl kolega 
def fetch_page(page_number):
    url = f'https://www.antikavion.cz/gramodesky?sort_by=popularity_desc&page={page_number}&takeOnlyReleaseComponent=loadComponent'
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'cs-CZ,cs;q=0.9',
        'cookie': '_hjSessionUser_2597778=eyJpZCI6IjYzMWY3NmFkLWEwYjktNTg4Zi1iNGM5LTc1ODkyMjZhNmM1ZCIsImNyZWF0ZWQiOjE3MTc1ODk2MDg2OTksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2597778=eyJpZCI6Ijc1OTU2ZTFmLThkNDQtNDQ2OS05NmIyLTI2YWI0YzI1NjkyNCIsImMiOjE3MTc5MzQ5NzI3MDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; adUserData=granted; adPersonalization=granted; adStorage=granted; adPersonalizationSignals=granted; analyticsStorage=granted; _gcl_au=1.1.219019121.1717936082; _gid=GA1.2.678247376.1717936082; _gat_UA-177431165-1=1; cookiesSeznam=true; cookiesRTB=true; cookiesFacebook=true; sorting=eyJpdiI6IlBFWW5BWHNzYU9xVm5Dc0VscnlVa1E9PSIsInZhbHVlIjoiRFBJcDQrRG4ybTRCRFVHNGhab0pEWWVxV3N5aXZuNEJ6WVU3OHpzVU15emxtbjVjWCtDV2RpcEJPNUNoamJ6dlBGbm9MMXUxMENBMUgrTWFWb3hraEE9PSIsIm1hYyI6ImVkOTYzOWM4Zjg1ZDQ0NzM0ZWM1ZWM0MDZmZmNjNjFhYjcxMzQ0MzQ2NWJkNmNkOTJkNzAxZDlhN2NiNWUwNGIiLCJ0YWciOiIifQ%3D%3D; XSRF-TOKEN=eyJpdiI6Ik1jZi9tNm5HUFJVOGtTbXF1TVZha2c9PSIsInZhbHVlIjoicVBIVmw1OHJkUmYxaTB5b1dycTltZVlZZks3SmVhbXJST1h3UkpYQTZ1bGlmVlhyMFA2QktpUklaUVFKL3VGYWdsakw5YlJCY1lwcnlLL1NWTkVxWjJWdmsyMWJsOUdhMUVZbFJzS0djdWg3U2UzUnE1MTMyYlZSQlVhbHVCbWQiLCJtYWMiOiI4YmU5ZTdjMDBjOWUyMjZlYzdjODMyMzljMzcyYjlmMjc5M2E4NjJiMWM1MTFlOGI2MGQwNjAzMzcwMmQ5MzExIiwidGFnIjoiIn0%3D; antikvariat_avion_session=eyJpdiI6ImROWGlHalFaMkdRR3BBMFNxVHJEZlE9PSIsInZhbHVlIjoiaEVKZXZ4bmllcnN4clVIMzVDSjZrQzd6Z0orVGxYdisvNGx4aVBobUgrcSt3OXVlZjdndExrZGhJa2RmQjMxVlZCOGpGcjJrYm5OYzhnQU40SDRRTDhDZVFmMXNVeEh4RW1nUGN2c1pSZlNnNk5HUE14MWF5ZlFGRTJVbklSWU0iLCJtYWMiOiJmZGFjZjM2MGJiYzc2Mzk0MTEyZDFmNmZkNjYxMDEwMGNlOGFjMDNjOTFmMjU0MTVjY2IyY2EwN2VjODUxYzFmIiwidGFnIjoiIn0%3D; PoTqFkx9q60S3lE6nboMg6ntWhv1v3bJDvNL5RZ9=eyJpdiI6IldPeG9LMG1nR0RyWW9nMEUzUkdQZkE9PSIsInZhbHVlIjoienRuVVo4MVFxU1cvRkhqL0IzOVlPUnFsYnpTTU5VWkR0RGN0UWdZTUk4ak1tYml0NkR6VU94bGNaZ2k3am9ZRG9nK2J5dER0VVF3cHEyU2JVNUpjckQ2SkE3U3Y0aU9saG1LT1dTV0liL2hUT1NBNzNiOXpJM2JhdXYyTnZiY1dGYXJZYXdjbVJTb0gzd3U5WllpQkFCSE04VDlpWndFbkVXTkJVL1dhMlh0elNTOTE2SjlxWEtTa1M3aHFkYTA0cE9KcW5MR0R6aXNlbTc1OTQrN2JPSGF0cEtoMEo0VkpybkxyVW8vczRZSzZVYm5RTEgvQWJOSTdSU1A1RXFjQnpiZks4TVlIR3V4T000NkZhUC93YnN0VjNVbkxUc1ViTzJQbTZVREFmcG0yNURjYTkyTzR4cHZEYkxrWXQ0QWJXMzhoMXlJTHZ0YXVvRC81YlNpRGtGdERuVDlwVklKU3BIRnI0RzZyMlJjMCtraEtkeE5PK3VzWHpNdWpHWENoUGh5WjBvNjVGWVZoRkNkLzdDajF4T1J2MGhvcTh3M09SeVViU2I2TDNONkNBSElFT0hsclZzbkxaQUFOekNzR2pMY2NVYzlSUjN6aTBrVThLMnFvWmc9PSIsIm1hYyI6ImI1ZTkyOGI5MWEwZGIzNzQwYzRiZjkzNjY1NTY5NzJkMzc5OTBhOThlOTU3ZTZhMjc3M2JhOTQ3MTQ1NzRhODciLCJ0YWciOiIifQ%3D%3D',
        'priority': 'u=1, i',
        'referer': 'https://www.antikavion.cz/gramodesky',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
 
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None
 
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    records = soup.find_all('div', class_='bigDaddyDiv')
 
    results = []
    for record in records:
        record_div = soup.find('div', class_='col-xl-7 col-12 px-1 px-lg-2 float-left overcard botdiv-container zpindex')
        year_and_publisher_div = record_div.find('div')
        year_text = year_and_publisher_div.contents[0].strip()  
        publisher_a_tag = year_and_publisher_div.find('a')
        publisher_text = publisher_a_tag.get_text(strip=True) 
        publisher_link = publisher_a_tag['href'] 
        title = record.find('h2', class_='text-size').get_text(strip=True)
        author = record.find('h3', class_='author-size').get_text(strip=True)
        price = record.find('span', id='book_price').get_text(strip=True)
        year = year_text.split(" |")[0]
        publisher = publisher_text
        details_link = record.find('a', href=True)['href']
        image = record.find('img', class_="img-centered")['src']
        
        results.append({
            'Title': title,
            'Author': author,
            'Year': year,
            'Publisher': publisher,
            'Price': price,
            'Image': image,
            'Link': details_link,
        })
 
    return results
 
def save_to_csv(data, filename='gramodesky.csv'):
    directory = os.path.dirname(__file__) #oprava relativni cesty
    file_path = os.path.join(directory,"datas",filename)
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
 
def main():
    all_records = []
    page_number = 1
 
    while page_number<20:
        print(f"Fetching page {page_number}")
        page_data = fetch_page(page_number)
        if not page_data:
            break
 
        html_content = page_data.get('html')
        if not html_content:
            break
 
        records = parse_html(html_content)
        if not records:
            break
 
        all_records.extend(records)
        page_number += 1
 
    if all_records:
        save_to_csv(all_records)
        print(f"Saved {len(all_records)} records to gramodesky.csv")
    else:
        print("No records found.")
 
if __name__ == "__main__":
    main()