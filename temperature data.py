import numpy as np 
#weather analysis using numpy
#task is to analyse temperature data for local weather station 

#last_week temperature
last_week=np.array([20,21,30,22,23,22,25])
days=np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])

#1. average temperature 
average=np.mean(last_week)
print("Average temperature:",average)

#2. temperature extremes.hottest and coldest temperature
hottest=np.max(last_week)
print("Hottest temperature:",hottest)

coldest=np.min(last_week)
print("coldest temperature:",coldest)

#3. temperature difference
temperature_difference=hottest-coldest
print("Temperature range:",temperature_difference)

#4. day-by-day differnce
daily_diff=np.diff(last_week)
print("Daily differences:",daily_diff)

#5 temperature above average, also print the days 
above_avg_days=last_week> average
print("temperature above average:",last_week[above_avg_days])

print("Days above Average temperature:",days[above_avg_days])

#6 sorted temperatures

sorted_temps=np.sort(last_week)
print("Sorted Temperture:",sorted_temps)

#7. Day with Hottest and Coldest Temperature
hottest_day=days[np.argmax(last_week)]
print("Hottest day is:",hottest_day)

coldest_day=days[np.argmin(last_week)]
print("coldest  day is:",coldest_day)



