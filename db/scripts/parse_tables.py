import sys

tables_to_dump = ['creature', 'creature_template']

START_MARKER = '# Dump of table'
END_MARKER = 'ENABLE'

name = None
for line in sys.stdin:
    line = line.rstrip()
    if line.startswith(START_MARKER):
        name = line[len(START_MARKER):].strip()
    elif name in tables_to_dump:
        print(line)

    if name and line.endswith(END_MARKER):
        name = None
