# class Solution:
#     def solve(self, text, key):
#         cip = []
#         start = ord('a')
#         print(start)
#         for l, k in zip(text, key):
#             shift = ord(k) - start
#             pos = start + (ord(l) - start + shift) % 26
#             cip.append(chr(pos))
#         return ''.join([l for l in cip])
#
#
# ob = Solution()
# text = "deepak"
# key = "team"
# print(ob.solve(text, key))

txt = input("Enter the message: ")
txt = list(txt)
print(txt)
key = input("Enter the key: ")
print(len(key))
l1 = []
print(key[0])
count = 0
for i in range(len(txt)):
    l1.append(key[count])
    count = count + 1
    if count > len(key)-1:
        count = 0

print(l1)

