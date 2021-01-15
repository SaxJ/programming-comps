class Solution:
    def tableItemCounts(self, items, tableCounts):
        output = []
        for item in items:
            output.append(str(0) if item not in tableCounts else str(tableCounts[item]))
        return output

    def displayTable(self, orders):  # [[string]] -> [[string]]
        counts = {}
        items = set()
        for order in orders:
            _, table, item = order
            if table not in counts:
                counts[table] = {}
            if item not in counts[table]:
                counts[table][item] = 0
            counts[table][item] += 1
            items.add(item)
        output = []
        items = sorted(list(items))
        output.append(["Table", *items])
        for table in sorted(list(counts.keys()), key=int):
            output.append([table, *self.tableItemCounts(items, counts[table])])
        return output
