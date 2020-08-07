# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  02_亲密字符串.py
@Description    :  
@CreateTime     :  2020/8/6 11:40
------------------------------------
@ModifyTime     : 亲密字符串
给定两个由小写字母构成的字符串 A 和 B ，
只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        '''
        时间复杂度：O(N),其中 N 是 A 和 B 的长度。
        空间复杂度：O(1)。
        :param A:
        :param B:
        :return:
        '''
        if len(A) != len(B):
            return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


def main():
    solution = Solution()
    A = "ab"
    B = "ba"
    print(solution.buddyStrings(A, B))
    A = "ab"
    B = "ab"
    print(solution.buddyStrings(A, B))
    A = "aa"
    B = "aa"
    print(solution.buddyStrings(A, B))
    A = "aaaaaaabc"
    B = "aaaaaaacb"
    print(solution.buddyStrings(A, B))
    A = ""
    B = "aa"
    print(solution.buddyStrings(A, B))


if __name__ == '__main__':
    main()