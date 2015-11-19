import Queue
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        q = Queue.Queue()
        q.put((x,y))
        image[x][y] = '.'
        mix = x
        miy = y
        mx = x
        my = y
        while not q.empty():
            (x, y) = q.get()
            for d in dir:
                nx = x+d[0]
                ny = y+d[1]
                if nx > -1 and nx < len(image) and ny > -1 and ny < len(image[0]):
                    if image[nx][ny] == '1':
                        mix = min(mix, nx)
                        miy = min(miy, ny)
                        mx = max(mx, nx)
                        my = max(my, ny)
                        image[nx][ny] = '.'
                        q.put((nx,ny))
        return (mx-mix+1)*(my-miy+1)