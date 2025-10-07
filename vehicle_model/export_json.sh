#!/bin/bash

VSSPEC_PATH="vehicle_signal_specification/spec/VehicleSignalSpecification.vspec"
OUTPUT_PATH="vss.json"
OVERLAY_PATH="custom_vss.vspec"

echo "Exporting VSS to JSON..."
vspec export json \
  --vspec "$VSSPEC_PATH" \
  --output "$OUTPUT_PATH" \
  --overlays "$OVERLAY_PATH" \
  --pretty

if [ $? -eq 0 ]; then
  echo "✅ Export completed successfully!"
  echo "Output saved at: $OUTPUT_PATH"
else
  echo "❌ Export failed!"
  exit 1
fi
