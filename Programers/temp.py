check_str = ['apple', 'banana', 'orange']

target_str = 'I eat banana'

if any(str in target_str for str in check_str):
	# 있을 경우 if 문 실행
	print(target_str)