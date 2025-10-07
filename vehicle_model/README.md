Define VSS signal want to add with data as below:

*** Data Types ***
Name 	Datatype 	Min 	Max
uint8 	unsigned 8-bit integer 	0 	255
int8 	signed 8-bit integer 	-128 	127
uint16 	unsigned 16-bit integer 	0 	65535
int16 	signed 16-bit integer 	-32768 	32767
uint32 	unsigned 32-bit integer 	0 	4294967295
int32 	signed 32-bit integer 	-2147483648 	2147483647
uint64 	unsigned 64-bit integer 	0 	2^64 - 1
int64 	signed 64-bit integer 	-2^63 	2^63 - 1
boolean 	boolean value 	0/false 	1/true
float 	IEEE 754-2008 binary32 floating point number 	-3.40e 38 	3.40e 38
double 	IEEE 754-2008 binary64 floating point number 	-1.80e 308 	1.80e 308
string 	character string (unicode) 	n/a 	n/a


Use vspec tools to generate vehicle VSS json file:
1. Activate a virtual environment.
python3 -m venv venv
source.venv/bin/activate
2. Install vss-tools
pip install vss-tools
3. At the dir: sdv_runtime/vehicle_model, command:
vspec export json --vspec vehicle_signal_specification/spec/VehicleSignalSpecification.vspec --output vss.json      --overlays custom_vss.vspec --pretty
    In that: custom_vss.vspec file is the vspec file that describe custom VSS signal.

Or run the export_json.sh