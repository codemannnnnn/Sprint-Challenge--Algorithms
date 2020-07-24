'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
	count = 0
	newword = []
	a = 0
	b = 2
	if 'th' in word[a:b]:
		count += 1
		a += 2
		b += 2
		newword.append(word)

		return count_th(newword)

	else:
		return 'None here'
	return count

	# if 'th' in word[a:b]:
	#     count += 1
	#     a += 2
	#     b += 2


	# return count_th(word)




	#
	# word = word[0:2]
	# if word == 'th':
	#     count += 1
	# elif word


	# if word[2:4] == 'th':
	#     count += 1








print(count_th('ththdlkthJJ'))

# print(count_th)
