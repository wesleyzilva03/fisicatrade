# GERADOR_ROBOS.py

import os
import json

# Directories for robot groups
group_dirs = ['group1', 'group2', 'group3', 'group4']

# Create directories if they don't exist
for group in group_dirs:
    if not os.path.exists(group):
        os.makedirs(group)

# Robot specifications based on group strategy
robot_specifications = {
    'group1': lambda i: {'name': f'robot_{i}', 'strategy': 'force gradient calculations', 'param1': 0.1, 'param2': 0.2},
    'group2': lambda i: {'name': f'robot_{i}', 'strategy': 'OBV indicators', 'param1': 0.3, 'param2': 0.4},
    'group3': lambda i: {'name': f'robot_{i}', 'strategy': 'VWAP', 'param1': 0.5, 'param2': 0.6},
    'group4': lambda i: {'name': f'robot_{i}', 'strategy': 'volume-weighted ATR', 'param1': 0.7, 'param2': 0.8},
}

# Generate robots
for group in group_dirs:
    for i in range(50):
        robot = robot_specifications[group](i)
        robot_filepath = os.path.join(group, f'{robot["name"]}.ntsl')
        with open(robot_filepath, 'w') as robot_file:
            json.dump(robot, robot_file, indent=4)

print('Robot files generated successfully!')
