import time

# Get the current time in seconds since January 1, 1970
current_time = time.time()

# Format the seconds since January 1, 1970 with commas and decimal places
formatted_time = "{:,.4f}".format(current_time)

# Format the seconds since January 1, 1970 in scientific notation
scientific_notation = "{:.2e}".format(current_time)

# Format the current date as "Month Day Year"
current_date = time.strftime("%b %d %Y")

# Print the formatted output
print("Seconds since January 1, 1970: {} or {}\
in scientific notation".format(formatted_time, scientific_notation))
print(current_date)
