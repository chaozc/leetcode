# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf = [None for _ in range(4)]
        self.n_buf = 0
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        eof = False
        buffer = ['' for _ in range(4)]
        
        for read_bytes in range(min(self.n_buf, n)):
            buf[read_bytes] = self.buf[read_bytes]
        read_bytes = min(self.n_buf, n)
        
        for i in range(self.n_buf-read_bytes):
            self.buf[i] = self.buf[i+read_bytes]
        self.n_buf -= read_bytes
        
        while not eof and n > read_bytes:
            size = read4(buffer)
            if size < 4:
                eof = True
            bytes = min(n - read_bytes, size)
            for i in range(bytes):
                buf[read_bytes + i] = buffer[i]
            read_bytes += bytes
            for i in range(bytes, size):
                self.buf[self.n_buf] = buffer[i]
                self.n_buf += 1
        return read_bytes