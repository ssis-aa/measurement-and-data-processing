# Analyzing light sensor data from a fan

The setup is rather simple: A light sensor (photoresistor on Metro express or phototransistor on Circuitpython Express) reads analog values in front of a spinning fan. We collect the raw values for 2 seconds and analyse the `csv` file.

Some example tasks:

## Thresholded data

This REPL link has a CSV file of thresholded values that are 0 and 1 depending on whether or not a blade is in front of the light sensor. Edit the code so that whenever the light value transitions from 1 to 0, the blade count goes up by 1.

- https://replit.com/@evanweinberg/Fan-Data-Analyzer-Thresholded-Data#main.py
- https://replit.com/@kreier/Fan-Data-Analyzer-Thresholded-Data-2023-with-students#main.py

## Raw data

This second one is similar, but it has a CSV of raw light sensor data that has not been thresholded. You need to add a step that does the threshold step, and then paste your thresholded processing code from the previous step.

- https://replit.com/@evanweinberg/Fan-Data-Analyzer-Raw-Data
- https://replit.com/@kreier/Fan-Data-Analyzer-Raw-Data-2023-with-students#main.py

