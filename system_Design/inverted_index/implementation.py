data_warehouse = {
    'Doc1': 'apple banana orange',
    'Doc2': 'banana apple apple',
    'Doc3': 'orange banana',
}
inverted_index = {
}

for doc_id, doc_data in data_warehouse.items():
    print(doc_id, doc_data)
    tokens = doc_data.split()
    for ele in set(tokens):
        ele = ele.strip()
        print(ele)
        if ele in inverted_index:
            inverted_index[ele].append(doc_id)
        else:
            inverted_index[ele] = [doc_id]

print(inverted_index)
