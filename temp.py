# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  temp.py
@Description    :  
@CreateTime     :  2020/8/24 18:38
------------------------------------
@ModifyTime     :  
"""


def main():
    flag = len(u_text.keys()) // 30000 + 1
    item = flag * 30000
    final_item = u_text.keys()[:]

    for i in range(flag + 1):
        if i == flag:
            keys = u_text.keys()[i * 30000:]
        else:
            keys = u_text.keys()[i * 30000: (i + 1)]

        for key in tqdm(keys):
            u_text[key] = getxiangliang(u_text[key])
        i_text = pad_sentences(i_text, i_len)
        print("pad u_text item done")

    flag = len(i_text.keys()) // 30000 + 1
    for i in range(flag + 1):
        if i == flag:
            keys = i_text.keys()[i:]
        else:
            keys = i_text.keys()[i:i + 1]

        for key in tqdm(keys):
            i_text[key] = getxiangliang(i_text[key])
        print("pad i_text  item done")




    from tqdm import tqdm

    count_flag = 30000
    u_text_list = list(u_text.keys())
    flag_u = len(u_text_list) // count_flag
    final_flag = len(u_text_list) % count_flag

    for i in range(flag_u):
        for key in tqdm(u_text_list[i*count_flag: (i+1)*count_flag]):
            u_text[key] = getxiangliang(u_text[key])
    if final_flag != 0:
        for key in tqdm(u_text_list[len(u_text) - final_flag:]):
            u_text[key] = getxiangliang(u_text[key])
    print("u_text item done")

    i_text = pad_sentences(i_text, i_len)
    i_text_list = list(i_text.keys())
    flag_i = len(i_text_list) // count_flag
    final_flag = len(i_text_list) % count_flag

    for i in range(flag_i):
        for key in tqdm(i_text_list[i*count_flag: (i+1)*count_flag]):
            i_text[key] = getxiangliang(i_text[key])
    if final_flag != 0:
        for key in tqdm(i_text_list[len(i_text) - final_flag:]):
            i_text[key] = getxiangliang(i_text[key])
    print("i_text item done")
    print("pad item done")


if __name__ == '__main__':
    main()