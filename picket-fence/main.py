# from https://replit.com/@kreier/picket-fence#main.py

import csv

input_file = "picket_fence.csv"
THRESHOLD = 12000
old_light_value = 0
starttime = 0
stoptime = 0
pulsewidth_data = []

with open(input_file) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  # For each row in our data:
  for row in csv_reader:
    # Read the light value as an integer
    light_value_raw = int(row[1])
    if light_value_raw > THRESHOLD:
      light_value = 1
    else:
      light_value = 0

    if (light_value != old_light_value):
      if old_light_value == 0:
        starttime = float(row[0])
        print('_{:.2}_'.format(starttime - stoptime))
      else:
        stoptime = float(row[0])
        pulsewidth = stoptime - starttime
        print(' {:.2} '.format(pulsewidth))
        pulsewidth_data.append(pulsewidth)
    old_light_value = light_value
    line_count += 1

print("\n", line_count, " lines read.")
print(pulsewidth_data)
