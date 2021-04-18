import json
import requests
import csv
import datetime 
import pytz

def main(): 

  #################################################################################################################################################################################################################################################################
  #   DATA ACQUISITION:
  #################################################################################################################################################################################################################################################################
  
  url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=statusBar_external_data"
  r = requests.get(url)
  res = json.loads(r.text) #get status bar data
  stat_bar = res['statusBar'][0] #we want the values inside of the 'statusBar'

  #total data: 
  tot_cases = stat_bar['us_total_cases']
  tot_deaths = stat_bar['us_total_deaths']
  tot_vaccines_administered = stat_bar['Administered_US']

  #gets current time and date 
  now = datetime.datetime.now(datetime.timezone.utc) #get date and time of run 
  now = now.astimezone(pytz.timezone('US/Eastern')) #set time to be EST instead of GMT
  now = now.strftime("%m/%d/%Y %H:%M:%S") #convert datetime obj to a string
  now = now.split(" ") #split date and time into their own strings
  date = now[0]
  time = now[1]

  #Calculated data: 

  #death_rate: 
  death_rate = (tot_deaths/tot_cases) #multiply by 100 for death_rate percentage 
  
  #infection rate: 
  seven_days_cases = stat_bar['cases-7-day']
  cases_end_of_yesterday = tot_cases - seven_days_cases[1][0]
  cases_two_days_ago = cases_end_of_yesterday - seven_days_cases[2][0]

  num_infections_per_day = cases_end_of_yesterday - cases_two_days_ago 
  pop_at_risk = 330425184 - tot_cases                                       #Assuming that people can't get re-infected: US Population - tot_cases = population@risk
  infect_rate = num_infections_per_day / pop_at_risk

  #################################################################################################################################################################################################################################################################
  #    FILE WORK :
  #################################################################################################################################################################################################################################################################

  file_name = 'covid_data.csv'   #file name that you want to write data to 

  try: 
    #if file_name already exists, we append the new data 
    with open(file_name, mode = 'r') as csv_file:  #try opening file in "read mode". will not work if file doesn't exist
      csvfile = open(file_name, 'a') #if we have the file, we put it in append_mode
      fieldnames = ['date', 'time', 'total_cases', 'total_deaths', 'total administered vaccines', 'infection rate', 'death rate']
      writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

      writer.writerow({'date': date, 'time': time, 'total_cases': tot_cases, 'total_deaths': tot_deaths, 'total administered vaccines': tot_vaccines_administered, 'infection rate': infect_rate, 'death rate': death_rate})
      csvfile.close()

  except: 
    #if file_name doesn't aleady exist, we create it
    new_file = open(file_name, mode = 'w') 
    
    fieldnames = ['date', 'time', 'total_cases', 'total_deaths', 'total administered vaccines', 'infection rate', 'death rate']
    writer = csv.DictWriter(new_file, fieldnames = fieldnames)

    writer.writeheader()  #writes the field names at the top
    writer.writerow({'date': date, 'time': time, 'total_cases': tot_cases, 'total_deaths': tot_deaths, 'total administered vaccines': tot_vaccines_administered, 'infection rate': infect_rate, 'death rate': death_rate})
    new_file.close()

  print(f"Published data to CSV file: \n\n total cases: {tot_cases}\n total deaths: {tot_deaths}\n total number of vaccines administered: {tot_vaccines_administered}\n infection rate: {infect_rate}\n death rate: {death_rate}\n ")

if __name__ == "__main__": 
    main()    
