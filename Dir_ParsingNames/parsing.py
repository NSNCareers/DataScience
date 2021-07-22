
import  csv
# We are only concerned about first and last names

html_output = ''
names = []

# use context manager to open file

with open('Dir_ParsingNames\Parse1.csv','r') as data_file:
    csv_data = csv.reader(data_file)
    # print(list(csv_data)) casting data to a list

    # Step over values by calling the next iterator
    # We do not want headers
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0]=='No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank you</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t\,li\.\{name}</li>'

html_output += '\n</ul>'
print(html_output)
    
        
