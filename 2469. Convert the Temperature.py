class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        tem = []
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00
        tem += [k, f]
        return tem