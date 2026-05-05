class circularqueue:
  def _init_(self,size):
    self.size=size
    self.queue=[None]*size
    self.front=-1
    self.rear=-1
  #check if queue is empty
  def is_empty(self):
    return self.front==-1
  #check if queue is full
  def is_full(self):
    return (self.rear+1)%self.size==self.front
  #enqueue
  def enqueue(self,value):
    if self.is_full():
      print("queue overflow!!! cannot insert value",value)
      return
    if self.is_empty():
      self.front=self.rear=0
    else:
      self.rear=(self.rear+1)%self.size
    self.queue[self.rear]=value
    print("value inserted:",value)
    #dequeue
  def dequeue(self):
    if self.is_empty():
      print("queue underflow!!!,nothing to delete")
      return    
    removed=self.queue[self.front]
    if self.front==self.rear:
       self.front=self.rear=-1
    else:
      self.front=(self.rear+1)%self.size
    print("deleted:",removed)
    #peek
  def peek(self):
    if self.is_empty():
      print("queue empty!!!")
    else:
      print("front element:",self.queue[self.front])
    #display
  def display(self):
    if self.is_empty():
      print("queue is empty!!!")
      return
    print("queue elements...")
    i=self.front
    while True:
      print(self.queue[i],end='')        
      if i==self.rear:
        break
      i=(i+1)%self.size
    print()

size=int(input("enter the size of circular queue:"))
cq=circularqueue(size)
while True:
  print("\n 1.enqueue 2.dequeue 3.peek 4.display 5.exit ")
  choice=int(input("enter choice:"))
  if choice==1:
    val=int(input("enter value to insert:"))
    cq.enqueue(val)
  elif choice==2:
    cq.dequeue()
  elif choice==3:
    cq.peek()
  elif choice==4:
    cq.display()
  elif choice==5:
    print("existing....")
    break
  else:
    print("invalid choice...")