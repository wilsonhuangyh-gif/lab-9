# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            storage = nums[i] + nums[j]
            if target == storage:
                return[i,j]

def max_profit(prices):
    # Outline:
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1,len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


def max_subarray(nums):
    # Outline:
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    best = nums[0]
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            best = max(best, total)
    return best


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    brackets = {"(" : ")","[" : "]","{" : "}" }
    stack = []
    for c in s:
        if c in brackets:                
            stack.append(brackets[c])
        elif c in ")]}":
            if not stack or stack.pop() != c:
                return False
    return not stack
    


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
