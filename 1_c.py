def extract_code_number(number: str) -> tuple[str, str]:
	number = number.replace('-', '')
	number = number.replace('(', '')
	number = number.replace(')', '')
	if len(number) == 7:
		code = '495'
	else:
		if number.startswith('+'):
			number = '8' + number[2:]
		code = number[1:4]
	number = number[-7:]
	return code, number


new_code, new_number = extract_code_number(input())
for _ in range(3):
	old_code, old_number = extract_code_number(input())
	if old_number == new_number and old_code == new_code:
		print('YES')
	else:
		print('NO')
