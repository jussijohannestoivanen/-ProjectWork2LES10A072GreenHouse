import csv

def find_variable_instances(csv_file, variables):
    instances = {var: [] for var in variables}

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row

        for row in reader:
            for variable in variables:
                if variable in row:
                    instances[variable].append(row)

    return instances

# Example usage
csv_file = 'data.csv'
variables = ['variable1', 'variable2', 'variable3', 'variable4', 'variable5']

result = find_variable_instances(csv_file, variables)

# Print the instances for each variable
for variable, instances in result.items():
    print(f'Instances of {variable}:')
    for instance in instances:
        print(instance)
    print()