class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        word_length = len(words[0])
        string_length = len(s)
        k = len(words)
        words_count = collections.Counter(words)
        if k * word_length > len(s):
            return answer
        def windowsliding(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess = False
            for right in range(left, string_length, word_length):
                if right + word_length > string_length:
                    break
                sub = s[right : right + word_length]
                if sub in words:
                    while right - left == k * word_length or excess :
                        left_word = s[left : left + word_length]
                        left = left + word_length
                        words_found[left_word] -= 1

                        if words_found[left_word] == words_count[left_word]:            
                            excess = False
                        else:
                            words_used -= 1


                    words_found[sub] += 1
                    
                    if words_found[sub] > words_count[sub]:
                        excess = True
                        continue
                    words_used += 1
                    if words_used == k:
                        answer.append(left)
                else:
                    left = right + word_length
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess = False
        for i in range(word_length):
                windowsliding(i)
        return answer

