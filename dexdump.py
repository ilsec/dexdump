import sys, io
from struct import pack, unpack

class dumpDex:
    def __init__(self, fname):
        with open(fname, 'rb') as f:
            self.__buff = f.read()
    def bsearch(self, key):
        offset = 0 
        key_length = len(key)
        while True:
            try:
                c = bytearray(unpack(str(key_length) + 'c', self.__buff[offset:key_length + offset]))
                if key == c:
                    #split
                    print '========'
                    #find offset
                    print 'offset = ' + str(offset)
                    #find length
                    len_offset = offset + key_length + 4 + 20
                    length = unpack('I', self.__buff[len_offset:len_offset + 4])[0]
                    print 'length = ' + str(length)
                    #print '========'
                    
                    #write file
                    with open(str(offset) + '.dex', mode='wb+') as f:
                        f.write(self.__buff[offset:offset + length])  
                                            
                    #find next
                    offset = offset + length
                    continue
                else:
                    offset = offset + 1
            except:
                break
            
if __name__ == '__main__':
    d = dumpDex(sys.argv[1])
    key = bytearray(b'\x64\x65\x78\x0a\x30\x33\x35\x00')  #dex\n035 = 64 65 78 0a 30 33 35 00
    d.bsearch(key)