from tqdm import tqdm

# Generate SQL script for inserting 100 rows with progress bar
rows = []
for i in tqdm(range(1000000, 10000000), desc="Generating SQL Script"):
    low_fats = 'Y' if i % 2 == 0 else 'N'  # Alternate between 'Y' and 'N'
    recyclable = 'Y' if i % 3 == 0 else 'N'  # Alternate based on modulo 3
    rows.append(
        f"INSERT INTO test.\"Products\" (product_id, low_fats, recyclable) VALUES ('{i}', '{low_fats}', '{recyclable}');"
    )

# Combine the rows into a single script
sql_script = "\n".join(rows)

# Save to a file
with open("products_insert_script.sql", "w") as file:
    file.write(sql_script)

print("SQL script saved to products_insert_script.sql")
