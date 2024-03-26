import re

def extract_ip_addresses(log_file):
    """
    Extracts unique IP addresses from a login attempt log file.

    Args:
        log_file (str): Path to the login attempt log file.

    Returns:
        list: List of unique IP addresses found in the log file.
    """


    # Initialize a set to store unique IP addresses (sets automatically ensure uniqueness)
    ip_addresses = set()

    # Open the log file in read mode with context manager (`with`) for guaranteed cleanup
    with open(log_file, 'r') as f:
        # Iterate over each line in the log file
        for line in f:

            # Use regular expression to search for valid IPv4 addresses
            match = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)

            # If a valid IP address is found
            if match:
                # Extract the matched IP address and add it to the set
                ip_addresses.add(match.group(0))

    # Convert the set of IP addresses to a list and return it
    return list(ip_addresses)


# Define the path to the login attempt log file (replace with your actual filename)
log_file = 'login_attempts_sample.txt'

# Extract unique IP addresses from the log file
ips = extract_ip_addresses(log_file)

# Print a message indicating the analyzed log file
print(f"List of unique IP addresses in the file '{log_file}':")

# Iterate through the list of unique IPs and print each on a separate line
for ip in ips:
    print(f"- {ip}")
