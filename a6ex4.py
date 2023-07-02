import os
from os import walk

def chunks(path: str, size: int, **kwargs):
    
    x = 0
    parts =[]
    if os.path.isfile(path) == False: 
        parts.append("ValueError")
        return parts
    else:
        if size <= 1:
            parts.append("ValueError")
            return parts
        else:
            with open(path) as f:
                s = " ".join([l.rstrip("\n") for l in f])
                for i in s: 
                    part = s[x:size+x]
                    parts.append(part)
                    x+=size
                    if x >= len(s):
                        break
                return parts
                                
for i, c in enumerate(chunks("ex1_data.txt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")
