# Flow Log Parser

## Description
This program parses flow log data and matches each log entry with a tag based on a lookup table. The results include:
1. A count of matches for each tag.
2. A count of matches for each port/protocol combination.

## Assumptions
- The program supports only the default log format and version 2.
- The lookup table is case-insensitive.
- The flow log file and lookup table are ASCII text files.

## Prerequisites
- Python 3.x
- `lookup_table.csv`: A CSV file that contains the lookup table with the following columns:
  - `dstport`: Destination port number.
  - `protocol`: Protocol name (e.g., `tcp`, `udp`).
  - `tag`: The tag associated with the `dstport` and `protocol` combination.
- `flow_logs.txt`: A text file containing flow log data in a specific format.

## Log File Format
- Each log entry in flow_logs.txt follows the format:

2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK

## Field Description:
- Version number: 2 - Indicates the log format version.
- AWS account ID: 123456789012 - The AWS account ID associated with the log entry.
- Elastic Network Interface (ENI) ID: eni-0a1b2c3d - The ENI ID associated with the log entry.
- Source IP address: 10.0.1.201 - The IP address from which the flow originated.
- Destination IP address: 198.51.100.2 - The IP address to which the flow was directed.
- Source port: 443 - The port number used by the source IP address.
- Destination port: 49153 - The port number used by the destination IP address.
- Protocol number: 6 - The protocol number representing TCP (6) or UDP (17) etc.
- Number of packets transferred: 25 - The total number of packets transferred during the flow.
- Number of bytes transferred: 20000 - The total number of bytes transferred during the flow.
- Start time: 1620140761 - The Unix epoch time when the flow started.
- End time: 1620140821 - The Unix epoch time when the flow ended.
- Action: ACCEPT - Indicates whether the flow was accepted or rejected.
- Log status: OK - Status of the log entry.

## Running the Program
1. Ensure you have Python installed on your machine.
2. Place the flow log file (`flow_logs.txt`) and the lookup table (`lookup_table.csv`) in the same directory as the script.
3. Run the script: 
   python flow_log_data_parser.py

## Results
The results will be written to output_tag_count.csv and output_port_protocol_count.csv.
- `output_tag_count.csv`: A CSV file containing the count of matches for each tag.
- `output_port_protocol_count.csv`: A CSV file containing the count of matches for each port/protocol.

## Testing
The program has been tested with sample data to verify correctness.
The sample data is provided in the flow_logs.txt and lookup_table.csv files.
You can use these files to test the program.
The script prints the time taken to process the logs at the end, which can be helpful for performance monitoring.

## Log Generation
- The flow logs data and lookup table can be generated using the `log_gen.py` script. 
- The outputs from this script are written to two separate files: `flow_logs_generated.txt` and `lookup_table_generated.csv`.
- You can modify the `log_gen.py` script to adjust the parameters for generating custom flow logs and lookup tables.
- The generated files can be used to test the `flow_log_parser_generated_data.py` script.
- Run the script: 
   python flow_log_parser_generated_data.py

## Generated Data Results
The results will be written to output_tag_count_generated.csv and output_port_protocol_count_generated.csv.
- `output_tag_count_generated.csv`: A CSV file containing the count of matches for each tag.
- `output_port_protocol_count_generated.csv`: A CSV file containing the count of matches for each port/protocol.