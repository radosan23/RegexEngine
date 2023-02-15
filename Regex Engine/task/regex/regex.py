def compare(regex, string):
    if not regex:
        return True
    if not string or regex[0] != string[0] and regex[0] != '.':
        return False
    return compare(regex[1:], string[1:])


def main():
    print(compare(*input().split('|')))


if __name__ == '__main__':
    main()
