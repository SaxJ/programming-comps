class Solution:
    def checkString(self, s):
        az = [i for i in range(len(s)) if s.startswith("a", i)]
        bz = [i for i in range(len(s)) if s.startswith("b", i)]

        if len(az) == 0:
            return True

        last_a = az[-1]
        for b in bz:
            if last_a > b:
                return False
        return True
