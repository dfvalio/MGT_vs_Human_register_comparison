import pandas as pd

input_file = "svm_results_summary.tsv"
output_file = "svm_results_feature_all.tsv"

# Load TSV
df = pd.read_csv(input_file, sep="\t")

# Keep only rows where feature_set == all
filtered = df[
    df["feature_set"] == "all"
]

# Save
filtered.to_csv(
    output_file,
    sep="\t",
    index=False
)

print("Saved:", output_file)
print(filtered.shape)
print(filtered[["experiment", "feature_set", "domain"]])