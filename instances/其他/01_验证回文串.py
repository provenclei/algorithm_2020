# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  01_验证回文串.py
@Description    :  
@CreateTime     :  2020/8/5 21:30
------------------------------------
@ModifyTime     :  
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


def main():
    solution = Solution()
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(solution.isPalindrome(s1))
    print(solution.isPalindrome(s2))


if __name__ == '__main__':
    main()