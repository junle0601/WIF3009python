import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 IShowSpeed: Rise of a Digital Phenomenon")

# === Load Data ===
try:
    yt_views = pd.read_csv("youtube_view_forecast.csv")
    sub_forecast = pd.read_csv("subscriber_forecast.csv")
    country_mentions = pd.read_csv("top_countries.csv")
    collab_mentions = pd.read_csv("collab_counts.csv")
    sentiment_over_time = pd.read_csv("sentiment_over_time.csv")
    content_trend = pd.read_csv("content_type_trend.csv")
    creator_comparison = pd.read_csv("creator_comparison.csv")
except Exception as e:
    st.error(f"❌ Data load failed: {e}")
    st.stop()

# === Tabs ===
tabs = st.tabs([
    "📌 Overview", "📊 Sentiment Trends", "📺 Content Types",  "📈 YouTube Forecast", "🌍 Country Mentions", "🤝 Collaborations", "🤖 Comparisons", "🔮 Conclusions"
])

# === Tab 1: Overview ===
with tabs[0]:
    st.header("🔍 Introduction to IShowSpeed")
    col1, col2 = st.columns([1, 3])  # adjust width ratio as you like

    with col1:
        st.image("ishowspeed_picture.jpg", caption="IShowSpeed", use_column_width=True)

    with col2:
        st.markdown("""
        **IShowSpeed** (real name: Darren Watkins Jr.) is a high-energy digital entertainer who rose to global fame through his unpredictable livestreams and viral moments. Known for his explosive reactions, chaotic humor, and intense audience interaction, he quickly became one of the most recognizable figures in the online entertainment space.

        His journey began on YouTube, where his gaming videos and live chats began attracting a steady stream of viewers. Over time, his reach expanded significantly to platforms like Twitter (X), Instagram, and Reddit — where fan discussions, memes, and clips of his antics further amplified his popularity. Unlike traditional creators, IShowSpeed thrives on spontaneity, often blurring the line between content and performance.

        What sets him apart is not just the content he produces, but how he engages with his audience in real-time. His streams often feature dramatic, meme-worthy moments that get instantly circulated, helping him sustain viral traction. Combined with his youthful energy and unpredictable antics, IShowSpeed has built a dedicated community that spans across multiple platforms and demographics.

        This dashboard offers an analytical deep-dive into his digital footprint — exploring his growth trajectory, public perception, content patterns, and what the future might hold for one of the most talked-about internet personalities today.
        """)
    st.markdown("""
    ### 🚀 Dashboard Key Features
    - **Sentiment Analysis:** Gauge and compare public sentiments over time using comments and discussions gathered from various social media platforms.
    - **Content Analysis:** Explore what types of content generate the most interaction and engagement across different platforms.
    - **Predictive Analytics:** Forecast potential future growth, platform expansion, creation of new video formats, possible collaborations, and future country visits.
    - **Comparative Insights:** See how IShowSpeed’s growth compares to creators like MrBeast and Doja Cat, and what sets him apart from them.
    """)

    st.markdown("""
    ### 📥 Data Sources Overview
                
    - **YouTube**: Titles, view counts, publish dates, and top user comments for all videos, along with growth metrics like subscriber and view trends over time.  
    - **Twitter (X)**: Full tweet history from IShowSpeed’s account, including engagement metrics (**likes**, **retweets**, **views**), and public tweets mentioning him to support sentiment analysis. 
    - **Instagram**: Titles, likes and comments from posts on IShowSpeed’s official account, enabling content performance and audience interaction studies.  
    - **Reddit**: Discussions mentioning IShowSpeed to understand how he's talked about in online communities and forums.  
    - **Audience Demographics**: Geographical distribution of IShowSpeed’s **Twitter** followers to map out his global reach.
    """)

# === Tab 2: Sentiment Trends ===
with tabs[1]:
    st.title("📊 Sentiment Analysis from Instagram, Twitter, Reddit & YouTube")
    st.subheader("📶Sentiment Distribution by Platform")

    # Sentiment data
    data = {
        'Platform': ['Instagram', 'Twitter', 'Reddit', 'YouTube'],
        'Positive': [429, 396, 68, 3274],
        'Neutral': [446, 375, 244, 3495],
        'Negative': [49, 235, 63, 1342]
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Calculate total and percentage
    df['Total'] = df[['Positive', 'Neutral', 'Negative']].sum(axis=1)
    df['% Positive'] = df['Positive'] / df['Total'] * 100
    df['% Neutral'] = df['Neutral'] / df['Total'] * 100
    df['% Negative'] = df['Negative'] / df['Total'] * 100

    # Create percentage-based bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df['Platform'],
        y=df['% Positive'],
        name='Positive',
        marker_color='green'
    ))
    fig.add_trace(go.Bar(
        x=df['Platform'],
        y=df['% Neutral'],
        name='Neutral',
        marker_color='gray'
    ))
    fig.add_trace(go.Bar(
        x=df['Platform'],
        y=df['% Negative'],
        name='Negative',
        marker_color='red'
    ))

    # Layout
    fig.update_layout(
        barmode='group',
        title='Percentage of Sentiment Mentions Across Platforms',
        xaxis_title='Platform',
        yaxis_title='Percentage (%)',
        yaxis=dict(range=[0, 100]),
        legend_title='Sentiment',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    emoji_data = {
    '🔥Instagram': [('🔥', 305), ('😂', 266), ('❤', 196), ('😍', 64), ('👏', 61)],
    '😭Twitter': [('😭', 185), ('😂', 83), ('📰', 82), ('🔥', 76), ('🔴', 70)],
    '😭Reddit': [('😭', 19), ('💀', 8), ('💪', 3), ('🔥', 3), ('🙏', 3)],
    '😂YouTube': [('😂', 991), ('🔥', 624), ('❤', 369), ('😭', 353), ('🤣', 307)]
    }

    st.header("Top Emojis per Platform")

    for platform, emoji_list in emoji_data.items():
        st.subheader(f"{platform}")
        df_emoji = pd.DataFrame(emoji_list, columns=["Emoji", "Count"])
        fig = px.bar(df_emoji, x="Emoji", y="Count", title=f"Emoji Usage", color="Count",
                    color_continuous_scale="Bluered")
        st.plotly_chart(fig, use_container_width=True)

    st.header("Top Sentiment Dates")

    # Summary table

    # Load each CSV
    df_insta = pd.read_csv('instagram_sentiment_over_time.csv')
    df_twitter = pd.read_csv('twitter_sentiment_over_time.csv')
    df_reddit = pd.read_csv('reddit_sentiment_over_time.csv')
    df_youtube = pd.read_csv('youtube_sentiment_over_time.csv')

    # Combine into one DataFrame
    df_all = pd.concat([df_insta, df_twitter, df_reddit, df_youtube], ignore_index=True)

    # Ensure date is parsed correctly
    df_all['date'] = pd.to_datetime(df_all['date'])

    # Melt the DataFrame to long format
    df_long = df_all.melt(id_vars=['date', 'platform'],
                        value_vars=['positive', 'negative'],
                        var_name='sentiment_type',
                        value_name='count')

    # Plot
    st.header("📊 Sentiment Trends Across Platforms")

    fig = px.line(df_long, x='date', y='count', color='platform', line_dash='sentiment_type',
                title='Positive & Negative Sentiment Over Time',
                labels={'count': 'Mentions', 'sentiment_type': 'Sentiment'})
    st.plotly_chart(fig, use_container_width=True)

    st.header("Cross-Platform Sentiment Comparison")

    comparison_data = {
        'Platform': ['Instagram', 'Twitter', 'Reddit', 'YouTube'],
        '% Positive': [46.4, 39.4, 18.1, 40.4],
        '% Neutral': [48.3, 37.3, 65.1, 43.1],
        '% Negative': [5.3, 23.4, 16.8, 16.5],
        'Total Comments': [924, 1006, 375, 8111]
    }

    df_compare = pd.DataFrame(comparison_data)
    st.dataframe(df_compare.style.background_gradient(cmap='RdYlGn_r', subset=['% Positive', '% Neutral', '% Negative']))

    st.header("Interpretive Insight")

    st.markdown("""
    - 🔥 **Instagram & YouTube** show consistently positive sentiment and are emoji-rich.
    - 💬 **Twitter** shows the highest emotional reactivity — both positive and negative — likely due to real-time events.
    - 💭 **Reddit** has a high neutral percentage, suggesting deeper or more analytical discussions.
    - 📅 **May 30–31** marks a major sentiment spike across platforms — aligned with the UCL trophy moment.
    """)

    st.header("Summary & Implications")

    st.markdown("""
    ### Key Takeaways:
    - **Instagram and YouTube** audiences are most supportive of IShowSpeed.
    - **Twitter**'s spikes reveal its strength as a reaction platform for live content.
    - **Reddit** offers a more analytical, discussion-based sentiment environment.
    - **Major spikes** in late May are tied to IShowSpeed's **Champions League moment**.

    ### Implications:
    - Brands or collaborators should focus campaigns on Instagram/YouTube for high sentiment.
    - Twitter is ideal for viral reactions and controversy monitoring.
    - Reddit can be used to test long-form engagement and deep feedback.
    """)



# === Tab 3: Content Types ===
with tabs[2]:
    st.subheader("🧩 Content Format Trends (Instagram + Twitter)")
    content_trend['month'] = content_trend['month'].astype(str)
    pivot = content_trend.pivot_table(index="month", columns="content_type", values="count", aggfunc="sum").fillna(0)
    st.area_chart(pivot) 

# === Tab 4: Youtube Forecast ===
with tabs[3]:
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

# === Tab 4: Content Types ===
with tabs[3]:
    st.subheader("🧩 Content Format Trends (Instagram + Twitter)")
    content_trend['month'] = content_trend['month'].astype(str)
    pivot = content_trend.pivot_table(index="month", columns="content_type", values="count", aggfunc="sum").fillna(0)
    st.area_chart(pivot)

# === Tab 5: Country Mentions ===
with tabs[4]:
    st.subheader("🌍 Country Interest")
    st.bar_chart(country_mentions.set_index("Label")["Mentions"])
    st.markdown("Frequent mentions and flags indicate high interest from Brazil, Portugal, Philippines, etc.")

# === Tab 6: Collaborations ===
with tabs[5]:
    st.subheader("🤝 Collaboration Themes")
    st.bar_chart(collab_mentions.set_index("Collaborator")["Mentions"])
    st.markdown("Recurring mentions of Ronaldo, Messi, Kai Cenat, and Twitch streamers suggest popular crossover appeal.")

# === Tab 7: Comparisons ===
with tabs[6]:
    st.subheader("📌 Comparison with Other Creators")

    # Show the raw table (optional)
    st.dataframe(creator_comparison)

    # Bar Chart: Subscriber Growth
    st.subheader("📈 Subscriber Growth (%)")
    st.bar_chart(creator_comparison.set_index("Creator")["Subscriber Growth (%)"])

    # Bar Chart: Total Twitter Engagement
    st.subheader("🐦 Total Twitter Engagement")
    st.bar_chart(creator_comparison.set_index("Creator")["Total Twitter Engagement"])

    # Bar Chart: Normalized Views Growth
    st.subheader("📺 Normalized Views Growth")
    st.bar_chart(creator_comparison.set_index("Creator")["Latest Normalized Views Growth"])

    # Grouped Bar Chart: Engagement Ratios
    st.subheader("💬 Engagement Ratios (Twitter)")

    import numpy as np
    fig, ax = plt.subplots()
    index = np.arange(len(creator_comparison))
    bar_width = 0.35

    r1 = creator_comparison["Avg Replies-to-Likes Ratio"]
    r2 = creator_comparison["Avg Retweets-to-Likes Ratio"]

    ax.bar(index, r1, bar_width, label='Replies-to-Likes', color='skyblue')
    ax.bar(index + bar_width, r2, bar_width, label='Retweets-to-Likes', color='orange')

    ax.set_xlabel('Creator')
    ax.set_ylabel('Ratio')
    ax.set_title('Twitter Engagement Ratios')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(creator_comparison["Creator"])
    ax.legend()
    st.pyplot(fig)

    # Commentary
    st.markdown("""
    - IShowSpeed leads in relative view growth and raw engagement.
    - MrBeast dominates in total reach and consistency.
    - Doja Cat shows strength in engagement ratios, suggesting strong fan interaction.
    """)


# === Tab 8: Conclusions ===
with tabs[7]:
    st.header("🔮 Final Thoughts & Future")
    st.markdown("""
    - **Future Growth**: Forecast indicates steady viewership and subscriber growth.
    - **Next Country?** Brazil and Portugal show strong signals from audience mentions.
    - **New Formats**: Strong rise in skits, music-related content, and meme formats.
    - **Opportunities**: Potential to expand into music collabs, brand deals, or live event streams.
    """)
