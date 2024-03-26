# This script parses a login attempt file and outputs a list of users with failed logins

def list_failed_logins(filename):
  """
  This function takes a filename as input and returns a list of users who had failed login attempts.

  Args:
      filename: The name of the file containing login attempt logs.

  Returns:
      A list of usernames that failed login attempts.
  """
  failed_users = []
  with open(filename, 'r') as f:
    for line in f:
      if "Invalid login attempt from user" in line:
        username = line.split("user '")[-1].split("'")[0]
        failed_users.append(username)
  return failed_users

# Get the filename from the user
filename = input("Enter the login attempts filename: ")

# Call the function to get the list of failed users
failed_logins = list_failed_logins(filename)

# Print the list of failed users
if failed_logins:
  print("The following users had failed login attempts:")
  for user in failed_logins:
    print(user)
else:
  print("No failed login attempts found in the file.")
