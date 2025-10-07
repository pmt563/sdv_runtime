./mosquitto/config:/mosquitto/config: This mounts a local configuration directory, allowing a custom mosquitto.conf file to be provided to the container.  

./mosquitto/data:/mosquitto/data: This volume is used for data persistence. Mosquitto will store retained messages and persistent session information here, ensuring this data survives container restarts.  

./mosquitto/log:/mosquitto/log: This volume captures the broker's log files, making them easily accessible on the host machine for debugging. 