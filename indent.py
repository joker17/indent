#!/usr/local/bin/python3

class Stack:
  """模拟栈"""
  def __init__(self):
    self.items = []
     
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

symbol_stack = Stack()

file = open("data.txt", 'r', encoding='UTF-8')
lines = file.readlines()

for line in lines:
    print(line)


print(lines[1])
file.close()