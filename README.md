# nsconn-influxdb.py
script to send data from nsconn to influxdb

## usage
ensure influxdb is supported in python: \
pip install influxdb \
or \
sudo apt-get install python-influxdb \

nsconn-influxdb.py should be edited to include your own credentials. A database named 'nsconn' should be created prior to use.\
Start nsconn with network output using nsconn -n and simply run nsconn-influxdb.py once nsconn is listening.

##*** IMPORTANT! ***
before using this script, make sure raw wave output has been disabled on nsconn with the -d option - Python is too slow to handle the volume of data produced by this metric (Give it a go and see what I mean...). I'll rewrite this in C at some point to speed things up and allow for real time raw wave data.
