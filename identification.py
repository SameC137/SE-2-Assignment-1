
class identifier:
    def __init__(self):
        self.findBird()
    def findBird(self):
        answer=input("Does it have a long beak?")
        if(answer=="yes" or answer =="Yes"):
            answer=input("Is the beak 1.wide,2. skinny or 3.spoon/shovel-shaped?(Please state the number)")
            if(answer=="1"):
                answer=input("Are the maincolors 1. black and yelow or 2.any other color?")
                if(answer=="1"):
                    print("The bird is a Keel-billed toucan")
                else:
                    print("It is a Curl-crested aracari")
            elif(answer=="2"):
                answer=input("Are the maincolors 1. red/pink or 2.white/grey?")
                if(answer=="1"):
                    print("The bird is a Scarlet ibis")
                else:
                    print("The bird is a White ibis")
            else:
                print("The bird is a Roseate spponbill")     
        else:
            answer=input("Is the bird shaped 1. short and squat or 2. Tall and thin?(Please type the number)")
            if(answer=="1"):
                answer=input("Does it have webbed feet?")
                if(answer=="yes" or answer=="Yes"):
                    answer=input("What shape is the birds beak 1.wide for diving or 2. narrow for dabbling?")
                    if(answer=="1"):
                        print("The bird is Ruddy duck")
                    else:
                        print("The bird is Blue-winged teal")
                else:
                    answer=input("What color is the birds plumage 1. black 2. brown?")
                    if(answer=="1"):
                        print("The bird is Blue-throated piping guan")
                    else:
                        print("The bird is Andean tinamou")
            else:
                answer=input("what color is the birds beak 1.yellow 2.othercolor?")
                if(answer=="1"):
                    print("The bird is Green Winged mackaw")
                else:
                    print("The bird is Crested oropendola")
identifier()   
       
