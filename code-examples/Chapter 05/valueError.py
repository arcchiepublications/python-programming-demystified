try:
    number = int("not_a_number")
except ValueError as e:
    print("ValueError:", e)
