from bs4 import BeautifulSoup
import requests

def main(): 
    url = "https://covid.cdc.gov/covid-data-tracker/#datatracker-home"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    # Steven wants: Total Vaccines Administered, Total Infections, and Total Deaths



    out_divs = soup.find_all(id='status-bar')
    for out_div in out_divs: 
        cases = soup.find('div', id="status-cases-total")
        vac_admin = soup.find('div', id="status-total-vaccines")
        deaths = soup.find('div',id="status-deaths-total")
    print(f"deaths: {str(deaths)}\n cases: {str(cases)}\n vaccines administered: {str(vac_admin)}\n")


if __name__ == "__main__": 
    main()    
