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
    #print("match,proc", char, num)
    tmp_item = self.peek()
    if len(tmp_item) > 0 and [tmp_item[0], char] in match_symbols:
      #print("match,out", tmp_item[0], char)
      self.pop()
      if num != tmp_item[1]:
        return tmp_item[1]
      else:
        return -1
    else:
      #print("match,in", char, num)
      self.push([char, num])
      return -1

def proc_indent(lines, tabsize = 4):
  i = 0
  #list ts_list
  #ts_list第几行要用几个缩进
  ts_list = list()
  symbol_stack = Stack()

  for line in lines:
      #print("==%s", line)
      ts_list.append(0)
      j = 0
      for word in line:
          if word in symbols:
              match_line = symbol_stack.proc(word, i)
              #print("return match_line", match_line, i)
              if match_line == -1:
                  continue
              for k in range(match_line+1, i+1):
                  #print("add to ts_list", k)
                  ts_list[k] += 1
          j += 1
      i += 1

  n = 0
  alltext = []
  newline = list()
  for line in lines:
      space_str = ""
      cnt = ts_list[n]
      #print("xxxxx = %d,%d", n, cnt)
      for m in range(cnt * tabsize):
          #print("===%d", n)
          space_str = " " + space_str
      newline = "%s%s" % (space_str, line.lstrip())
      if (len(alltext) == 0):
          alltext = "%s\n" % (newline)
      else:
          alltext = "%s%s\n" % (alltext, newline)
      #print(newline)
      n += 1
  return alltext
    
if __name__ == "__main__":
  file = open("data.txt", 'r', encoding='UTF-8')
  lines = file.readlines()
  text = proc_indent(lines)
  print("finish \n proc_indent")
  print(text)
  file.close()
