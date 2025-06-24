import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV (use correct path method)
df = pd.read_csv(r"C:\Users\HAPPY\Downloads\archive (5)\Books.csv")

# Clean and convert data
df['pages'] = pd.to_numeric(df['pages'], errors='coerce')
df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
df['published_date'] = df['published_date'].dt.tz_localize(None)

# Top 5 authors
top_authors = df['author'].value_counts().head(5)

# Print
print("Top 5 authors:\n", top_authors)

# Plot
plt.figure(figsize=(8, 5))
top_authors.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 5 Authors by Number of Books')
plt.xlabel('Author')
plt.ylabel('Number of Books')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
