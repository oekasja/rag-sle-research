"""
Gwet's AC2 Inter-Rater Reliability Calculator.

This script computes Gwet's AC2 agreement coefficient with linear weighting 
for 1-5 Likert scale data across multiple raters and models.
"""

from pathlib import Path
import sys
import numpy as np
import pandas as pd

# --- CONSTANTS ---
INPUT_FILE = "scoring_results.xlsx"
RATER_COLUMNS = ["Rater_A", "Rater_B", "Rater_C"]
NUM_CATEGORIES = 5  # Likert scale 1 to 5


def calculate_gwet_ac2_linear(
    df_ratings: pd.DataFrame, num_categories: int = 5
) -> float:
    """Calculates Gwet's AC2 with linear weighting for ordinal ratings."""
    ratings = df_ratings.values
    num_subjects, num_raters = ratings.shape

    if num_raters < 2:
        raise ValueError("Gwet's AC2 requires at least 2 raters.")

    # 1. Generate Linear Weights Matrix
    # Closer ratings receive partial agreement credit
    weights = np.zeros((num_categories, num_categories))
    for i in range(num_categories):
        for j in range(num_categories):
            weights[i, j] = 1 - abs(i - j) / (num_categories - 1)

    # 2. Compute category distribution per subject (frequency table)
    frequencies = np.zeros((num_subjects, num_categories))
    for i in range(num_subjects):
        for j in range(num_raters):
            val = ratings[i, j]
            if pd.isna(val):
                continue
            val_idx = int(val) - 1
            if 0 <= val_idx < num_categories:
                frequencies[i, val_idx] += 1

    # 3. Calculate Observed Agreement (Pa)
    pa_sum = 0
    for i in range(num_subjects):
        row_sum = 0
        for k in range(num_categories):
            for l in range(num_categories):
                adjustment = 1 if k == l else 0
                row_sum += (
                    weights[k, l]
                    * frequencies[i, k]
                    * (frequencies[i, l] - adjustment)
                )
        pa_sum += row_sum / (num_raters * (num_raters - 1))
    observed_agreement = pa_sum / num_subjects

    # 4. Calculate Chance Agreement (Pe)
    classification_prob = frequencies.sum(axis=0) / (num_subjects * num_raters)
    chance_agreement = 0
    for k in range(num_categories):
        for l in range(num_categories):
            chance_agreement += (
                weights[k, l] * classification_prob[k] * classification_prob[l]
            )

    # 5. Compute Final Gwet's AC2
    if chance_agreement >= 1.0:
        return 1.0

    ac2 = (observed_agreement - chance_agreement) / (1 - chance_agreement)
    return float(ac2)


def main():
    """Main execution flow."""
    path = Path(INPUT_FILE)
    if not path.exists():
        print(f"[ERROR] Input file '{INPUT_FILE}' not found.")
        sys.exit(1)

    try:
        df = pd.read_excel(path)

        # Validate that required columns exist
        required_cols = RATER_COLUMNS + ["Model"]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Missing required columns in dataset: {missing_cols}")

        print("=" * 65)
        print(f"{'ANALYSIS GROUP':<35} | {'GWET AC2 (Linear)':<20}")
        print("-" * 65)

        # 1. Overall Global Reliability
        global_score = calculate_gwet_ac2_linear(
            df[RATER_COLUMNS], NUM_CATEGORIES
        )
        print(f"{'OVERALL GLOBAL':<35} | {global_score:.4f}")

        # 2. Reliability Per Sub-Model
        for model_name in df["Model"].dropna().unique():
            subset = df[df["Model"] == model_name]
            model_score = calculate_gwet_ac2_linear(
                subset[RATER_COLUMNS], NUM_CATEGORIES
            )
            print(f"{f'Model: {model_name}':<35} | {model_score:.4f}")

        print("=" * 65)
        print(
            "Interpretation: >0.80 (Very Strong), 0.60-0.80 (Strong), 0.40-0.60 (Moderate)"
        )

    except Exception as e:
        print(f"[ERROR] Failed to execute analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
