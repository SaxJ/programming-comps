class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        last_count = 0
        beams = 0
        for line in bank:
            devs = line.count("1")
            if devs > 0:
                beams += last_count * devs
                last_count = devs
        return beams
        
