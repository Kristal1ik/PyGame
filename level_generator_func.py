from random import choice, randrange

file_with_part_of_level = open('Level.txt', 'w')
def new_part_generate():
    all_file = ''
    for stroka in range(12):
        if stroka != 11:
            printed_stroka = ''
            lenth_stroki = 0
            ground = choice((True, False))
            #print(ground)
            while lenth_stroki < 32:
                min_len = 3
                max_empty_len = 20
                min_empty_len = 12
                ok_variant = False
                max_len = 10
                add_lenth = 1
                if ground:
                    while not ok_variant:
                        add_lenth = randrange(min_len, max_len)
                        if 32 >= lenth_stroki + add_lenth:
                            ok_variant = True
                        else:
                            if max_len - 1 > min_len:
                                max_len -= 1
                            else:
                                add_lenth = 32 - lenth_stroki
                                ok_variant = True
                    lenth_stroki += add_lenth
                    printed_stroka += 'X' * add_lenth
                    #print(printed_stroka)
                    ground = not ground
                elif not ground:
                    while ok_variant == False:
                        add_lenth = randrange(min_empty_len, max_empty_len)
                        if 32 >= lenth_stroki + add_lenth:
                            ok_variant = True
                        else:
                            if max_empty_len - 1 > min_empty_len:
                                max_empty_len -= 1
                            else:
                                add_lenth = 32 - lenth_stroki
                                ok_variant = True
                    lenth_stroki += add_lenth
                    printed_stroka += '.' * add_lenth
                    ground = not ground
        else:
            printed_stroka = 'X' * 32
        all_file += printed_stroka
        all_file += '\n'
    print(all_file)
    return all_file

new_part_generate()
