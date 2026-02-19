import sys

try:
    result = int(4/2)
# except Exception as e:
#     print(type(e))

except ZeroDivisionError as error_msg:
    print(f"above the error message\n{error_msg}")

else:
    print(f"the result is {result}")





