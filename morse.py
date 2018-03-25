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


for letter in d:
	print(letter);



#code for reading and translating from english
bool = True;
while(bool):
	s = raw_input("type your message: ");
	if s == 'exit':
		bool = False;
	t = "";
	for c in s:
		t = t + d.get(c, '?') + '  ';

	print(t);

exit();

