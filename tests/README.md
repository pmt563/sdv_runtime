1. Synchronization Bridge test: A program that subscribing to sensor VSS (Vehicle.Speed), if have change change send a request change "set" actuator Vehicle...Driver.Position change = current value + 1. Publish any changed value to MQTT broker (Mosquitto).
2. Handle dual direction of MQTT broker: Subscription and publish MQTT message. A program subscribe to MQTT set VSS topic, when receving MQTT message, set VSS flow is processed at the same time with sensor flow.

The MQTT message is formed as below:
{
  "value": 105.3,
  "timestamp": "2024-11-13T14:29:37.156154+00:00"
}

Verify Component Deployment:

    Execute docker compose ps in the terminal.

    Confirm that all defined services (kuksa-databroker, mosquitto, mock-provider, etc.) are listed with a STATUS of running or healthy.   

Verify Mock Provider:

    Start the runtime and ensure the Mock Provider is configured to generate a known signal, such as Vehicle.Speed.

    Use the KUKSA client CLI to query the Databroker: docker compose exec kuksa-databroker /usr/local/bin/databroker-cli --server 127.0.0.1:55555 get Vehicle.Speed.

    Confirm that the command returns a valid value (not NotAvailable).   

Verify UI:

    Access the web UI in a browser.

    Use the "Add Signal" form to create a new signal, for example, Vehicle.FuelLevel with type uint8.

    Verify that the new signal appears in the UI's signal list.

    Repeat the databroker-cli verification step for Vehicle.FuelLevel to confirm it has been successfully added to the Databroker and is being updated.

Verify Synchronization:

    Open a new terminal and start an MQTT subscriber client to listen to the topic corresponding to a simulated signal. Use the mosquitto_sub command-line tool, which is part of the mosquitto-clients package : mosquitto_sub -h localhost -p 1883 -t "vss/Vehicle/Speed" -v.   

    Observe the terminal output and confirm that a continuous stream of messages, containing the topic and the JSON payload, is being printed.

Verify Startup and Error Handling:

    To test the ordered startup, run docker compose down -v to completely remove the environment, followed by docker compose up. Observe the container logs to confirm that the Mock Provider waits for the Databroker to become healthy before starting.

    To test error correction, while the system is running, manually stop the Databroker container: docker stop kuksa-databroker.

    Observe the logs of the Mock Provider (docker logs -f mock-provider). Confirm that it prints connection error messages and enters its retry loop.

    Restart the Databroker: docker start kuksa-databroker.

    Confirm that the Mock Provider's logs show a successful reconnection and that data flow resumes.

Verify Stability:

    Execute the stability testing protocol detailed in the following section. Run the full runtime for a minimum of 10 minutes with several simulated signals of varying frequencies.

    Monitor the logs of all containers for any error messages or warnings (docker compose logs -f).

    Ensure no containers exit unexpectedly.