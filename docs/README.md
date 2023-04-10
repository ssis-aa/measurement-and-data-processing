# Measurement and Data Processing

Unit 6: Measurement and Data Processing

Read a CSV file in Python: https://replit.com/@evanweinberg/CSV-Reader-Pressures 

Introducion lesson [1-1 Intro to Data Processing.pdf](1-1 Intro to Data Processing.pdf)

``` py
import csv

pressures = []
num_of_lines_to_process = 10000
biggestNumber = 0
with open('pressure_partial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')
print(len(pressures))
print(biggestNumber)
print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )
```
