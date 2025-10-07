import time
import random
import grpc
from kuksa_client.grpc import VSSClient

def run_provider():
    """Main function to connect and run the data generation loop."""
    databroker_address = "kuksa-databroker:55555"
    with VSSClient(host=databroker_address) as client:
        print("Successfully connected to KUKSA Databroker.")
        # Reset retry delay on successful connection
        global retry_delay
        retry_delay = 1
        
        # --- Main data generation loop would be here ---
        # This loop would parse signals.yml, generate data,
        # and call client.set_current_values(...)
        while True:
            # Placeholder for generation logic
            time.sleep(1)

if __name__ == "__main__":
    retry_delay = 1  # Initial delay in seconds
    max_delay = 60   # Maximum delay
    
    while True:
        try:
            run_provider()
            # If run_provider exits cleanly, break the loop
            break
        except grpc.RpcError as e:
            # This catches gRPC-specific errors, like UNAVAILABLE
            print(f"Connection to Databroker failed: {e}. Retrying in {retry_delay:.2f}s...")
            time.sleep(retry_delay)
            # Exponential backoff with jitter
            retry_delay = min(max_delay, retry_delay * 2 + random.uniform(0, 1))
        except Exception as e:
            # Catch other potential exceptions
            print(f"An unexpected error occurred: {e}. Retrying...")
            time.sleep(retry_delay)