with open('pi-10million.txt', 'r') as file:
  pi = file.read()
  if True:
    inp = input("Enter a number: ") 
    while inp.isnumeric():
      index = pi.find(inp)
      if index == -1:
        print("Not found") 
      else:
        print(f"It is located at the {index+1}. digit after the comma.")
      inp = input("Enter a number: ")
