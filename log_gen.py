import random
import socket
import string

# Constants
prefix = "IPPROTO_"
protocol_num_map = {num: name[len(prefix):].lower() 
                    for name, num in vars(socket).items() 
                    if name.startswith(prefix)}

# Generate a set of unique ports
ports = set()
while len(ports) < 333:
    ports.add(random.randint(0, 65535))
ports = list(ports)

def rand_name_gen():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

# Creating a new lookup_table_generated.csv file
with open('lookup_table_generated.csv', 'w') as f:
    f.write("dstport,protocol,tag\n")
    for proto_num in protocol_num_map.keys():
        proto_name = protocol_num_map[proto_num]
        for port in ports:
            f.write(f"{port},{proto_name},{rand_name_gen()}\n")

# Generate random ENI IDs
def generate_eni_id():
    return "eni-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

# Generate random IP addresses
def generate_ip_address():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Generate random log status
def generate_status():
    return random.choice(["ACCEPT", "REJECT"])

# Generate random time (Unix epoch time)
def generate_time():
    return random.randint(1600000000, 1700000000) 

# Generate random account IDs
def generate_account_id():
    return ''.join(random.choices(string.digits, k=12))

# Creating the flow logs
with open('flow_logs_generated.txt', 'w') as f:
    for _ in range(90000):
        account_id = generate_account_id()
        eni_id = generate_eni_id()
        src_ip = generate_ip_address()
        dst_ip = generate_ip_address()
        src_port = random.choice(ports)
        dst_port = random.choice(ports)
        protocol_num = random.choice(list(protocol_num_map.keys()))
        protocol_name = protocol_num_map[protocol_num]
        packets = random.randint(5, 25)
        bytes_transferred = packets * random.randint(500, 1000)
        start_time = generate_time()
        end_time = start_time + random.randint(1, 60) 
        status = generate_status()

        log_entry = (
            f"2 {account_id} {eni_id} {src_ip} {dst_ip} {src_port} {dst_port} {protocol_num} "
            f"{packets} {bytes_transferred} {start_time} {end_time} {status} OK\n"
        )
        f.write(log_entry)
