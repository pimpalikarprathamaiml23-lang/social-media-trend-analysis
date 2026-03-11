import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# -------------------------------
# Title
# -------------------------------
st.title("📊 Social Media Trend Analysis")
st.write("Topic Modeling Demo for PBL")

# -------------------------------
# User Input
# -------------------------------
st.subheader("Enter Social Media Posts (one per line)")

text = st.text_area(
    "Enter Posts:",
    """AI is transforming technology
Machine learning and AI are trending
Cricket match today was exciting
Football fans celebrate victory
Technology companies release AI tools"""
)

# Convert text to list
posts = text.split("\n")

# -------------------------------
# Display Posts
# -------------------------------
st.subheader("Collected Social Media Posts")

for p in posts:
    st.write(p)

# -------------------------------
# Text Processing
# -------------------------------
words = []

for post in posts:
    tokens = post.lower().split()
    words.extend(tokens)

# Word Frequency
freq = Counter(words)

# -------------------------------
# Frequency Table
# -------------------------------
st.subheader("Trending Words Table")

df = pd.DataFrame(freq.items(), columns=["Word","Frequency"])

st.dataframe(df)

# -------------------------------
# Bar Graph
# -------------------------------
st.subheader("Trending Words Bar Graph")

top = freq.most_common(10)

labels = [i[0] for i in top]
values = [i[1] for i in top]

fig, ax = plt.subplots()

ax.bar(labels, values)

ax.set_xlabel("Words")
ax.set_ylabel("Frequency")
ax.set_title("Top Trending Words")

plt.xticks(rotation=45)

st.pyplot(fig)

# -------------------------------
# Pie Chart
# -------------------------------
st.subheader("Topic Distribution Pie Chart")

fig2, ax2 = plt.subplots()

ax2.pie(values, labels=labels, autopct='%1.1f%%')

ax2.set_title("Topic Share")

st.pyplot(fig2)

# -------------------------------
# Trend Line Graph
# -------------------------------
st.subheader("Trend Comparison Graph")

topics = ["ai","technology","cricket"]

trend = []

for t in topics:
    trend.append(freq[t])

fig3, ax3 = plt.subplots()

ax3.plot(topics, trend, marker="o")

ax3.set_xlabel("Topic")
ax3.set_ylabel("Frequency")
ax3.set_title("Trend Comparison")

st.pyplot(fig3)

st.success("Trend Analysis Completed!")