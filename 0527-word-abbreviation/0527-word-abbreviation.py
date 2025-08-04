from collections import defaultdict

class Solution:
    def wordsAbbreviation(self, words):
        n = len(words)
        prefix_len = [1] * n  # start with prefix of length 1
        res = [''] * n

        def abbreviate(word, pre_len):
            if len(word) - pre_len - 1 <= 1:
                return word  # abbreviation not shorter than word
            return word[:pre_len] + str(len(word) - pre_len - 1) + word[-1]

        while True:
            abbr_map = defaultdict(list)
            for i, word in enumerate(words):
                abbr = abbreviate(word, prefix_len[i])
                abbr_map[abbr].append(i)

            unique = True
            for abbr, indices in abbr_map.items():
                if len(indices) > 1:
                    unique = False
                    for idx in indices:
                        prefix_len[idx] += 1
            if unique:
                break

        for i, word in enumerate(words):
            abbr = abbreviate(word, prefix_len[i])
            res[i] = abbr

        return res
