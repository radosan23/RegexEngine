def compare(regex, string):
    if not regex:
        return True
    if not string or regex[0] != string[0] and regex[0] != '.':
        return False
    return compare(regex[1:], string[1:])


def change_pos(regex, string):
    return compare(regex, string) or bool(string) and change_pos(regex, string[1:])


def main():
    print(change_pos(*input().split('|')))


if __name__ == '__main__':
    main()
