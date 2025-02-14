class Solution:
    def fractionAddition(self, expression):
        """
        Manual parsing

        For each operation:
        num1/denom1 + num2/denom2 = (num1*denom2 + num2*denom1)/(denom1 * denom2)

        For result:
        numerator / denominator = (numerator/gdm) / (denominator/gdm)

        Time O(n)
        Space O(1)
        """
        num = 0
        denom = 1

        i = 0
        while i < len(expression):
            curr_num = 0
            curr_denom = 0

            is_negative = False

            # check for sign
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    is_negative = True
                # move to next character
                i += 1

            # build numerator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_num = curr_num * 10 + val
                i += 1

            if is_negative:
                curr_num *= -1

            # skip divisor
            i += 1

            # build denominator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_denom = curr_denom * 10 + val
                i += 1

            # add fractions together using common denominator
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        # reduce fractions with greatest common denominator
        gcd = abs(math.gcd(num, denom))
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"