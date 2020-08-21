
language = "python3"
run = "HackerRank.doc/30_days_challenges.doc/Day_18_Stack_and_Queues"

'''
Problem:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you
 determine if a given string, is a palindrome?
We must first take each character in, enqueue it in a queue, and also push that same character onto a stack. Once that's done,
 we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to
 see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until
 our containers are empty (a non-match meansisn't a palindrome).

Input Format
You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string. It
 then calls the methods specified above to pass each character to your instance variables.
Constraints
    is composed of lowercase English letters.
Output Format
You are not responsible for printing any output to stdout.
If your code is correctly written and
is a palindrome, the locked stub code will print ; otherwise, it will print
Sample Input
racecar
Sample Output
The word, racecar, is a palindrome.
'''

# Solution
import sys

class Solution:

    def __init__(self):
        self.dequeue = -1
        self.pop = -1
        self.stack = str()
        self.queue = str()

    def pushCharacter(self, s):
        self.stack = s + self.stack


    def enqueueCharacter(self, q):
        self.queue += q


    def popCharacter(self):
        self.pop += 1
        return self.stack[self.pop]

    def dequeueCharacter(self):
        self.dequeue += 1
        return self.queue[self.dequeue]

# read the string s
s=input("Introduce a word:")
s = s.lower()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")