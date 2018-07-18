import os

def read_file(file):
	lines = [];
	with open(file, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip());
	#print(lines);
	return lines;

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen' :
			person = 'Allen';
			continue;
		elif line == 'Tom':
			person = 'Tom';
			continue;
		new.append(person + ': ' + line)
	print(new)
	return new;
	
def write_file(file, new_lines):
	with open(file, 'w', encoding = 'utf-8') as f:
		for p in new_lines:
			f.write(p);

def main():
	file_name = 'input.txt';
	file_name2 = 'output.txt';
	lines = read_file(file_name);
	news = convert(lines);
	write_file(file_name2, news);

main();