# LeetCode
# 1108
# Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        