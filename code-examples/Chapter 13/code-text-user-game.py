import re

# Regular expression patterns for parsing player commands
command_pattern = r'(?P<action>\w+)\s+(?P<target>\w+)\s+with\s+(?P<tool>\w+)'

# Function to interpret player commands
def interpret_command(command):
    match = re.match(command_pattern, command)
    if match:
        action = match.group('action')
        target = match.group('target')
        tool = match.group('tool')
        print(f"Action: {action}")
        print(f"Target: {target}")
        print(f"Tool: {tool}")
    else:
        print("Invalid command. Please try again.")

# Interactive mode: continuously accept player commands
print("Welcome to the text adventure game!")
print("Enter commands in the format 'action target with tool'.")
print("For example: 'attack dragon with sword'.")
print("Type 'quit' to exit.")

while True:
    user_input = input("Enter your command: ").lower()
    
    if user_input == 'quit':
        print("Exiting game. Goodbye!")
        break
    
    interpret_command(user_input)
    print()
