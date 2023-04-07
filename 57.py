# LeetCode
# 57. Insert Interval
# Medium
# https://leetcode.com/problems/insert-interval/
# Array

def insert(intervals, newInterval):
    indexs = set()

    for x, interval in enumerate(intervals):
        print(x, interval, newInterval)
        if interval[1] >= newInterval[0]:
            print('Here', interval)
            indexs.add(x)

    for x, interval in enumerate(intervals):
        print(x, interval, newInterval)
        if interval[0] <= newInterval[1]:
            print('There', interval)
            indexs.add(x)

    print(indexs)

    return None


print(insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
