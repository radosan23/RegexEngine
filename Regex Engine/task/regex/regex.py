def compare(regex, string):
    if not regex or regex == '$' and not string:
        return True
    if len(regex) > 1 and regex[1] in ('?', '*', '+') and regex[0] != '\\':
        return quantifiers(regex, string)
    if regex[0] == '\\':
        regex = regex[1:]
        if not string or regex[0] != string[0]:
            return False
    else:
        if not string or regex[0] not in (string[0], '.'):
            return False
    return compare(regex[1:], string[1:])


def quantifiers(regex, string):
    if regex[1] in ('*', '+') and len(string) > 1 and (string[0] == string[1] == regex[0] or regex[0] == '.'):
        return (compare(regex[2:], string) if regex[1] != '+' else compare(regex[2:], string[1:])) \
                                                                  or compare(regex, string[1:])
    elif string and (regex[0] in (string[0], '.')):
        return regex[1] != '+' and compare(regex[2:], string) or compare(regex[2:], string[1:])
    else:
        return False if regex[1] == '+' else compare(regex[2:], string)


def change_pos(regex, string):
    return compare(regex, string) or bool(string) and change_pos(regex, string[1:])


def check_caret(regex, string):
    return compare(regex[1:], string) if regex.startswith('^') else change_pos(regex, string)


def main():
    data = input().split('|')
    print(check_caret(*data))


if __name__ == '__main__':
    main()
