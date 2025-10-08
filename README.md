Use the exist repo/ packages, just config to use:
- KUKSA Data Broker: use release images and pass config to it.
- KUKSA Data Broker CLI
- MQTT mosquitto: add config file

Need to be developed:
- Ordered startup sequence using health checks, which is critical for system stability.
- The program provides friendly UI for adding and deleting then merge with exist VSS 4.0 file
- The program handles error fault:
    - Retries with Backoff
- The program sync custom VSS file
- Graceful shutdown.
- (Opt) Friendly UI all above features



The complete dependency chain for the runtime will be as follows:

    The KUKSA Databroker and Mosquitto services start first, as they have no dependencies.

    The Mock Provider and the KUKSA-to-MQTT Bridge will both have depends_on: kuksa-databroker: { condition: service_healthy }. This ensures they do not start until the Databroker is confirmed to be fully operational.

    The KUKSA-to-MQTT Bridge will also have depends_on: mosquitto: { condition: service_started }. A health check is not strictly necessary for Mosquitto as it becomes ready very quickly.

    The UI Backend will depend_on the Mock Provider, ensuring the data generation process has begun before the UI is available.


#### Core Services

| Service Name               | Container Image                                  | Host Ports  | Container Ports |
|----------------------------|--------------------------------------------------|-------------|-----------------|
| **kuksa-databroker**       | `ghcr.io/eclipse-kuksa/kuksa-databroker:latest`  | 55555       | 55555           |
| **mosquitto**              | `eclipse-mosquitto:latest`                       | 1883, 9001  | 1883, 9001      |
| **mock-provider**          |                  *(custom build)*                | —           | —               |
| **vehicle-model-generator**|                  *(custom build)*                | 8080        | 80              |

### Environment variables

|-------------------|-----------------------------------------|----------|--------------------------------------|
|   Variable Name   | Description                             | Required |                  Default Value       | 
|-------------------|-----------------------------------------|----------|--------------------------------------|
| `MOCK_ADDRESS`    | Address of mock service                 | ✅       | `0.0.0.0:50053`                      |
| `VDB_ADDRESS`     | Address of Data Broker                  | ✅       | `127.0.0.1:55555`                    |
| `MOCK_ADDRESS`    | Address of mock service                 | ✅       | `0.0.0.0:50053`                      |
| `MOCK_ADDRESS`    | Address of mock service                 | ✅       | `0.0.0.0:50053`                      |
| `APP_ENV`         | Defines the running environment         | ❌       | `development`                        | 
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |
| `APP_ENV`         | Defines the running environment         | ✅       | `development`                        |

