device = input("Enter device name: ")
params = ", ".join(london_co[device].keys())
parameter = input(f"Enter parameter name ({params}): ")

print(london_co[device][parameter])