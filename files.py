with open('1.txt') as file1, open('2.txt') as file2, open('3.txt') as file3, open('4.txt', 'w') as file4:
    list_files = [file1, file2, file3]
    list_lines = {}
    for file in list_files:
        list_line = [line for line in file]
        added_inf = {'name': file.name, 'list_line': list_line}
        list_lines[len(list_line)] = added_inf
    sort_list_lines = sorted((list_lines).items())
    print(sort_list_lines)
    for len, file in sort_list_lines:
        list_line = ''.join(file['list_line'])
        file4.writelines(f"{file['name']}\n{len}\n{list_line}\n")

    