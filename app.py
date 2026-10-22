
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Healthcare Analytics",
    page_icon="🏥",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv(
        "1776250375-P2-Healthcare Analytics for Doctor Visits (1).csv"
    )

df = load_data()

st.title("🏥 Healthcare Analytics for Doctor Visits")
st.write(
    "Explore doctor visit patterns by demographics, "
    "health conditions, income, and healthcare support."
)

st.sidebar.header("Dashboard Filters")

filtered = df.copy()

if "gender" in filtered.columns:
    genders = sorted(filtered["gender"].dropna().unique().tolist())
    selected_gender = st.sidebar.multiselect(
        "Gender", genders, default=genders
    )
    filtered = filtered[filtered["gender"].isin(selected_gender)]

if "age" in filtered.columns:
    age_min = float(filtered["age"].min())
    age_max = float(filtered["age"].max())
    age_range = st.sidebar.slider(
        "Age range", age_min, age_max, (age_min, age_max)
    )
    filtered = filtered[
        filtered["age"].between(age_range[0], age_range[1])
    ]

if "visits" in filtered.columns:
    visits = pd.to_numeric(filtered["visits"], errors="coerce")
    filtered = filtered[visits.notna()].copy()
    filtered["visits"] = visits[visits.notna()]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("Patient records", f"{len(filtered):,}")
c2.metric("Average doctor visits", f"{filtered['visits'].mean():.2f}")
c3.metric("Records with zero visits",
          f"{(filtered['visits'] == 0).sum():,}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Doctor Visit Distribution")
    counts = filtered["visits"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x=counts.index, y=counts.values, color="steelblue", ax=ax)
    ax.set_xlabel("Number of doctor visits")
    ax.set_ylabel("Number of records")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("Doctor Visits by Gender")
    gender_data = filtered.groupby("gender")["visits"].mean().sort_values()
    st.bar_chart(gender_data)

st.subheader("Doctor Visits by Age")
age_data = filtered.copy()
age_data["Age Group"] = pd.cut(
    age_data["age"],
    bins=[-float("inf"), 29, 44, 59, float("inf")],
    labels=["Under 30", "30–44", "45–59", "60+"]
)
st.bar_chart(age_data.groupby("Age Group", observed=False)["visits"].mean())

st.subheader("Health and Healthcare Support")

options = [
    c for c in [
        "illness", "health", "income", "reduced",
        "nchronic", "lchronic", "private", "freepoor", "freerepat"
    ]
    if c in filtered.columns
]

if options:
    selected = st.selectbox("Compare doctor visits with", options)
    if pd.api.types.is_numeric_dtype(filtered[selected]):
        summary = filtered.groupby(selected, dropna=False)["visits"].mean()
        st.bar_chart(summary)
    else:
        summary = filtered.groupby(selected, dropna=False)["visits"].mean()
        st.bar_chart(summary)

st.subheader("Dataset Preview")
st.dataframe(filtered.head(100), use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download filtered data (CSV)",
    data=csv,
    file_name="healthcare_analysis_results.csv",
    mime="text/csv"
)

st.caption(
    "This dashboard explores associations in the supplied dataset. "
    "It does not provide medical diagnoses or prove causation."
)
