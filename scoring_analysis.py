"""
Medical Model Performance Analysis Script.

This script calculates the mean scores from multiple raters, aggregates the data 
by Category, Metric, and Difficulty Level across different models, and exports 
the summarized results into a formatted Excel workbook.
"""

from pathlib import Path
import sys
import pandas as pd

# --- CONSTANTS ---
INPUT_FILE = "scoring_results.xlsx"
OUTPUT_FILE = "final_thesis_analysis_results.xlsx"
RATER_COLUMNS = ["Rater_A", "Rater_B", "Rater_C"]
LEVEL_ORDER = ["Easy", "Medium", "Hard"]


def load_and_preprocess_data(file_path: str) -> pd.DataFrame:
    """Loads the Excel data and preprocesses rater scores and difficulty levels."""
    path = Path(file_path)
    if not path.exists():
        print(f"[ERROR] Input file '{file_path}' not found.")
        sys.exit(1)

    try:
        df = pd.read_excel(path)

        # Validate required columns exist in the source file
        required_cols = RATER_COLUMNS + ["Level", "Model", "Category", "Metric"]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Missing required columns in dataset: {missing_cols}")

        # Calculate mean score across all raters
        df["Mean_Score"] = df[RATER_COLUMNS].mean(axis=1)

        # Enforce logical categorical ordering for difficulty levels
        df["Level"] = pd.Categorical(
            df["Level"], categories=LEVEL_ORDER, ordered=True
        )

        return df
    except Exception as e:
        print(f"[ERROR] Failed to process data: {e}")
        sys.exit(1)


def analyze_group(
    df: pd.DataFrame, group_col: str, title: str
) -> pd.DataFrame:
    """Groups data by a specific column and 'Model', calculating the mean scores."""
    print(f"\n--- {title} ---")
    try:
        summary = df.groupby([group_col, "Model"])["Mean_Score"].mean().unstack()
        print(summary.round(2))  # Rounded to 2 decimal places for clean console output
        return summary
    except Exception as e:
        print(f"[ERROR] Failed during aggregation on '{group_col}': {e}")
        sys.exit(1)


def main():
    """Main execution flow."""
    # 1. Load and Clean Data
    df = load_and_preprocess_data(INPUT_FILE)

    # 2. Execute Analysis
    summary_category = analyze_group(
        df, "Category", "MEAN SCORE PER CATEGORY & MODEL"
    )
    summary_metric = analyze_group(df, "Metric", "MEAN SCORE PER METRIC & MODEL")
    summary_level = analyze_group(
        df, "Level", "MEAN SCORE PER DIFFICULTY LEVEL & MODEL"
    )

    # 3. Save Documentation to Excel
    try:
        with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
            summary_category.to_excel(writer, sheet_name="Per_Category")
            summary_metric.to_excel(writer, sheet_name="Per_Metric")
            summary_level.to_excel(writer, sheet_name="Per_Level")
        print(f"\n[INFO] Success! Analysis exported to '{OUTPUT_FILE}'.")
    except Exception as e:
        print(f"[ERROR] Failed to save Excel file: {e}")


if __name__ == "__main__":
    main()
