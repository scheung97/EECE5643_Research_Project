from bs4 import BeautifulSoup 
import requests

def main(): 
    url = "https://www.nytimes.com/interactive/2021/us/massachusetts-covid-cases.html"
    r = requests.get(url)
    # print(r.text)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.get_text())

if __name__ == "__main__": 
    main()    