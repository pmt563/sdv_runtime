API Endpoints:

    GET /api/signals: This endpoint reads the signals.yml file from the shared volume, parses it using the PyYAML library, and returns its content as a JSON array to the frontend.

    POST /api/signals: This endpoint accepts a JSON object in its request body containing the details of a new signal. The backend validates this data, appends it to the existing list of signals in signals.yml, and overwrites the file with the updated configuration.

    DELETE /api/signals: This endpoint accepts a VSS path as part of the URL (e.g., /api/signals/Vehicle.Speed). It removes the corresponding signal entry from the signals.yml file.