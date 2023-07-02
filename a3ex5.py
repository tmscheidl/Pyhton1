import pprint


print("Welcome to Powerlifting Data Collector!")
print("\n")
print("Available actions:")
print("a - Add lifter")
print("r - Remove lifter")
print("u - Update lifter")
print("v - View lifters")
print("x - Exit the program")

d = {}
while True:
    x = input("Enter action: ").lower()
    if x == 'a':
        lifter = input("Enter new lifter name: ")
        
        if lifter in d:
            print("Lifter ", lifter ," already exists!")
        else:
            d[lifter] = {}
            d[lifter]["Name"] = lifter
            d[lifter]["squat"] = []
            d[lifter]["bench press"] = []
            d[lifter]["deadlift"] = []

    elif x == 'r':
        lifter = input("Enter new lifter name: ")
        
        if lifter in d:
            
            del d[lifter]
        else:
            print("Lifter ", lifter ,"does not exist!")

    elif x == 'u':
        lifter = input("Enter new lifter name: ")
        
        if lifter in d:
            u = input("Enter lift (one of 'squat', 'bench press', 'deadlift'):")
            
            if u == 'squat':
                squat = input()
                d[lifter]["squat"] = squat
                
            elif u == 'bench press':
                bench_press = input()
                d[lifter]["bench press"] = bench_press
                
            elif u == 'deadlift':
                deadlift = input()
                d[lifter]["deadlift"] = deadlift
            else:
                print("Invalid action '",u,"'. Try again!")
                
        else:
            print("Lifter ", lifter ,"does not exist!")
            
    elif x == 'v':
        for v, p in d.items():
            print("------------------------------")
            for key in p:
            #print(*d[v].items() ,sep='\n')            
                print(key + ':', p[key])
            print("\n")
           # print(d)
        
    elif x == 'x':
        print("Bye!")
        break
    else:
        print("Invalid action '",x,"'. Try again!")
