import sys
import io

eng_letters = ["@suf", "yyCM", "yyCLN", "yyLRB", "yyQUOT", "yyDOT", "yyDASH", "yyRRB", "yyEXCL", "yyQM", "yySCLN", "yyELPS", "U", "O", "T", "F", "R", "Q", "C", "P", "E", "S", "N", "M", "L", "K", "I", "J", "X", "Z", "W", "H", "D", "G", "B", "A"]
heb_letters = ["~", ",", ":", "(", '"', ".", "-", ")", "!", "?", ";", "...", '"', "%", "ת", "ש", "ר", "ק", "צ", "פ", "ע", "ס", "נ", "מ", "ל", "כ", "י", "ט", "ח", "ז", "ו", "ה", "ד", "ג", "ב", "א"]

reg_letters = ["פ", "צ", "נ", "מ", "כ"]
last_letters = ["ף", "ץ", "ן", "ם", "ך"]

def untransliterate_word(word):
	for eng_letter, heb_letter in zip(eng_letters, heb_letters):
		word = word.replace(eng_letter, heb_letter)

	if len(word) > 1:
		for reg_letter, last_letter in zip(reg_letters, last_letters):
			if word[-1] == reg_letter:
				word = word[:-1] + last_letter

	return word

if __name__=='__main__':
	text = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8').read()

	untransliterated_text = "\n".join(
								" ".join(
									untransliterate_word(word)
									for word in line.split(" "))
								for line in text.split('\n'))

	sys.stdout.buffer.write(untransliterated_text.encode('utf8'))
