# Log File Filters 

This repository contains Python scripts for filtering and analyzing login attempt logs. 

Scripts:                                             

logs-failed-filter.py                                             
  Parses a login attempt log file and lists users with failed logins.                                              
  Prompts the user to enter the filename.                                             
  Identifies failed logins based on the string "Invalid login attempt from user".                                             
  Prints a list of failed usernames.                                             
                                            
logs-ip-filter.py                                                                 
  Extracts unique IP addresses from a login attempt log file.                                             
  Uses regular expressions to identify IPv4 addresses.                                             
  Prints a list of unique IP addresses found in the log file.                                             
                                            
logs-user-filter.py                                            
  Extracts unique usernames from a login attempt log file.                                                                                         
  Assumes usernames are within quotes and preceded by the word "user".                                             
  Prints a list of unique usernames found in the log file.                                             
                                            
Usage                                            
1.	Clone or download this repository.                                             
2.	Ensure you have Python 3.x installed on your system.                                             
3.	Run the desired script directly from the command line:                                             
                                            
Additional Notes                                             
Replace any placeholder filenames (login_attempts_sample.txt) with the actual names of your log files.                                             
Depending on the type of log you want to analyze, some adaptations may be necessary.                                             
Consider incorporating logging and exception handling for more robust scripts.                                             
                                            
Contributing                                             
Fork this repository and create a branch for your changes.                                                                                         
Commit your changes with clear and descriptive commit messages. 
Open a pull request for review and potential merging.                                             
