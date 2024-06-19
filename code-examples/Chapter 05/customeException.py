class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("This is a custom error message.")
except MyCustomError as e:
    print("MyCustomError:", e)
