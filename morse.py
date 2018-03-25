#dictionary
d = {
	'a' :'.-',
	'b' :'-...',
	'c' :'-.-.',
	'd' :'-..',
	'e' :'.',
	'f' :'..-.',
	'g' :'--.',
	'h' :'....',
	'i' : '..',
	'j' : '.---',
	'k' : '-.-',
	'l' : '.-..',
	'm' : '--',
	'n' : '-.',
	'o' : '---',
	'p' : '.--.',
	'q' : '--.-',
	'r' : '.-.',
	's' : '...',
	't' : '-',
	'u' : '..-',
	'v' : '...-',
	'w' : '.--',
	'x' : '-..-',
	'y' : '-.--',
	'z' : '--..',
	'.' : '-.-.-.',
	' ' : '   ',
	}

#node class
class Node:
	l = None
	r = None
	letter = None	


root = Node();

for letter in d:
	node = root;
	for c in d.get(letter, " "):
		if c == '-':
			if node.r == None:
				node.r = Node();
				node = node.r
			else:
				node = node.r;
		if c == '.':
			if node.l == None:
				node.l = Node();
				node = node.l
			else:
				node = node.l;
	node.letter = letter;



def findLetter(s):
	ret = "";
	node = root;
	for c in s:
		if c =='-':
			node = node.r;
		if c == '.':
		    node = node.l;
	ret = ret + node.letter;
	return ret;



#code for reading and translating from english
bool = True;
while(bool):
	s = raw_input("type your message: ");
	if s == 'exit':
		bool = False;
	t = "";
	if s[:2] == 'M:':
		splits = s[2:].split(' ');
		for s in splits:
			t = t + findLetter(s);
	else:
		for c in s:
			t = t + d.get(c, '?') + '  ';

	print(t);
exit();

