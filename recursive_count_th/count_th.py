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





print(count_th('ththdlkthJthJ'))
