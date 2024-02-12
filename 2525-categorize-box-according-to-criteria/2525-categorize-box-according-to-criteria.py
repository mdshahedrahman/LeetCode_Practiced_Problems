class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if (length >= 10 ** 4 or width >= 10 ** 4 or
                height >= 10 ** 4 or mass >= 10 ** 4 or
                (length * width * height) >= 10 ** 9) and mass < 100:
            return ("Bulky")

        elif ((length >= 10 ** 4 or width >= 10 ** 4 or
                height >= 10 ** 4 or mass >= 10 ** 4 or
                (length * width * height) >= 10 ** 9)) and mass >= 100:
            return ("Both")

        elif ((length < 10 ** 4 or width < 10 ** 4 or
                height < 10 ** 4 or mass < 10 ** 4 or
                (length * width * height) < 10 ** 9)) and mass < 100:
            return("Neither")

        elif ((length < 10 ** 4 or width < 10 ** 4 or
                height < 10 ** 4 or mass < 10 ** 4 or
                (length * width * height) < 10 ** 9)) and mass >= 100:
            return("Heavy")