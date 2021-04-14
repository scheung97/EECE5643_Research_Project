# EECE5643_Research_Project
Epidemiology Simulation of COVID-19

webscraping script used to implement real COVID-19 data into our MATLAB simulation. 

*Work in Progress*
Currently uses the CDC data tracker's status bar 3rd party call to grab the total number of cases, the total number of deaths, and the total number of vaccines administered at the time the script is run. It then gets the current date and time, and writes all the grabbed data into a csv file. 


Would recommend creating a virtualenvironment for this. 

To run: <br> <br> 
    1) Download required libraries: 
        <br> 
        ```
        python -m pip install -r requirements 
        ```
        <br><br> 
    2)  <br>
        ```
        python webscrape.py
        ```
