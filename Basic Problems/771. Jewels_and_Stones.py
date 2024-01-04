class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        characters_list_jewels = list(jewels)
        characters_list_stones = list(stones)

        len_jewel = len(characters_list_jewels)
        len__stone = len(characters_list_stones)

        counter = 0

        if len_jewel <= len__stone:
            for i in range(min(len_jewel, len__stone)):
                for j in range(max(len_jewel, len__stone)):
                    if characters_list_jewels[i] == characters_list_stones[j]:
                        counter = counter + 1
        elif len_jewel > len__stone:
            for i in range(max(len_jewel, len__stone)):
                for j in range(min(len_jewel, len__stone)):
                    if characters_list_jewels[i] == characters_list_stones[j]:
                        counter = counter + 1

        return counter