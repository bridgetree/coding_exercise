def firstUniqChar(self, s):
        if s == "":
              return -1
          dict = {}
          for i in s:
              if i in dict.keys():
                  dict[i] += 1
              else:
                  dict[i] = 1

          cnt = 0
          for i in s:
              if dict[i] == 1:
                  return cnt
              cnt += 1
          return -1
