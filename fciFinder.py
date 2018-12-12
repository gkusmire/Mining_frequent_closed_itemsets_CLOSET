from Mining_frequent_closed_itemsets_CLOSET.closetAlgorithm import ClosetFCIFinder

a = ClosetFCIFinder("sample.csv", 2)

fci = a.build_frequent_closed_itemset()
d = a.dictionary
print("Zbiory zamkniete")
for x in fci.items:
    for y in x.itemset:
        print(d.dictionary[y], end=' ')
    print("FREQUENCY: ", end=' ')
    print(x.frequency)

