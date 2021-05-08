with open("Python.txt") as file:
    content = file.readlines()[2]
    print(content)
    char_count = 0
    word_count = 0
    line_count = 0
    for char in content:
        char_count += 1
        if char == ' ':
            word_count += 1
        if char == '\n':
            line_count += 1
    word_count += 1
    line_count += 1
    print("Characters:", char_count)
    print("Words:", word_count)
    print("Lines:", line_count)
