def compare(strings):
    regex, inp = strings.split('|')
    if not regex or regex == '.' and inp:
        return True
    return regex == inp


print(compare(input()))
