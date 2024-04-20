#Exercises for 13_Read_Write_files
#1
wordstats = {}

with open("/workspaces/PythonExercises/poem.txt","+r") as f:
    tokens = [line.split(' ') for line in f]
    for line in tokens:
        for word in line:
            if word in wordstats:
                wordstats[word]+=1
            else :
                wordstats[word]=1

counts = wordstats.values()
max_count = max(counts)
value = [i for i in wordstats if wordstats[i]==max_count]
print(f'The word that occured the most is {value[0]} and it occured {wordstats[value[0]]} times')
#2

with open("/workspaces/PythonExercises/stocks.csv","r") as f, open("/workspaces/PythonExercises/output.csv","w") as o :
    #This would be SO much faster with pandas, but i will hold off for sake of base file io
    CompanyName = []
    price = []
    eps = []
    book_value = []
    pe_ratio :list[float] = []
    p2br :list[float] = []
    header = f.readline().split(',')
    rows = [line.split(',') for line in f]
    o.write("Company Name, PE Ratio, PB Ratio \n")
    for row in rows:
        CompanyName.append(row[0])
        price.append(int(row[1]))
        eps.append(int(row[2]))
        book_value.append(int(row[3]))
    for p in price:
        pe_ratio.append(round(p/eps[price.index(p)],2)) 
        p2br.append(round(p/book_value[price.index(p)],2))
        x = price.index(p)
        o.write(CompanyName[x]+","+str(pe_ratio[x])+","+str(p2br[x])+"\n")
    #pe_ratio = price/eps
    #p2br = price/book_value




