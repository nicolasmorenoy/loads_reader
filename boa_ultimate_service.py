from loads_list import load_combinations

combos = load_combinations()

service = [load for load in combos if load[0:2]=='S:']
ultimate = [load for load in combos if load[0:2]=='U:']