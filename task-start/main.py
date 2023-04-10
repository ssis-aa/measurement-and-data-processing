import csv

pressures = []
num_of_lines_to_process = 10000
biggestNumber = 0
smallestNumber = 0
with open('pressure_partial.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print(f'Column names are: {", ".join(row)}')
      line_count += 1
            
    else:
      #Set biggest number to the first row of data
      if(line_count == 1):
        biggestNumber = float(row[1])
        smallestNumber = float(row[1])
        pressures.append([row[1],row[3]])
        pressures.append([row[1],row[3]])

      # If the current value of the data is bigger than the previous 
      # biggestNumber, set biggestNumber equal to the new data value.
      if(biggestNumber < float(row[1])):
        biggestNumber = float(row[1])
        pressures[1][0] = row[1]
        pressures[1][1] = row[3]

      if(smallestNumber > float(row[1])):
        smallestNumber = float(row[1])
        pressures[0][0] = row[1]
        pressures[0][1] = row[3]
        
      line_count += 1

print(f'Processed {line_count} lines.')
print(f'The smallest pressure is {smallestNumber} hPa.')
print(f'It was measured {pressures[0][0]} hPa at {pressures[0][1]}.' )
print(f'The biggest pressure is {biggestNumber} hPa.')
print(f'It was measured {pressures[1][0]} hPa at {pressures[1][1]}.' )
