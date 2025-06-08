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
    content_type_trend = pd.read_csv("content_type_trend.csv")
    creator_comparison = pd.read_csv("creator_comparison.csv")
    platform_freq = pd.read_csv("platform_freq.csv")

    content_trend = pd.read_csv("content_trend.csv")



except Exception as e:
    st.error(f"❌ Data load failed: {e}")
    st.stop()

# === Tabs ===
tabs = st.tabs([
    "📌 Overview", "📊 Sentiment Analysis", "📺 Content Analysis","📈 Future Predictions", "🤖 Comparisons With Others", "🔮 Conclusions"
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
# === Tab 2: Sentiment Analysis ===
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
    content_type_trend['month'] = content_type_trend['month'].astype(str)
    pivot = content_type_trend.pivot_table(index="month", columns="content_type", values="count", aggfunc="sum").fillna(0)
    st.area_chart(pivot)

# === Tab 3: Future Predictions ===
with tabs[3]:
    st.subheader("📈 YouTube Views and Subscriber Forecast")

    yt_views['Month'] = pd.to_datetime(yt_views['Month'], errors='coerce')
    sub_forecast['Date'] = pd.to_datetime(sub_forecast['Date'])

    forecast_start_date_view = pd.to_datetime("2024-06-01")
    forecast_start_date_sub = pd.to_datetime("2025-07-01")


    import altair as alt

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("**Forecasted Monthly Views**")
        base_views = alt.Chart(yt_views).encode(x='Month:T')

        line_views = base_views.mark_line(point=True, color="steelblue").encode(
            y=alt.Y('Predicted Views:Q', title='Views'),
            tooltip=['Month:T', 'Predicted Views']
        )

        rule = alt.Chart(pd.DataFrame({'x': [forecast_start_date_view]})).mark_rule(
            color='red', strokeDash=[5, 5]
        ).encode(x='x:T')

        st.altair_chart((line_views + rule).properties(height=400), use_container_width=True)

    with col2:
        st.markdown("**Subscriber Forecast**")
        base_subs = alt.Chart(sub_forecast).encode(x='Date:T')

        line_subs = base_subs.mark_line(point=True, color="deepskyblue").encode(
            y=alt.Y('Predicted Subscribers:Q', title='Subscribers'),
            tooltip=['Date:T', 'Predicted Subscribers']
        )

        rule2 = alt.Chart(pd.DataFrame({'x': [forecast_start_date_sub]})).mark_rule(
            color='red', strokeDash=[5, 5]
        ).encode(x='x:T')

        st.altair_chart((line_subs + rule2).properties(height=400), use_container_width=True)

    with st.expander("🔍 What Does the Forecast Tell Us?", expanded=False):
        st.markdown("""
        **Future Trajectory of IShowSpeed**

        Based on predictive analytics using linear regression models on historical YouTube data:

        - 📈 **Views**: Forecasted to increase steadily through mid-2026.
        - 👥 **Subscribers**: Projected to surpass current milestones and grow continuously.
        - 🧠 **Implications**:
            - His content strategy is effective — consistently high retention and reach.
            - He remains relevant and influential in the creator ecosystem.
            - His growth opens up more monetization, sponsorship, and brand collaboration opportunities.

        🔮 **Conclusion**: Strong growth trend with no signs of plateauing over the next 12–18 months.
        """)


    st.subheader("📲 Fan-Mentioned Platforms")
    # Create Altair bar chart
    bar_chart = alt.Chart(platform_freq).mark_bar().encode(
        x=alt.X('Platform:N', title='Platform'),
        y=alt.Y('Mentions:Q', title='Number of Mentions'),
        color=alt.Color('Platform:N', legend=None),
        tooltip=['Platform', 'Mentions']
    ).properties(
        title='Mentions of Streaming Platforms by Fans',
        width=500,
        height=300
    ).configure_axisX(
        labelAngle=0
    )

    st.altair_chart(bar_chart, use_container_width=True)

    with st.expander("🔍 Interpretation: Potential Platforms for Future Growth"):
        st.markdown("""
        Based on fan discussions extracted from IShowSpeed's Instagram and Twitter content, **YouTube** remains the dominant platform with the highest number of direct mentions, indicating a strong, loyal base.

        However, there is noticeable fan interest in emerging platforms such as:

        - **Twitch** — still garners support despite past bans  
        - **TikTok** — short-form and live content potential aligns well with Speed's energetic style  
        - **Kick** — gaining traction among streamers and mentioned by fans as a possible alternative

        These insights suggest that while **YouTube** will likely remain his primary platform, **expansion into TikTok LIVE or Kick** could open new audience segments, particularly among younger or international viewers. These platforms also offer more **live engagement, viral reach**, and **monetization opportunities**.
        """)

    st.markdown("### 🔄 Content Format Trends (Recent 6 Months)")


    # Sum total for selected categories
    categories_to_show = ['country', 'gaming', 'other']
    available_categories = [col for col in categories_to_show if col in content_trend.columns]
    category_totals = content_trend[available_categories].sum().reset_index()
    category_totals.columns = ['Content Type', 'Total Posts']

    # Create bar chart
    chart = alt.Chart(category_totals).mark_bar().encode(
        x=alt.X('Content Type:N', title='Content Type'),
        y=alt.Y('Total Posts:Q', title='Total Post Count'),
        color=alt.Color('Content Type:N', legend=None),
        tooltip=['Content Type', 'Total Posts']
    ).properties(
        title='Total Mentions by Content Type (All Months)',
        width=500,
        height=350
    ).configure_axisX(
        labelAngle=0
    )

    st.altair_chart(chart, use_container_width=True)


    with st.expander("📌 New Video Formats (Content Type Trends)", expanded=False):
        st.markdown("""
        An analysis of IShowSpeed's recent Instagram and Twitter posts over the past 6 months reveals that the majority of content falls under the **"other"** category, indicating diverse or less classifiable formats.  
        Among recognizable categories, **"gaming"** content maintains a consistent presence, underscoring its role as a core part of his content strategy.  
        Mentions of **"country"**-themed posts — often tied to travel or international collaborations — appear in smaller volume but suggest continued audience interest in his global reach and travel-related content.

        This trend suggests that while Speed remains experimental in his formats:
        - 🎮 **Gaming** remains a foundational content pillar  
        - 🌍 There’s potential to scale up travel, culture, or globally themed content, especially around international events or tours  
        - 📺 Future content strategies could benefit from exploring more defined or recurring series formats to strengthen audience recall
        """)
    
    st.subheader("🌍 Which Country will he go next?")
    # Custom color mapping for countries
    country_colors = {
        "Portugal": "#006600",   # green
        "Brazil": "#009C3B",     # green
        "Philippines": "#0038A8",  # blue
        "USA": "#B22234",
        "UK": "#00247D",
        "Argentina": "#FF9933",
        "Hong Kong": "#BC002D",
        "China": "#DE2910",
        "Mongolia": "#0055A4",
        "Netherlands": "#AA151B"
    }

    # Create color scale
    color_scale = alt.Scale(
        domain=list(country_colors.keys()),
        range=list(country_colors.values())
    )

    # Chart
    chart = alt.Chart(country_mentions).mark_bar().encode(
        x=alt.X('Label:N', title='Country', sort='-y', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Mentions:Q', title='Mentions'),
        color=alt.Color('Label:N', scale=color_scale, legend=None),
        tooltip=['Label', 'Mentions']
    ).properties(
        title="Top Countries Mentioned by Fans",
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    with st.expander("📌 Which Country Will He Go Next?", expanded=False):
        st.markdown("""
        Based on fan interactions and post content, the top mentioned countries include **Portugal**, **Brazil**, and **China**.  
        These mentions suggest high relevance in IShowSpeed’s recent content, likely tied to **football culture** and **global engagement** — for example, **Portugal is the home of Cristiano Ronaldo**.

        Given this trend, it is plausible that his next international appearance or content focus could involve a **collaboration**, **travel vlog**, or **live event** in one of these regions:
        - 🇵🇹 **Portugal** – strongest signal, high emotional and cultural value  
        - 🇧🇷 **Brazil** – passionate fanbase and sports synergy  
        - 🇨🇳 **China** – strong social platform activity and global expansion potential
        """)

    st.subheader("🤝 Potential Collaboration")
        # Custom color palette (can be extended)
    collab_colors = {
        "Ronaldo": "#FFCC00",
        "Messi": "#66CCFF",
        "Kai Cenat": "#FF6699",
        "Ava": "#CC99FF",
        "Speed with": "#00CCCC",
        "Twitch": "#9966FF",
        "MrBeast": "#FF9966",
        "Other": "#CCCCCC"
    }

    color_scale = alt.Scale(
        domain=list(collab_colors.keys()),
        range=list(collab_colors.values())
    )

    # Altair Chart
    # Sort data manually by Mentions (descending)
    collab_mentions_sorted = collab_mentions.sort_values(by="Mentions", ascending=False)

    # Altair Chart
    chart = alt.Chart(collab_mentions_sorted).mark_bar().encode(
        x=alt.X('Collaborator:N', title='Collaborator', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Mentions:Q', title='Mentions'),
        color=alt.Color('Collaborator:N', scale=color_scale, legend=None),
        tooltip=['Collaborator', 'Mentions']
    ).properties(
        title="Top Collaboration Mentions by Fans",
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    with st.expander("📌 Collaboration Indicators", expanded=False):
        st.markdown("""
        Analysis of IShowSpeed's recent Instagram and Twitter posts reveals a **strong fan-driven interest in collaborations** — particularly with **Cristiano Ronaldo**, who dominates mentions by a significant margin.  
        **Lionel Messi** also features notably, indicating **sustained engagement with football-related content**.  
        The use of the word **"with"** in many posts reinforces the collaborative nature of these mentions.

        This suggests that:
        - 🏆 **Fans are highly engaged** with content involving global sports icons  
        - 🤝 **Collaborations**, especially **in-person** or themed around **football**, are likely to generate viral traction  
        - 📸 There’s clear potential for **strategic content** involving athlete interactions, sports-themed challenges, or co-streamed events
        """)

# === Tab 4: Comparisons ===
with tabs[4]:
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


# === Tab 5: Conclusions ===
with tabs[5]:
    st.header("🔮 Final Thoughts & Future")
    st.markdown("""
    - **Future Growth**: Forecast indicates steady viewership and subscriber growth.
    - **Next Country?** Brazil and Portugal show strong signals from audience mentions.
    - **New Formats**: Strong rise in skits, music-related content, and meme formats.
    - **Opportunities**: Potential to expand into music collabs, brand deals, or live event streams.
    """)
