import sys

tables_to_dump = ['creature', 'creature_template']

START_MARKER = '# Dump of table'
END_MARKER = 'ENABLE'
INSERT_MARKER = 'INSERT INTO'

name = None
current_keys = list()
data = {name: list() for name in tables_to_dump}

for line in open(sys.argv[1], 'r'):
    line = line.rstrip()
    if line.startswith(START_MARKER):
        name = line[len(START_MARKER):].strip()
    elif name in tables_to_dump:
        if line.startswith(INSERT_MARKER):
            contents = line[line.find('(') + 1:line.find(')')].replace('`', '')
            current_keys = [part.strip() for part in contents.split(',')]
        elif line.lstrip().startswith('('):
            contents = line[line.find('(') + 1:line.find(')')].replace('`', '')
            values = [part.strip() for part in contents.split(',')]
            assert len(values) == len(current_keys)

            data[name].append({current_keys[i]: value for i, value in enumerate(values)})
            #print(data)

    if name and line.endswith(END_MARKER):
        name = None
