from Mining_frequent_closed_itemsets_CLOSET.fptreeBuilder import FPTreeBuilder

a = FPTreeBuilder('a.csv')

t = a.get_fptree()
print(t.rootNode.childrenNodes[0].item.name)
