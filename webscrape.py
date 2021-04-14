import json
import requests
import csv
import datetime 
import pytz

def main(): 
    url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=statusBar_external_data"
    r = requests.get(url)
    res = json.loads(r.text) #get status bar data
    res = res['statusBar'][0] #we want the values inside of the 'statusBar'
    tot_cases = res['us_total_cases']
    tot_deaths = res['us_total_deaths']
    tot_vaccines_administered = res['Administered_US']

    #gets current time and date 
    now = datetime.datetime.now(datetime.timezone.utc) #get date and time of run 
    now = now.astimezone(pytz.timezone('US/Eastern')) #set time to be EST instead of GMT
    now = now.strftime("%m/%d/%Y %H:%M:%S") #convert datetime obj to a string
    now = now.split(" ") #split date and time into their own strings
    date = now[0]
    time = now[1]

    with open('covid_data.csv', mode = 'w') as csv_file: 
      fieldnames = ['date', 'time', 'cases', 'deaths', 'administered vaccines']
      writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

      writer.writeheader()  #writes the field names at the top
      writer.writerow({'date': date, 'time': time, 'cases': tot_cases, 'deaths': tot_deaths, 'administered vaccines': tot_vaccines_administered})

    print(f"Published data to CSV file: \n\n deaths: {tot_deaths}\n cases: {tot_cases}\n vaccines administered: {tot_vaccines_administered}\n")

if __name__ == "__main__": 
    main()    
