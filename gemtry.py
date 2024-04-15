import pandas as pd
from mlxtend.frequent_patterns import apriori

# Load your preprocessed data into a pandas DataFrame
data = pd.read_csv("buildsfinal2.csv")

# Define a function to prepare the data for association rule learning
def prepare_data(data):
  # Extract relevant component selections (CPU-Motherboard, CPU-GPU, etc.)
  # This might involve combining columns or creating new features
  transactions = data[["CPU", "Motherboard"]]  # Example for CPU-Motherboard pairs
  return transactions.tolist()

# Prepare transactions from your data
transactions = prepare_data(data)

# Define minimum support threshold (e.g., how frequent a combination must be)
min_support = 0.05

# Generate frequent itemsets using apriori algorithm
frequent_itemsets = apriori(transactions, min_support=min_support, use_colnames=True)

# Extract association rules from frequent itemsets
association_rules = frequent_itemsets.sort_values(by=["support", "lift"], ascending=[False, False])

# Define a function to recommend components based on user selections
def recommend_component(selected_components, association_rules):
  # Filter rules where the antecedent matches user selections
  filtered_rules = association_rules[association_rules["antecedents"].apply(lambda x: set(x) <= set(selected_components))]
  # Select the rule with the highest confidence
  if not filtered_rules.empty:
    top_rule = filtered_rules.iloc[0]
    return top_rule["consequents"].tolist()[0]  # Recommend the consequent component
  else:
    return None  # No recommendation found

# Example usage: User selects a CPU
selected_cpu = "Ryzen 7 7700X"

# Get motherboard recommendation
recommended_motherboard = recommend_component([selected_cpu], association_rules)

print(f"Recommended motherboard for {selected_cpu}: {recommended_motherboard}")
