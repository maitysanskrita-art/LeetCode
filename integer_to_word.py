class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        ones = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            result = []

            # Hundreds place
            if n >= 100:
                result.append(ones[n // 100])
                result.append("Hundred")
                n = n % 100

            # Numbers from 20 to 99
            if n >= 20:
                result.append(tens[n // 10])
                n = n % 10

            # Numbers from 0 to 19
            if n > 0:
                result.append(ones[n])

            return " ".join(result)

        result = []

        # Billions
        if num >= 1_000_000_000:
            result.append(convert(num // 1_000_000_000))
            result.append("Billion")
            num = num % 1_000_000_000

        # Millions
        if num >= 1_000_000:
            result.append(convert(num // 1_000_000))
            result.append("Million")
            num = num % 1_000_000

        # Thousands
        if num >= 1_000:
            result.append(convert(num // 1_000))
            result.append("Thousand")
            num = num % 1_000

        # Remaining number
        if num > 0:
            result.append(convert(num))

        return " ".join(result)