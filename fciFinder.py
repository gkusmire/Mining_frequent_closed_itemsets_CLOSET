# from Mining_frequent_closed_itemsets_CLOSET.fptreeBuilder import FPTreeBuilder
#
# builder = FPTreeBuilder("sample.csv", 2)
#
# tree = builder.get_fptree()
#
# items = tree.frequentItems
#
#
# for x in items.items:
#     print(builder.dictionary.dictionary[x.name])
#     print(x.frequent_counter)
#     last = x
#
#
# # print("TRANSACTION")
# # for x in transaction:
# #     print(builder.dictionary.dictionary[x])
#
# tree.print_tree(builder.dictionary)
#
# #
# # for x in tree.items_in_every_transaction.itemset:
# #     print(builder.dictionary.dictionary[x])
#
#
# print("Nowe drzewo")
# trans = []
# iii = items.get(2)
# # aaa = tree.get_frequent_sublist(iii, trans)
# print("ITEM " + builder.dictionary.dictionary[iii.name])
# #
# # for x in aaa.items:
# #     print(builder.dictionary.dictionary[x.name])
# #     print(x.frequent_counter)
# #
# # for x in trans:
# #     for y in x:
# #         print(builder.dictionary.dictionary[y], end=' ')
# #     print("")
#
# # subtree = tree.get_subtree_associated_with(iii, 2)
# # subtree.print_tree(builder.dictionary)
# #
# # for x in subtree.items_in_every_transaction.itemset:
# #     print(builder.dictionary.dictionary[x])
from Mining_frequent_closed_itemsets_CLOSET.closetAlgorithm import ClosetFCIFinder

a = ClosetFCIFinder("sample.csv", 2)

fci = a.build_frequent_closed_itemset()
d = a.dictionary
print("Zbiory zamkniete")
for x in fci.items:
    for y in x.itemset:
        print(y, end=' ')
    print(x.frequency)

