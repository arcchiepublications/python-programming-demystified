from collections import Counter

# Sample data: List of responses in a survey
responses = ['Yes', 'No', 'Yes', 'No', 'Yes', 'Maybe', 'Yes', 'No', 'Maybe', 'Maybe']

# Creating a Counter for the responses
response_counter = Counter(responses)

# Most common response
most_common_response = response_counter.most_common(1)[0]
print("Most common response:", most_common_response)

# Total count of 'Maybe' responses
maybe_count = response_counter['Maybe']
print("Total 'Maybe' responses:", maybe_count)
