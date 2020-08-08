# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  03_反转字符串中的单词.py
@Description    :  
@CreateTime     :  2020/8/7 23:49
------------------------------------
@ModifyTime     :  给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


class Solution:
    def reverseWords1(self, s: str) -> str:
        # 时间复杂度： O(n) 。其中n是字符串的长度。
        # 空间复杂度： O(n) 。使用了大小为 n 的空间。
        return ' '.join(i[::-1] for i in s.split())

    def my_split(self):
        pass

    def my_reverse(self):
        pass

    def reverseWords(self, s: str) -> str:
        # 时间复杂度： O(n) 。其中n是字符串的长度。
        # 空间复杂度： O(n) 。使用了大小为 n 的空间。
        start, end = 0, 0
        while True:
            if start >= len(s)-1:
                break
            if end == len(s)-1 or s[end + 1] == ' ':
                # 如果可以在字符串中进行交换，空间复杂度可以降为O(1)
                sstring = s[start: end + 1][::-1]
                # sstring = sstring[::-1]
                s = s[0: start] + sstring + s[end + 1:]
                
                start = end + 2
                end = start
            else:
                end += 1
        return s


def main():
    solution = Solution()
    s = "Let's take LeetCode contest"
    print(solution.reverseWords(s))


if __name__ == '__main__':
    main()