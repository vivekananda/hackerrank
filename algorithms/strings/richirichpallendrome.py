# !/bin/python

import sys

# https://www.hackerrank.com/challenges/richie-rich

"""
Sandy likes palindromes. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as it does forward. For example, madam is a palindrome.

On her  birthday, Sandy's uncle, Richie Rich, offered her an -digit check which she refused because the number was not a palindrome. Richie then challenged Sandy to make the number palindromic by changing no more than  digits. Sandy can only change  digit at a time, and cannot add digits to (or remove digits from) the number.

Given  and an -digit number, help Sandy determine the largest possible number she can make by changing digits.

Note: Treat the integers as numeric strings. Leading zeros are permitted and can't be ignored (So 0011 is not a palindrome, 0110 is a valid palindrome). A digit can be modified more than once.

Input Format

The first line contains two space-separated integers,  (the number of digits in the number) and  (the maximum number of digits that can be altered), respectively.
The second line contains an -digit string of numbers that Sandy must attempt to make palindromic.

Constraints

Each character  in the number is an integer where .
Output Format

Print a single line with the largest number that can be made by changing no more than  digits; if this is not possible, print -1.

Sample Input 0

4 1
3943
Sample Output 0

3993
Sample Input 1

6 3
092282
Sample Output 1

992299
Sample Input 2

4 1
0011
Sample Output 2

-1
Explanation

Sample 0

There are two ways to make  a palindrome by changing exactly  digits:

, so we print

"""

n, k = 7, 6
number = "0923282"
# n ,k = raw_input().strip().split(' ')
# n ,k = [int(n) ,int(k)]
# number = raw_input().strip()

li = [int(el) for el in list(number)]
original_li = [int(el) for el in list(number)]
# print "len", len()
for i in range(n / 2):
    if li[i] != li[n - 1 - i]:
        # use the number that is bigger
        if int(li[i]) > int(li[n - 1 - i]):
            li[n - 1 - i] = li[i]
        else:
            li[i] = li[n - 1 - i]
        k -= 1
    if k < 0:
        break
i = 0
max_i = n / 2 + 1
while k > 0 and i > max_i:
    change_req = 0
    if li[i] != 9:
        if li[i] != original_li[i] or li[n - 1 - i] != original_li[n - 1 - i] or i == n - 1 - i:
            change_req = 1
        else:
            change_req = 2

    if 0 < change_req <= k:
        li[i] = 9
        li[n - i - 1] = 9
        k -= change_req
    i += 1

if k < 0:
    print -1
else:  # k will be greater than or equal to 0 in case of success
    print "".join([str(el) for el in li])
