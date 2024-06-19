def fetch_paginated_data(api_url, page_size):
    page = 0
    while True:
        response = requests.get(f"{api_url}?page={page}&size={page_size}")
        data = response.json()
        if not data:
            break
        yield from data
        page += 1

# Example usage
for item in fetch_paginated_data('https://api.example.com/data', 100):
    # Process each item
    pass
