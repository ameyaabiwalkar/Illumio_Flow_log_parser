import csv
import time
import socket
from collections import defaultdict

start = time.time()

# Mapping protocol numbers to their names
prefix = "IPPROTO_"
protocol_num_map = {num: name[len(prefix):].lower() 
                    for name, num in vars(socket).items()
                    if name.startswith(prefix)}

lookup_table = {}
port_protocol_counter = defaultdict(int)
tag_counter = defaultdict(int)

# Loading lookup table
with open('lookup_table.csv', 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            key = (row['dstport'].strip(), row['protocol'].strip().lower())
            tag = row['tag'].strip()
            lookup_table[key] = tag
        except KeyError as e:
            print(f"KeyError: {e} - Ensure the CSV file has correct headers")

# Processing each line in the flow logs
def process_line_and_update_counters(line):
    port, protocol_num = line.split(' ')[6:8]
    protocol = protocol_num_map.get(int(protocol_num), 'unknown')
    port_protocol_counter[(port, protocol)] += 1
    tag = lookup_table.get((port, protocol), "Untagged")
    tag_counter[tag] += 1

with open('flow_logs.txt', mode='r') as file:
    for line in file:
        process_line_and_update_counters(line)

# Writing output files
with open('output_tag_count.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Tag", "Count"])
    writer.writeheader()
    for tag, count in tag_counter.items():
        writer.writerow({"Tag": tag, "Count": count})

with open('output_port_protocol_count.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Port", "Protocol", "Count"])
    writer.writeheader()
    for (port, protocol), count in port_protocol_counter.items():
        writer.writerow({"Port": port, "Protocol": protocol, "Count": count})

end = time.time()
print(end - start)
