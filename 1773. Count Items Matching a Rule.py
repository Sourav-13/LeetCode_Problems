class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleNumber = -1
        if ruleKey == "type":
            ruleNumber = 0
        if ruleKey == "color":
            ruleNumber = 1
        if ruleKey == "name":
            ruleNumber = 2
        count = 0

        for item in items:
            if item[ruleNumber] == ruleValue:
                count += 1
        return count        