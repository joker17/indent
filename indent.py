#!/usr/local/bin/python3

symbols = ['{', '}', '[', ']', '(', ')']
match_symbols = [['{', '}'], ['[', ']'], ['(', ')']]
tabsize = 4

class Stack:
  """模拟栈"""
  def __init__(self):
    self.items = [[]]
     
  def isEmpty(self):
    return len(self.items)==0

   
  def push(self, item):
    self.items.append(item)
   
  def pop(self):
    return self.items.pop() 
   
  def peek(self):
    if not self.isEmpty():
      return self.items[len(self.items)-1]
     
  def size(self):
    return len(self.items) 

  def proc(self, char, num):
    print("match,proc", char, num)
    tmp_item = self.peek()
    if len(tmp_item) > 0 and [tmp_item[0], char] in match_symbols:
      print("match,out", tmp_item[0], char)
      self.pop()
      if num != tmp_item[1]:
        return tmp_item[1]
      else:
        return -1
    else:
      print("match,in", char, num)
      self.push([char, num])
      return -1
    
file = open("data.txt", 'r', encoding='UTF-8')
lines = file.readlines()

i = 0
#list ts_list
ts_list = list()
symbol_stack = Stack()

for line in lines:
    ts_list.append(0)
    j = 0
    for word in line:
        if word in symbols:
            match_line = symbol_stack.proc(word, i)
            #print("return match_line", match_line, i)
            if match_line == -1:
                continue
            for k in range(match_line+1, i):
                #print("add to ts_list", k)
                ts_list[k] += 1
        j += 1
    i += 1

n = 0
newline = list()
for line in lines:
    space_str = ""
    cnt = ts_list[n]
    #print("xxxxx = %d,%d", n, cnt)
    for m in range(cnt * tabsize):
        #print("===%d", n)
        space_str = " " + space_str
    newline = "%s%s" % (space_str, line.lstrip())
    print(newline)
    n += 1
file.close()