'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    target = 2
    length = len(word)
    if length < target:
        return 0

    if "th" == word[0: target]:
        return count_th(word[target - 1:]) + 1

    return count_th(word[target - 1:])




    # if word:
    #     count = word.count('th')
    #     return count
    # else:
    #     return 0
    # if word.count('th'):
    #     count += 1
    #     newcount = count_th(word)
    # return newcount
    # if 'th' in word:
    #     count += 1
    #     return count
    #     return count + count_th(word[1:])


    # count = 0
    # if len(word) > 0:
    #     word.count('th')
    #     count += 1
    #     return count
    # return count_th(word)


    # count = 0
    # if 'th' in word:
    #     count += 1
    #     return count







    #
	# count = 0
	# newword = []
	# a = 0
	# b = 2
	# if 'th' in word[a:b]:
	# 	count += 1
	# 	# a += 2
	# 	# b += 2
	# 	return count_th(word[a+2:b+2])
    #
	# else:
	# 	return 'None here'
	# return count

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




#
# word = 'ththdlkthJthJ'
#
# print(word.count('th'))


print(count_th('ththdlkthJthJ'))

# print(count_th)
