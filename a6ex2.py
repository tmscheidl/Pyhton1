def write_dict(d: dict, path: str, encoding: str = "utf-8"):
     with open(path, 'w') as f: 
        for key, value in d.items(): 
            f.write('%s:%s\n' % (key, value))
        return
    
    
def read_dict(path: str, encoding: str = "utf-8") -> dict:
    d = {}
    with open(path, 'r') as f: 
        for line in f:
            #s="".join([l.rstrip("\n") for l in line])
            #str(s)
            s =line.replace('\n', '')
            (key, value) = s.split(":")
            d[key] = value

        return d
        
    
some_dict = {'Name' : "Volkswagen Beetle",
         'Manufacturer' : "Volkswagen",
         'First Production' : "1938",
         'Designer' : "Ferdinand Porsche"}

write_dict(some_dict,"/Users/tomi/Documents/jku/jelenlegi feladat/Programing in Python I/Assigments/6/try1.txt")
print(some_dict)
print(read_dict("/Users/tomi/Documents/jku/jelenlegi feladat/Programing in Python I/Assigments/6/try1.txt"))


some_dict == d
