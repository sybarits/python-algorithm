# 가장 긴 팬린드롬 부분 문자열을 출력하라.

class LongestPalindromeSubstring:

    def solution(self, s: str) -> str:
        result = ""
        length = 2

        while length <= len(s):
            for start in range(len(s)):
                if start+length > len(s):
                    break
                s_sub = s[start: start+length]
                if s_sub == s_sub[::-1] and len(result) < len(s_sub):
                    result = s_sub
            length += 1

        return result

if __name__ == "__main__":
    s = "babad"
    lps = LongestPalindromeSubstring()
    print("result is", lps.solution(s))
    ss = "123454321"
    print("result is", lps.solution(ss))
