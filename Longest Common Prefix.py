class Solution:
    def longestCommonPrefix(self, strs):
        answer = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word):
                    return answer
                elif word[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer
    

def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["ab", "a"]))
    

main()
