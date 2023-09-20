
import time
from datetime import date

timestamp = time.time()
formatted_timestamp = f"{timestamp:,.4f}"
# print(formatted_timestamp)
formatted_scientific = f"{timestamp:.2e}"
# print(formatted_scientific)
print("Seconds since January 1, 1970:", formatted_timestamp, "or",
formatted_scientific, "in scientific notation")

# Oct 21 2022
# b - months abbreviation
current_date = date.today()
formatted_date = current_date.strftime("%b %d %Y")
print(formatted_date)

# import datetime
# from datetime import date

# now = datetime.datetime.now()

# # print(date.today())
# formatted_time = f"Seconds since January 1, 1970: {now:.4f}"
# print(formatted_time)

# epoch - begins at 00:00:00 1 Jan 1970
# Seconds since January 1, 1970: 1,666,355,857.3622 or
# 1.67e+09 in scientific notation$
