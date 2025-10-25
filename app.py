import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
df = pd.DataFrame({
    'population': ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte'],
    'percentage': [20, 50, 30, 40, 60]
})

st.title("Interactive Streamlit Dashboard")
st.write("This dashboard allows you to explore immune cell populations.")

# --- Interactive widget: select populations to display ---
pop_options = st.multiselect(
    "Select populations to display:",
    options=df['population'].unique(),
    default=df['population'].unique()
)

# Filter the DataFrame based on selection
filtered_df = df[df['population'].isin(pop_options)]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# --- Interactive bar chart ---
st.subheader("Bar Chart of Selected Populations")
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x='population', y='percentage', data=filtered_df, ax=ax)
ax.set_ylabel("Percentage")
ax.set_ylim(0, 100)  # optional: fix y-axis range
st.pyplot(fig)

# --- Optional: display summary statistics ---
st.subheader("Summary Statistics")
st.write(filtered_df.describe())
