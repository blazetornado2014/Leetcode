class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_str = min(str1, str2)
        long_str = max(str1, str2)

        ans = ""
        curr_substr = ""
        for c in short_str:
            curr_substr += c

            t_times_curr = len(long_str) // len(curr_substr)
            gcd_long = curr_substr * t_times_curr == long_str

            t_times_curr = len(short_str) // len(curr_substr)
            gcd_short = curr_substr * t_times_curr == short_str

            if gcd_long and gcd_short:
                ans = curr_substr

        return ans