# EECE5643_Research_Project
Epidemiology Simulation of COVID-19

1) webscraping script used to implement real COVID-19 data into our MATLAB simulation. <br> 
2) matlab script that visualizes and runs a COVID-19 simulation <br> 

*Work in Progress* <br>
Currently uses the CDC data tracker's status bar 3rd party call to grab the total number of cases, the total number of deaths, and the total number of vaccines administered at the time the script is run. It then gets the current date and time, and writes all the grabbed data into a csv file. 


Would recommend creating a virtualenvironment for this. 

To run: <br> 

1) Download required libraries: <br> 

```
python -m pip install -r requirements 
```

<br> 
2)  <br>

```
python webscrape.py
```

<br> 
3) Run MATLAB script: <br>

One method: Open 'CovidSimulation.m' file in MATLAB window --> hit the Run button 
<br>  

Other method: Using Linux command line (with MATLAB program downloaded) <br> 

```
matlab.exe -r "run('CovidSimulation.m');" 
```

