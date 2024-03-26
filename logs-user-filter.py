# Open the log file for reading
with open("login_attempts_sample.txt", "r") as file:

  # Initialize an empty list to store usernames
  usernames = []

  # Loop through each line in the file
  for line in file:
    # Split the line based on spaces
    parts = line.split()

    # Extract the username (assuming it's within quotes after "user")
    if "user" in parts:
      username_index = parts.index("user") + 1
      if username_index < len(parts):
        username = parts[username_index].strip("'")
        usernames.append(username)

  # Remove duplicate usernames and print them in the desired format
  unique_usernames = list(set(usernames))
  for username in unique_usernames:
    print(f"- {username}")
