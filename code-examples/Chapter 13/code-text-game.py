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

# Sample player commands
commands = [
    "attack dragon with sword",
    "kill the dragon using the blade",
    "explore the forest",
    "fight banana"
]

# Interpret and process player commands
for command in commands:
    print(f"Player command: '{command}'")
    interpret_command(command)
    print()
