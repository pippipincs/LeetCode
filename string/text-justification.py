class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ## assign to lines
        def assign_to_line(i):
            current_line = []
            length = -1
            while length <= maxWidth and i < len(words):
                if length + len(words[i]) + 1 <= maxWidth:
                    length += len(words[i]) + 1
                    current_line.append(words[i])
                    i  += 1
                else:
                    break
            return current_line
        ## padding
        def pad(line, i):
            length = -1
            for word in line:
                length += len(word) + 1
            extra_spaces = maxWidth - length
            if len(line) == 1 or i == len(words):
                line[-1] += " " * extra_spaces
                return " ".join(line)
            intervals = len(line) -1
            spaces_per_interval = extra_spaces // intervals
            extra_counts = extra_spaces % intervals
            for i in range(intervals):
                line[i] += " " * spaces_per_interval
            for i in range(extra_counts):
                line[i] += " "
            return " ".join(line)
        
        ## main
        i = 0
        ans = []
        while i < len(words):
            line = assign_to_line(i)
            i += len(line)
            ans.append(pad(line, i))
        return ans
            