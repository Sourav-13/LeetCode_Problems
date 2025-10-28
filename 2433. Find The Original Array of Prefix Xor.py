class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ansList= [pref[0]]
        for i in range(1, len(pref)):
            ansList.append(pref[i-1] ^ pref[i])
        return ansList
