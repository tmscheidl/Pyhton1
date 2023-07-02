fnames = ["file7.txt", "file1.png", "file3.txt", "file2.txt",
          "file7.txt", "file1.txt", "file3.txt", "file4.png",
          "file4.png", "file5.txt", "file0.txt", "file7.dat"]
fname=[]

for i in fnames:
    
    if i.endswith("txt") == True:
        fname.append(i)
        
new_fnames = set(fname)
new_fnames = list(new_fnames)
new_fnames.sort()
print(new_fnames)
