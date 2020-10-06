states = { 'init': 0, 'start': 1, 'progress': 2, 'stop': 3 } 
states_inv = {value: key for key, value in states.items()}
print(states)
print(states_inv)
print(states.keys())
print(states.values())