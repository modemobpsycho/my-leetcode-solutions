from typing import Literal


class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_map: dict[int, str] = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman_numeral: Literal[''] = ""

        for base, symbol in int_to_roman_map.items():
            roman_numeral += symbol * (num // base)
            num %= base

        return roman_numeral
