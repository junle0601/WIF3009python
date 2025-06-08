import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 IShowSpeed: Rise of a Digital Phenomenon")

# === Load Data ===
try:
    yt_views = pd.read_csv("youtube_view_forecast.csv")
    sub_forecast = pd.read_csv("subscriber_forecast.csv")
    country_mentions = pd.read_csv("top_countries.csv")
    #collab_mentions = pd.read_csv("collab_mentions.csv")
    sentiment_over_time = pd.read_csv("sentiment_over_time.csv")
    #content_trend = pd.read_csv("content_type_trend.csv")
    #creator_comparison = pd.read_csv("creator_comparison.csv")
except Exception as e:
    st.error(f"❌ Data load failed: {e}")
    st.stop()

# === Tabs ===
tabs = st.tabs([
    "📌 Overview", "📈 YouTube Forecast", "📊 Sentiment Trends", "📺 Content Types",
    "🌍 Country Mentions", "🤝 Collaborations", "🤖 Comparisons", "🔮 Conclusions"
])

# === Tab 1: Overview ===
with tabs[0]:
    st.header("Project Summary & Introduction")
    st.markdown("""
    **IShowSpeed** is a viral digital entertainer known for his chaotic humor and explosive reactions.  
    This dashboard analyzes his rise through data and forecasts what's next.
    """)
    st.markdown("""
    **Key Features**:
    - Social media growth analysis (YouTube, Twitter, IG)
    - Audience sentiment breakdown
    - Top countries and collaborators
    - Predictive analytics for views, subscribers, and global expansion
    """)

# === Tab 2: Forecast ===
with tabs[1]:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Monthly Views Forecast")
        yt_views['Month'] = pd.to_datetime(yt_views['Month'], errors='coerce', format='mixed')
        fig, ax = plt.subplots()
        ax.plot(yt_views['Month'], yt_views['Predicted Views'], marker='o')
        ax.set_title("Monthly Views Forecast")
        ax.grid()
        st.pyplot(fig)
    with col2:
        st.subheader("👥 Subscriber Forecast")
        sub_forecast['Date'] = pd.to_datetime(sub_forecast['Date'])
        st.line_chart(sub_forecast.set_index("Date")["Predicted Subscribers"])

# === Tab 3: Sentiment ===
with tabs[2]:
    st.subheader("📊 Sentiment Over Time")
    st.line_chart(sentiment_over_time.set_index("Date")[["positive", "negative"]])
    st.markdown("Majority of audience sentiment remains positive, especially after viral streams or collaborations.")

# # === Tab 4: Content Types ===
# with tabs[3]:
#     st.subheader("🧩 Content Format Trends (Instagram + Twitter)")
#     pivot = content_trend.pivot(index="Month", columns="content_type", values="count").fillna(0)
#     st.area_chart(pivot)

# === Tab 5: Country Mentions ===
with tabs[4]:
    st.subheader("🌍 Country Interest")
    st.bar_chart(country_mentions.set_index("Label")["Mentions"])
    st.markdown("Frequent mentions and flags indicate high interest from Brazil, Portugal, Philippines, etc.")

# # === Tab 6: Collaborations ===
# with tabs[5]:
#     st.subheader("🤝 Collaboration Themes")
#     st.bar_chart(collab_mentions.set_index("Collaborator")["Mentions"])
#     st.markdown("Recurring mentions of Ronaldo, Messi, Kai Cenat, and Twitch streamers suggest popular crossover appeal.")

# # === Tab 7: Comparisons ===
# with tabs[6]:
#     st.subheader("📌 Comparison with Other Creators")
#     st.dataframe(creator_comparison)
#     st.markdown("""
#     - IShowSpeed's growth outpaces traditional creators in engagement spike.
#     - More meme-viral moments and real-time audience interaction vs polished content from peers like MrBeast.
#     """)

# === Tab 8: Conclusions ===
with tabs[7]:
    st.header("🔮 Final Thoughts & Future")
    st.markdown("""
    - **Future Growth**: Forecast indicates steady viewership and subscriber growth.
    - **Next Country?** Brazil and Portugal show strong signals from audience mentions.
    - **New Formats**: Strong rise in skits, music-related content, and meme formats.
    - **Opportunities**: Potential to expand into music collabs, brand deals, or live event streams.
    """)
