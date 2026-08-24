class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #   5#words
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res

        # 5#words
        # j = 1
        # length = s[0:1] not including 1 = int('5')
        # append(s[1 + 1: 1 + 1 + 5])
        #



