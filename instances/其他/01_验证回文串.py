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


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        # 时间：o(n), 空间：o(n）

        # 方法一
        # sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
        # return sgood == sgood[::-1]

        # 方法二：双指针
        sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(sgood)-1
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 时间：o(n), 空间：o(1）
        # 在原字符串上进行
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True


def main():
    solution = Solution()
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(solution.isPalindrome(s1))
    print(solution.isPalindrome(s2))


if __name__ == '__main__':
    main()