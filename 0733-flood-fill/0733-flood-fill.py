class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image
        self.fill(image, sr, sc, color, old_color)
        return image
    
    def fill(self, image, sr, sc, color, old_color):
        if (sr<0) or (sr>=len(image)) or (sc>=len(image[0])) or (sc<0) :
            return;
        if (image[sr][sc] != old_color):
            return;
        image[sr][sc] = color
        self.fill(image, sr+1,sc,color,old_color)
        self.fill(image, sr-1,sc,color,old_color)
        self.fill(image, sr,sc+1,color,old_color)
        self.fill(image, sr,sc-1,color,old_color)

