class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def helper(ip, index, k):
            if index == len(s) and k ==0:
                res.append(".".join(ip))
                return
            if k == 0:
                return
            if index == len(s):
                return
            for i in range(index, len(s)):
                single = s[index : i + 1]
                if int(single) < 0 or int(single) > 255:
                    continue
                if single[0] == '0' and int(single) != 0:
                    continue
                ip.append(single)
                helper(ip, i + 1, k - 1)
                ip.pop()
        helper([], 0, 4)
        return res