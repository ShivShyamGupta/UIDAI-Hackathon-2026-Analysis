import pandas as pd
import matplotlib.pyplot as plt
import glob

# 1. Load the Data
print("Loading data...")
try:
    df_enrolment = pd.concat([pd.read_csv(f) for f in glob.glob("*enrolment*.csv")])
    df_biometric = pd.concat([pd.read_csv(f) for f in glob.glob("*biometric*.csv")])
    df_demographic = pd.concat([pd.read_csv(f) for f in glob.glob("*demographic*.csv")])
except ValueError:
    print("Error: CSV files not found. Please upload the data files.")
    exit()

# 2. Analyze Enrolment Trends
print("Generating Enrolment Graph...")
state_enrolment = df_enrolment.groupby('state')[['age_0_5', 'age_5_17', 'age_18_greater']].sum()
state_enrolment['Total'] = state_enrolment.sum(axis=1)
top_states = state_enrolment.sort_values('Total', ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_states[['age_0_5', 'age_5_17', 'age_18_greater']].plot(kind='bar', stacked=True)
plt.title('Aadhaar Enrolment Trends by Age Group')
plt.xlabel('State')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('enrolment_trends.png')

# 3. Analyze Demographic Specific Trends (NEW)
print("Generating Demographic Update Graph...")
demo_state = df_demographic.groupby('state')[['demo_age_5_17', 'demo_age_17_']].sum()
demo_state['Total'] = demo_state.sum(axis=1)
top_demo = demo_state.sort_values('Total', ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_demo[['demo_age_5_17', 'demo_age_17_']].plot(kind='bar', stacked=True, color=['skyblue', 'salmon'])
plt.title('Demographic Update Volume by State')
plt.xlabel('State')
plt.ylabel('Update Requests')
plt.tight_layout()
plt.savefig('demographic_trends.png')

# 4. Analyze Update Comparison
print("Generating Comparison Graph...")
bio_counts = df_biometric.groupby('state')[['bio_age_5_17', 'bio_age_17_']].sum().sum(axis=1)
demo_counts = df_demographic.groupby('state')[['demo_age_5_17', 'demo_age_17_']].sum().sum(axis=1)

comparison = pd.DataFrame({'Biometric': bio_counts, 'Demographic': demo_counts})
comparison['Total'] = comparison.sum(axis=1)
comparison.sort_values('Total', ascending=False).head(10)[['Biometric', 'Demographic']].plot(kind='bar')

plt.title('Biometric vs Demographic Updates')
plt.xlabel('State')
plt.ylabel('Volume')
plt.tight_layout()
plt.savefig('update_comparison.png')

print("Analysis Complete. All 3 graphs saved.")
