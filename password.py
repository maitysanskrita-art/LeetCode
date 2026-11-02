
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)

        missing = 3 - (lower + upper + digit)

        replace = 0
        one = 0
        two = 0

        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                replace += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

            i = j

        if n < 6:
            return max(6 - n, missing)

        elif n <= 20:
            return max(missing, replace)

        else:
            delete = n - 20

            use = min(delete, one)
            replace -= use
            delete -= use

            use = min(delete // 2, two)
            replace -= use
            delete -= use * 2

            replace -= delete // 3

            return (n - 20) + max(missing, replace)
