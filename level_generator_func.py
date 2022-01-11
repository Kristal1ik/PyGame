from random import choice, randrange

def new_part_generate():
    all_file = '['
    for stroka in range(12):
        if stroka != 11:
            printed_stroka = '['
            lenth_stroki = 0
            ground = choice((True, False))
            #print(ground)
            while lenth_stroki < 22:
                min_len = 3
                max_empty_len = 20
                min_empty_len = 8
                ok_variant = False
                max_len = 10
                add_lenth = 1
                if ground:
                    while not ok_variant:
                        add_lenth = randrange(min_len, max_len)
                        if 22 >= lenth_stroki + add_lenth:
                            ok_variant = True
                        else:
                            if max_len - 1 > min_len:
                                max_len -= 1
                            else:
                                add_lenth = 22 - lenth_stroki
                                ok_variant = True
                    lenth_stroki += add_lenth
                    printed_stroka += "'X', " * add_lenth
                    #print(printed_stroka)
                    ground = not ground
                elif not ground:
                    while ok_variant == False:
                        add_lenth = randrange(min_empty_len, max_empty_len)
                        if 22 >= lenth_stroki + add_lenth:
                            ok_variant = True
                        else:
                            if max_empty_len - 1 > min_empty_len:
                                max_empty_len -= 1
                            else:
                                add_lenth = 22 - lenth_stroki
                                ok_variant = True
                    lenth_stroki += add_lenth
                    printed_stroka += "'.', " * add_lenth
                    ground = not ground
            printed_stroka += "'X'"
        else:
            printed_stroka = '['
            printed_stroka += "'X', " * 22
            printed_stroka += ']'
        all_file += printed_stroka
        if stroka != 11:
            all_file += '],'
        else:
            all_file += ']'
        all_file += '\n'
    print(all_file)
    return all_file

new_part_generate()
