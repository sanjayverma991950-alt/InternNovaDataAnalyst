"""
InternNova Data Analytics Internship - Week 4
Master Orchestration Script: Run All Tasks 1 to 9
Student Name: Sanjay Kumar
Course: Python for Data Analytics & AI
"""

import sys
import os
import time

def print_banner(title):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80 + "\n")

def main():
    start_time = time.time()
    print_banner("INTERNNOVA WEEK 4: COMPLETE ASSIGNMENT PIPELINE EXECUTION")
    print("Student Name: Sanjay Kumar")
    print("Assignment  : Week 4 - Statistics, Data Visualization & EDA")
    print("Max Marks   : 100 / 100")
    print("-" * 80)

    # Import and run each task module
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)

    import task1_mean_median_mode
    import task2_variance_std
    import task3_correlation_probability
    import task4_outlier_detection
    import task5_matplotlib_visualizations
    import task6_seaborn_visualizations
    import task7_eda_inspection_cleaning
    import task8_eda_correlation_insights
    import task9_business_recommendations

    tasks = [
        ("Task 1: Mean, Median & Mode", task1_mean_median_mode.analyze_central_tendency),
        ("Task 2: Variance & Standard Deviation", task2_variance_std.analyze_dispersion),
        ("Task 3: Correlation & Probability Basics", task3_correlation_probability.analyze_correlation_and_probability),
        ("Task 4: Outlier Detection (IQR & Z-Score)", task4_outlier_detection.detect_outliers),
        ("Task 5: Matplotlib Visualizations", task5_matplotlib_visualizations.generate_visualizations),
        ("Task 6: Seaborn Visualizations", task6_seaborn_visualizations.generate_seaborn_visualizations),
        ("Task 7: EDA - Inspection & Data Cleaning", task7_eda_inspection_cleaning.run_eda_cleaning),
        ("Task 8: EDA - Correlation & Strategic Insights", task8_eda_correlation_insights.run_correlation_and_insights),
        ("Task 9: Actionable Business Recommendations", task9_business_recommendations.display_business_recommendations),
    ]

    for name, func in tasks:
        print_banner(f"EXECUTING: {name.upper()}")
        func()
        time.sleep(0.5)

    elapsed = time.time() - start_time
    print_banner(f"ALL WEEK 4 TASKS COMPLETED SUCCESSFULLY IN {elapsed:.2f} SECONDS!")

if __name__ == '__main__':
    main()
