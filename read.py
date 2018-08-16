import sys

print("Reading votes...\n")

voted = []
counts = {}

with open("votes.txt") as file:
    for line in file:
        line = line.strip()
        part = line.split(" - ")
        name = part[0]
        vote = part[1]
        ote = vote.replace("  ", " ")
        if name not in voted:
            voted.append(name)
            if vote not in counts:
                counts[vote] = 1
            else:
                counts[vote] += 1
        else:
            print(name + " already voted!")

print("\nFinishing to read votes...\n")
print("The results are:")

count = 1
winners = sorted(counts, key=counts.get, reverse=True)
for name in winners:
    if count < 4:
        print (str(count) + " place: " + name + " with " + str(counts[name]) + " votes.")
        count += 1
