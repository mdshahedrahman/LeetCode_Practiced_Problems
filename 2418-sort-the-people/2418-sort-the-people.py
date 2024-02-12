class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_height = sorted(heights, reverse = True)
        temp = []
        temp2 = []
        for i in sorted_height:
            index_max = heights.index(i)
            temp2.append(index_max)

        for i in temp2:
            temp.append(names[i])
        
        return temp 