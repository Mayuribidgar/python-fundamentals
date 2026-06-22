#Accept : One Parameter
# Return :Nothing

def Display(Value):
   print("Inaside the Display:",Value)
   return Display
def main():
     Ret=Display(10)
     print("Return Is:",Ret)

if __name__ =="__main__":           
   main()