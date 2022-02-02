
def count_substrings(string, start_letter, end_letter):
    counter = 0

    for i in range(len(string)-1):

        if string[i] != start_letter:
            continue

        for j in range(i+1, len(string)):
            if string[j] == end_letter:
                counter = counter + 1

    return counter


def demo_counter():

    string = 'TXZXXJZWX'
    start_letter = 'X'
    end_letter = 'Z'

    count = count_substrings(string, start_letter, end_letter)
    print('String: ', string)
    print('Start_letter: ', start_letter, '\t', 'End_letter: ', end_letter)
    print('Substring count: ', count)
    print('-----------------------------------------------------')

    string = 'abab'
    start_letter = 'a'
    end_letter = 'b'

    count = count_substrings(string, start_letter, end_letter)
    print('String: ', string)
    print('Start_letter: ', start_letter, '\t', 'End_letter: ', end_letter)
    print('Substring count: ', count)
    print('-----------------------------------------------------')

    string = 'tttccc'
    start_letter = 't'
    end_letter = 'c'

    count = count_substrings(string, start_letter, end_letter)
    print('String: ', string)
    print('Start_letter: ', start_letter, '\t', 'End_letter: ', end_letter)
    print('Substring count: ', count)
    print('-----------------------------------------------------')

demo_counter()