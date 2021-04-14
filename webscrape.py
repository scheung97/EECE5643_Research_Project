#from bs4 import BeautifulSoup
import json
import requests

def main(): 
    url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=statusBar_external_data"
    r = requests.get(url)
    res = json.loads(r.text)
    res = res['statusBar'][0]
    tot_cases = res['us_total_cases']
    tot_deaths = res['us_total_deaths']
    tot_vaccines_administered = res['Administered_US']
    """
    soup = BeautifulSoup(r.text, 'html.parser')


    # Steven wants: Total Vaccines Administered, Total Infections, and Total Deaths



    out_divs = soup.find_all(id='status-bar')
    for out_div in out_divs: 
        cases = soup.find('div', id="status-cases-total")
        vac_admin = soup.find('div', id="status-total-vaccines")
        deaths = soup.find('div',id="status-deaths-total")
    """
    print(f"deaths: {tot_deaths}\n cases: {tot_cases}\n vaccines administered: {tot_vaccines_administered}\n")



if __name__ == "__main__": 
    main()    
