# NH 2nd writing to csv files notes
"""with open("notes\\sample.txt", 'a') as file:
    file.write("\nJoe\n")
    file.write("Israel\n")
    file.write("Zee\n")

print("Run finished")"""
"""content = []
with open("notes/sample.txt", 'r+') as file:
    for line in file:
        content.append(line.strip())
        
    index = content.index('Tia')
    content[index] = "Torii"

    file.truncate(0)
    for name in content:
        file.write(name + "\n")

print("Code ends")"""


import csv
"""with open("notes/test.csv", 'w', newline='') as csvfile:
    fieldnames = ['name', 'Radiant']
    writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
    writer.writerow(["name1", "edge_dancer"])
    writer.writerow(["name2", "truth_watcher"])"""
with open("notes/test.csv", 'a', newline='') as csvfile:
    fieldnames = ['name', 'Radiant']
    writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
    writer.writerow(["name1", "edge_dancer"])
    writer.writerow(["name2", "truth_watcher"])