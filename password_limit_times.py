password = 'a123456'
x = 0
while x < 3:
	a = input('請輸入密碼：[最多輸入三次密碼]')
	if a == password:
		print('登入成功!')
		break
	else:
		x = x + 1 # x += 1
		if x == 3:
			print('登入失敗!')
		else:
			print('密碼錯誤! 你還有', 3 - x, '次機會。') # b = 3 - x
