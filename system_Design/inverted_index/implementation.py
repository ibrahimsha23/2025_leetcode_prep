from collections import defaultdict

data_warehouse = {
    'Doc1': 'apple banana orange',
    'Doc2': 'banana apple apple',
    'Doc3': 'orange banana',
}

inverted_index = defaultdict(list)

for doc_id, doc_data in data_warehouse.items():
    tokens = set(doc_data.split())
    for ele in tokens:
        inverted_index[ele].append(doc_id)

print(inverted_index)
