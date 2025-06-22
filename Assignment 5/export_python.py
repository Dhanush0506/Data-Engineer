import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
import matplotlib.pyplot as plt
import os

# Sample data
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85.5, 90.0, 78.2]
})

# Create export folder
os.makedirs("exports", exist_ok=True)

# Export to CSV
df.to_csv("exports/sample_data.csv", index=False)

# Export to Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, "exports/sample_data.parquet")

# Export to Avro
schema = {
    "doc": "Sample schema",
    "name": "Record",
    "namespace": "example.avro",
    "type": "record",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
records = df.astype(str).to_dict(orient="records")
with open("exports/sample_data.avro", "wb") as out:
    fastavro.writer(out, schema, records)

# Generate Graph
plt.bar(df['name'], df['score'], color='skyblue')
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Individuals')
plt.tight_layout()
plt.savefig("exports/sample_graph.png")

