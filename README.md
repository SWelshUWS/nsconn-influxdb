# nsconn-influxdb
script to send data from nsconn to influxdb

# usage
ensure influxdb is supported in python: \
pip install influxdb \
or \
sudo apt-get install python-influxdb \

connect.py should be edited to include your own credentials. A database named 'nsconn' should be created prior to use.\
Start nsconn with network output using nsconn -n and simply run connect.py once nsconn is listening.
