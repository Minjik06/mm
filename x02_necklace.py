#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  a=int(a)
  b=int(b)
  c= [a,b]
  p=f"{c[-2]}{c[-1]}"  
  while True:
    if c[-1]+c[-2]<10:
      c.append(c[-1]+c[-2])
      p=f"{p}{c[-1]}"
      if c[-1]==b and c[-2]==a:
        print(p)
        return p
    elif c[-1]+c[-2]>=10:
      d=c[-1]+c[-2]
      e=1+(d-10)
      c.append(e)
      p=f"{p}{c[-1]}"
      if c[-1]==b and c[-2]==a:
        print(p)
        return p
    
  
  
def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
  
  
  """while True:
    if c[i]+c[i+1]<10:
      c.append(c[i]+c[i+1])
      print(c)
      i+=1
      if c[-1]==b and c[-2]==a:
        break
    elif c[i]+c[i+1]>=10:
      d=c[i]+c[i+1]
      e=1+(d-10)
      c.append(e)
      print(c)
      i+=1
      if c[-1]==b and c[-2]==a:
        break"""

  """for i in c:
      print(i-1)"""
    

  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """
