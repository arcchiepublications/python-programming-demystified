def coroutine():
    while True:
        value = yield
        # Process the value

# Example usage
co = coroutine()
next(co)  # Prime the coroutine
co.send(10)  # Send a value to the coroutine
