eng_letters = ["T", "F", "R", "Q", "C", "P", "E", "S", "N", "M", "L", "K", "I", "J", "X", "Z", "W", "H", "D", "G", "B", "A"]
heb_letters = ["ת", "ש", "ר", "ק", "צ", "פ", "ע", "ס", "נ", "מ", "ל", "כ", "י", "ט", "ח", "ז", "ו", "ה", "ד", "ג", "ב", "א"]

reg_letters = ["פ", "צ", "נ", "מ", "כ"]
last_letters = ["ף", "ץ", "ן", "ם", "ך"]

single_letters = ["ו", "ל", "כ", "ש", "מ" , "ה", "ב"]

if __name__=='__main__':
	import sys
	import io

	from optparse import OptionParser
	parser = OptionParser("%prog [options] < in_file > out_file")
	opts, args = parser.parse_args()

	text = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8').read()

	for eng_letter, heb_letter in zip(eng_letters, heb_letters):
		text = text.replace(eng_letter, heb_letter)

	for single_letter in single_letters:
		text = text.replace(" " + single_letter + " ", " " + single_letter)

	for reg_letter, last_letter in zip(reg_letters, last_letters):
		for ending in [",", ".", "!", "?", " ", ")", ";"]:
			text = text.replace(reg_letter + ending, last_letter + ending)

	sys.stdout.buffer.write(text.encode('utf8'))
