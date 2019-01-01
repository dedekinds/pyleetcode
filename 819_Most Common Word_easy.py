卡无聊的输入，样例里面

from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        check = set(banned)
        count = Counter(word.strip("!?',;.") for word in paragraph.lower().split())
        print(count)
        res = ''
        max_value = 0
        for temp in count:
            if count[temp] > max_value and temp not in check:
                res = temp
                max_value = count[temp]
        return res
        