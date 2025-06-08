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
    index_comparison = pd.read_csv("normalized_index.csv")


except Exception as e:
    st.error(f"❌ Data load failed: {e}")
    st.stop()

# === Tabs ===
tabs = st.tabs(
    [
        "📌 Overview",
        "📊 Sentiment Analysis",
        "📺 Content Analysis",
        "📈 Future Predictions",
        "🤖 Comparisons With Others",
        "📈 Growth & Demographics",
        "🔮 Conclusions",
    ]
)

# === Tab 1: Overview ===
with tabs[0]:
    st.header("🔍 Introduction to IShowSpeed")
    col1, col2 = st.columns([1, 3])  # adjust width ratio as you like

    with col1:
        st.image(
            "ishowspeed_picture.jpg", caption="IShowSpeed", use_container_width=True
        )

    with col2:
        st.markdown(
            """
        **IShowSpeed** (real name: Darren Watkins Jr.) is a high-energy digital entertainer who rose to global fame through his unpredictable livestreams and viral moments. Known for his explosive reactions, chaotic humor, and intense audience interaction, he quickly became one of the most recognizable figures in the online entertainment space.

        His journey began on YouTube, where his gaming videos and live chats began attracting a steady stream of viewers. Over time, his reach expanded significantly to platforms like Twitter (X), Instagram, and Reddit — where fan discussions, memes, and clips of his antics further amplified his popularity. Unlike traditional creators, IShowSpeed thrives on spontaneity, often blurring the line between content and performance.

        What sets him apart is not just the content he produces, but how he engages with his audience in real-time. His streams often feature dramatic, meme-worthy moments that get instantly circulated, helping him sustain viral traction. Combined with his youthful energy and unpredictable antics, IShowSpeed has built a dedicated community that spans across multiple platforms and demographics.

        This dashboard offers an analytical deep-dive into his digital footprint — exploring his growth trajectory, public perception, content patterns, and what the future might hold for one of the most talked-about internet personalities today.
        """
        )
    st.markdown(
        """
    ### 🚀 Dashboard Key Features
    - **Sentiment Analysis:** Gauge and compare public sentiments over time using comments and discussions gathered from various social media platforms.
    - **Content Analysis:** Explore what types of content generate the most interaction and engagement across different platforms.
    - **Predictive Analytics:** Forecast potential future growth, platform expansion, creation of new video formats, possible collaborations, and future country visits.
    - **Comparative Insights:** See how IShowSpeed’s growth compares to creators like MrBeast and Doja Cat, and what sets him apart from them.
    """
    )

    st.markdown(
        """
    ### 📥 Data Sources Overview
                
    - **YouTube**: Titles, view counts, publish dates, and top user comments for all videos, along with growth metrics like subscriber and view trends over time.  
    - **Twitter (X)**: Full tweet history from IShowSpeed’s account, including engagement metrics (**likes**, **retweets**, **views**), and public tweets mentioning him to support sentiment analysis. 
    - **Instagram**: Titles, likes and comments from posts on IShowSpeed’s official account, enabling content performance and audience interaction studies.  
    - **Reddit**: Discussions mentioning IShowSpeed to understand how he's talked about in online communities and forums.  
    - **Audience Demographics**: Geographical distribution of IShowSpeed’s **Twitter** followers to map out his global reach.
    """
    )

# === Tab 1: Sentiment Analysis ===
with tabs[1]:
    st.title("📊 Sentiment Analysis from Instagram, Twitter, Reddit & YouTube")
    st.subheader("📶Sentiment Distribution by Platform")

    # Sentiment data
    data = {
        "Platform": ["Instagram", "Twitter", "Reddit", "YouTube"],
        "Positive": [429, 396, 68, 3274],
        "Neutral": [446, 375, 244, 3495],
        "Negative": [49, 235, 63, 1342],
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Calculate total and percentage
    df["Total"] = df[["Positive", "Neutral", "Negative"]].sum(axis=1)
    df["% Positive"] = df["Positive"] / df["Total"] * 100
    df["% Neutral"] = df["Neutral"] / df["Total"] * 100
    df["% Negative"] = df["Negative"] / df["Total"] * 100

    # Create percentage-based bar chart
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df["Platform"], y=df["% Positive"], name="Positive", marker_color="green"
        )
    )
    fig.add_trace(
        go.Bar(x=df["Platform"], y=df["% Neutral"], name="Neutral", marker_color="gray")
    )
    fig.add_trace(
        go.Bar(
            x=df["Platform"], y=df["% Negative"], name="Negative", marker_color="red"
        )
    )

    # Layout
    fig.update_layout(
        barmode="group",
        title="Percentage of Sentiment Mentions Across Platforms",
        xaxis_title="Platform",
        yaxis_title="Percentage (%)",
        yaxis=dict(range=[0, 100]),
        legend_title="Sentiment",
        height=500,
    )

    st.plotly_chart(fig, use_container_width=True)

    emoji_data = {
        "🔥Instagram": [("🔥", 305), ("😂", 266), ("❤", 196), ("😍", 64), ("👏", 61)],
        "😭Twitter": [("😭", 185), ("😂", 83), ("📰", 82), ("🔥", 76), ("🔴", 70)],
        "😭Reddit": [("😭", 19), ("💀", 8), ("💪", 3), ("🔥", 3), ("🙏", 3)],
        "😂YouTube": [("😂", 991), ("🔥", 624), ("❤", 369), ("😭", 353), ("🤣", 307)],
    }

    st.header("Top Emojis per Platform")

    for platform, emoji_list in emoji_data.items():
        st.subheader(f"{platform}")
        df_emoji = pd.DataFrame(emoji_list, columns=["Emoji", "Count"])
        fig = px.bar(
            df_emoji,
            x="Emoji",
            y="Count",
            title=f"Emoji Usage",
            color="Count",
            color_continuous_scale="Bluered",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.header("Top Sentiment Dates")

    # Summary table

    # Load each CSV
    df_insta = pd.read_csv("instagram_sentiment_over_time.csv")
    df_twitter = pd.read_csv("twitter_sentiment_over_time.csv")
    df_reddit = pd.read_csv("reddit_sentiment_over_time.csv")
    df_youtube = pd.read_csv("youtube_sentiment_over_time.csv")

    # Combine into one DataFrame
    df_all = pd.concat([df_insta, df_twitter, df_reddit, df_youtube], ignore_index=True)

    # Ensure date is parsed correctly
    df_all["date"] = pd.to_datetime(df_all["date"])

    # Melt the DataFrame to long format
    df_long = df_all.melt(
        id_vars=["date", "platform"],
        value_vars=["positive", "negative"],
        var_name="sentiment_type",
        value_name="count",
    )

    # Plot
    st.header("📊 Sentiment Trends Across Platforms")

    fig = px.line(
        df_long,
        x="date",
        y="count",
        color="platform",
        line_dash="sentiment_type",
        title="Positive & Negative Sentiment Over Time",
        labels={"count": "Mentions", "sentiment_type": "Sentiment"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.header("Cross-Platform Sentiment Comparison")

    comparison_data = {
        "Platform": ["Instagram", "Twitter", "Reddit", "YouTube"],
        "% Positive": [46.4, 39.4, 18.1, 40.4],
        "% Neutral": [48.3, 37.3, 65.1, 43.1],
        "% Negative": [5.3, 23.4, 16.8, 16.5],
        "Total Comments": [924, 1006, 375, 8111],
    }

    df_compare = pd.DataFrame(comparison_data)
    st.dataframe(
        df_compare.style.background_gradient(
            cmap="RdYlGn_r", subset=["% Positive", "% Neutral", "% Negative"]
        )
    )

    st.header("Interpretive Insight")

    st.markdown(
        """
    - 🔥 **Instagram & YouTube** show consistently positive sentiment and are emoji-rich.
    - 💬 **Twitter** shows the highest emotional reactivity — both positive and negative — likely due to real-time events.
    - 💭 **Reddit** has a high neutral percentage, suggesting deeper or more analytical discussions.
    - 📅 **May 30–31** marks a major sentiment spike across platforms — aligned with the UCL trophy moment.
    """
    )

    st.header("Summary & Implications")

    st.markdown(
        """
    ### Key Takeaways:
    - **Instagram and YouTube** audiences are most supportive of IShowSpeed.
    - **Twitter**'s spikes reveal its strength as a reaction platform for live content.
    - **Reddit** offers a more analytical, discussion-based sentiment environment.
    - **Major spikes** in late May are tied to IShowSpeed's **Champions League moment**.

    ### Implications:
    - Brands or collaborators should focus campaigns on Instagram/YouTube for high sentiment.
    - Twitter is ideal for viral reactions and controversy monitoring.
    - Reddit can be used to test long-form engagement and deep feedback.
    """
    )


# === Tab 2: Content Types ===
with tabs[2]:
    st.subheader("🧩 Content Format Trends (Instagram + Twitter)")
    content_type_trend["month"] = content_type_trend["month"].astype(str)
    pivot = content_type_trend.pivot_table(
        index="month", columns="content_type", values="count", aggfunc="sum"
    ).fillna(0)
    st.area_chart(pivot)

    # datas
    # import pandas as pd

    df_avg_engagement = pd.DataFrame(
        {
            "content_type": ["country", "gaming", "other"],
            "Avg Likes (Instagram)": [7232530.46, 523905.00, 4569579.24],
        }
    )

    df_twitter = pd.DataFrame(
        {
            "content_type": [
                "music",
                "country",
                "other",
                "gaming",
                "viral",
                "meme",
                "reaction",
                "livestream",
            ],
            "Avg Likes (Twitter)": [
                117966,
                298171.1,
                109240.7,
                66626.6,
                83028,
                174657.3,
                82199.2,
                75494,
            ],
            "Avg Views (Twitter)": [
                5764902,
                22166600,
                12115399.74,
                10780360,
                4558568.33,
                14281100,
                5716589,
                1986135,
            ],
            "Like/View % (Twitter)": [2.05, 1.34, 0.90, 0.62, 1.82, 1.22, 1.44, 3.80],
        }
    )

    df_youtube_top = pd.DataFrame(
        {
            "content_type": [
                "music",
                "other",
                "country",
                "gaming",
                "meme",
                "viral",
                "reaction",
            ],
            "Title": [
                "IShowSpeed - Shake (Official Music Video)",
                "I Played Football with Ronaldo Jr.",
                "i met ronaldo 🇵🇹",
                "speed vs adin 1v1 basketball",
                "i just found out i’m a famous meme on tiktok..💔 “JUST GIVE IT TO ME”",
                "this is crazy💔",
                "HOW I LOST MY V CARD STORYTIME👀 (VIDEO INCLUDED)",
            ],
            "Views": [227676271, 26053284, 23980932, 5988569, 587585, 304584, 124634],
        }
    )

    df_content_counts_instagram = pd.DataFrame(
        {"content_type": ["other", "country", "gaming"], "count": [31, 13, 1]}
    )

    df_cross_platform = pd.DataFrame(
        {
            "content_type": [
                "music",
                "country",
                "other",
                "gaming",
                "viral",
                "meme",
                "reaction",
                "livestream",
            ],
            "Avg Likes (Twitter)": [
                117966,
                298171.1,
                109240.7,
                66626.6,
                83028,
                174657.3,
                82199.2,
                75494,
            ],
            "Avg Views (Twitter)": [
                5764902,
                22166600,
                12115399.74,
                10780360,
                4558568.33,
                14281100,
                5716589,
                1986135,
            ],
            "Like/View % (Twitter)": [2.05, 1.34, 0.90, 0.62, 1.82, 1.22, 1.44, 3.80],
            "Avg Views (YouTube)": [
                22835601.69,
                7961375.67,
                589360.28,
                504694.07,
                188726.67,
                95912.64,
                44096.8,
                0,
            ],
            "Avg Likes (Instagram)": [0, 7232530.46, 4569579.24, 523905, 0, 0, 0, 0],
        }
    )

    # Engagement by Content Type
    fig = px.bar(
        df_avg_engagement,
        x="content_type",
        y="Avg Likes (Instagram)",
        title="Instagram: Avg Likes by Content Type",
    )
    st.plotly_chart(fig)

    fig2 = px.scatter(
        df_twitter,
        x="Avg Views (Twitter)",
        y="Avg Likes (Twitter)",
        size="Like/View % (Twitter)",
        color="content_type",
        title="Twitter: Engagement Efficiency (Likes vs Views)",
    )
    st.plotly_chart(fig2)

    # Top Performing Content
    st.subheader("Top YouTube Videos by Views")
    st.dataframe(df_youtube_top.sort_values(by="Views", ascending=False).head(5))

    # Content Frequency & Dominance
    fig = px.pie(
        df_content_counts_instagram,
        names="content_type",
        values="count",
        title="Instagram Content Distribution",
    )
    st.plotly_chart(fig)

    # Engagement Efficiency Overview
    st.subheader("Cross-Platform Content Efficiency")
    st.dataframe(df_cross_platform.style.background_gradient(axis=0, cmap="Blues"))

    st.markdown(
        """
    ### 📌 Strategic Insights:
    - **Country** content dominates Instagram & YouTube in engagement.
    - **Music** drives scale — especially on YouTube (~22M avg views).
    - **Livestream** content shows high Like/View % — leverage for real-time interaction.
    - **Other**, **meme**, and **reaction** provide variety but vary by platform.
    """
    )

    st.markdown(
        """
    ### ✅ Final Takeaways:
    - Double down on **Country**-themed content — consistently top-performing across all platforms.
    - Use **Music** for reach; it’s the best-performing format on YouTube.
    - Twitter: Use **memes & livestreams** to trigger viral reactions.
    - Instagram: Prioritize **visually rich country & lifestyle content**.
    - YouTube: Focus on **music, country, and reaction formats** with strong thumbnails.
    """
    )


# === Tab 3: Future Predictions ===
with tabs[3]:
    st.subheader("📈 YouTube Views and Subscriber Forecast")

    yt_views["Month"] = pd.to_datetime(yt_views["Month"], errors="coerce")
    sub_forecast["Date"] = pd.to_datetime(sub_forecast["Date"])

    forecast_start_date_view = pd.to_datetime("2024-06-01")
    forecast_start_date_sub = pd.to_datetime("2025-07-01")

    import altair as alt

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("**Forecasted Monthly Views**")
        base_views = alt.Chart(yt_views).encode(x="Month:T")

        line_views = base_views.mark_line(point=True, color="steelblue").encode(
            y=alt.Y("Predicted Views:Q", title="Views"),
            tooltip=["Month:T", "Predicted Views"],
        )

        rule = (
            alt.Chart(pd.DataFrame({"x": [forecast_start_date_view]}))
            .mark_rule(color="red", strokeDash=[5, 5])
            .encode(x="x:T")
        )

        st.altair_chart(
            (line_views + rule).properties(height=400), use_container_width=True
        )

    with col2:
        st.markdown("**Subscriber Forecast**")
        base_subs = alt.Chart(sub_forecast).encode(x="Date:T")

        line_subs = base_subs.mark_line(point=True, color="deepskyblue").encode(
            y=alt.Y("Predicted Subscribers:Q", title="Subscribers"),
            tooltip=["Date:T", "Predicted Subscribers"],
        )

        rule2 = (
            alt.Chart(pd.DataFrame({"x": [forecast_start_date_sub]}))
            .mark_rule(color="red", strokeDash=[5, 5])
            .encode(x="x:T")
        )

        st.altair_chart(
            (line_subs + rule2).properties(height=400), use_container_width=True
        )

    with st.expander("🔍 What Does the Forecast Tell Us?", expanded=False):
        st.markdown(
            """
        **Future Trajectory of IShowSpeed**

        Based on predictive analytics using linear regression models on historical YouTube data:

        - 📈 **Views**: Forecasted to increase steadily through mid-2026.
        - 👥 **Subscribers**: Projected to surpass current milestones and grow continuously.
        - 🧠 **Implications**:
            - His content strategy is effective — consistently high retention and reach.
            - He remains relevant and influential in the creator ecosystem.
            - His growth opens up more monetization, sponsorship, and brand collaboration opportunities.

        🔮 **Conclusion**: Strong growth trend with no signs of plateauing over the next 12–18 months.
        """
        )

    st.subheader("📲 Fan-Mentioned Platforms")
    # Create Altair bar chart
    bar_chart = (
        alt.Chart(platform_freq)
        .mark_bar()
        .encode(
            x=alt.X("Platform:N", title="Platform"),
            y=alt.Y("Mentions:Q", title="Number of Mentions"),
            color=alt.Color("Platform:N", legend=None),
            tooltip=["Platform", "Mentions"],
        )
        .properties(
            title="Mentions of Streaming Platforms by Fans", width=500, height=300
        )
        .configure_axisX(labelAngle=0)
    )

    st.altair_chart(bar_chart, use_container_width=True)

    with st.expander("🔍 Interpretation: Potential Platforms for Future Growth"):
        st.markdown(
            """
        Based on fan discussions extracted from IShowSpeed's Instagram and Twitter content, **YouTube** remains the dominant platform with the highest number of direct mentions, indicating a strong, loyal base.

        However, there is noticeable fan interest in emerging platforms such as:

        - **Twitch** — still garners support despite past bans  
        - **TikTok** — short-form and live content potential aligns well with Speed's energetic style  
        - **Kick** — gaining traction among streamers and mentioned by fans as a possible alternative

        These insights suggest that while **YouTube** will likely remain his primary platform, **expansion into TikTok LIVE or Kick** could open new audience segments, particularly among younger or international viewers. These platforms also offer more **live engagement, viral reach**, and **monetization opportunities**.
        """
        )

    st.markdown("### 🔄 Content Format Trends (Recent 6 Months)")

    # Sum total for selected categories
    categories_to_show = ["country", "gaming", "other"]
    available_categories = [
        col for col in categories_to_show if col in content_trend.columns
    ]
    category_totals = content_trend[available_categories].sum().reset_index()
    category_totals.columns = ["Content Type", "Total Posts"]

    # Create bar chart
    chart = (
        alt.Chart(category_totals)
        .mark_bar()
        .encode(
            x=alt.X("Content Type:N", title="Content Type"),
            y=alt.Y("Total Posts:Q", title="Total Post Count"),
            color=alt.Color("Content Type:N", legend=None),
            tooltip=["Content Type", "Total Posts"],
        )
        .properties(
            title="Total Mentions by Content Type (All Months)", width=500, height=350
        )
        .configure_axisX(labelAngle=0)
    )

    st.altair_chart(chart, use_container_width=True)

    with st.expander("📌 New Video Formats (Content Type Trends)", expanded=False):
        st.markdown(
            """
        An analysis of IShowSpeed's recent Instagram and Twitter posts over the past 6 months reveals that the majority of content falls under the **"other"** category, indicating diverse or less classifiable formats.  
        Among recognizable categories, **"gaming"** content maintains a consistent presence, underscoring its role as a core part of his content strategy.  
        Mentions of **"country"**-themed posts — often tied to travel or international collaborations — appear in smaller volume but suggest continued audience interest in his global reach and travel-related content.

        This trend suggests that while Speed remains experimental in his formats:
        - 🎮 **Gaming** remains a foundational content pillar  
        - 🌍 There’s potential to scale up travel, culture, or globally themed content, especially around international events or tours  
        - 📺 Future content strategies could benefit from exploring more defined or recurring series formats to strengthen audience recall
        """
        )

    st.subheader("🌍 Which Country will he go next?")
    # Custom color mapping for countries
    country_colors = {
        "Portugal": "#006600",  # green
        "Brazil": "#009C3B",  # green
        "Philippines": "#0038A8",  # blue
        "USA": "#B22234",
        "UK": "#00247D",
        "Argentina": "#FF9933",
        "Hong Kong": "#BC002D",
        "China": "#DE2910",
        "Mongolia": "#0055A4",
        "Netherlands": "#AA151B",
    }

    # Create color scale
    color_scale = alt.Scale(
        domain=list(country_colors.keys()), range=list(country_colors.values())
    )

    # Chart
    chart = (
        alt.Chart(country_mentions)
        .mark_bar()
        .encode(
            x=alt.X("Label:N", title="Country", sort="-y", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("Mentions:Q", title="Mentions"),
            color=alt.Color("Label:N", scale=color_scale, legend=None),
            tooltip=["Label", "Mentions"],
        )
        .properties(title="Top Countries Mentioned by Fans", width=600, height=400)
    )

    st.altair_chart(chart, use_container_width=True)

    with st.expander("📌 Which Country Will He Go Next?", expanded=False):
        st.markdown(
            """
        Based on fan interactions and post content, the top mentioned countries include **Portugal**, **Brazil**, and **China**.  
        These mentions suggest high relevance in IShowSpeed’s recent content, likely tied to **football culture** and **global engagement** — for example, **Portugal is the home of Cristiano Ronaldo**.

        Given this trend, it is plausible that his next international appearance or content focus could involve a **collaboration**, **travel vlog**, or **live event** in one of these regions:
        - 🇵🇹 **Portugal** – strongest signal, high emotional and cultural value  
        - 🇧🇷 **Brazil** – passionate fanbase and sports synergy  
        - 🇨🇳 **China** – strong social platform activity and global expansion potential
        """
        )

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
        "Other": "#CCCCCC",
    }

    color_scale = alt.Scale(
        domain=list(collab_colors.keys()), range=list(collab_colors.values())
    )

    # Altair Chart
    # Sort data manually by Mentions (descending)
    collab_mentions_sorted = collab_mentions.sort_values(by="Mentions", ascending=False)

    # Altair Chart
    chart = (
        alt.Chart(collab_mentions_sorted)
        .mark_bar()
        .encode(
            x=alt.X(
                "Collaborator:N", title="Collaborator", axis=alt.Axis(labelAngle=0)
            ),
            y=alt.Y("Mentions:Q", title="Mentions"),
            color=alt.Color("Collaborator:N", scale=color_scale, legend=None),
            tooltip=["Collaborator", "Mentions"],
        )
        .properties(title="Top Collaboration Mentions by Fans", width=600, height=400)
    )

    st.altair_chart(chart, use_container_width=True)

    with st.expander("📌 Collaboration Indicators", expanded=False):
        st.markdown(
            """
        Analysis of IShowSpeed's recent Instagram and Twitter posts reveals a **strong fan-driven interest in collaborations** — particularly with **Cristiano Ronaldo**, who dominates mentions by a significant margin.  
        **Lionel Messi** also features notably, indicating **sustained engagement with football-related content**.  
        The use of the word **"with"** in many posts reinforces the collaborative nature of these mentions.

        This suggests that:
        - 🏆 **Fans are highly engaged** with content involving global sports icons  
        - 🤝 **Collaborations**, especially **in-person** or themed around **football**, are likely to generate viral traction  
        - 📸 There’s clear potential for **strategic content** involving athlete interactions, sports-themed challenges, or co-streamed events
        """
        )

# === Tab 4: Comparisons ===
with tabs[4]:
    st.subheader("📌 Comparison with Other Creators")

    col1, col2, col3, col4 = st.columns([1, 2, 1, 2])

    with col1:
        st.image("mrbeast_picture.jpg", caption="MrBeast", use_container_width=True)

    with col2:
        st.markdown(
            """
        **MrBeast** (Jimmy Donaldson) is an American YouTuber and philanthropist known for his over-the-top challenges, large-scale giveaways, and record-breaking stunts. 
        Since launching in 2012, he’s become one of the fastest-growing creators on YouTube, combining jaw-dropping spectacles with real-world impact.
        """
        )

    with col3:
        st.image("dojacat_picture.jpg", caption="Doja Cat", use_container_width=True)

    with col4:
        st.markdown(
            """
        **Doja Cat** (Amala Ratna Zandile Dlamini) is an American singer, rapper, and producer whose eclectic style and viral hits—like “Say So” and “Kiss Me More”—
        have earned her multiple Grammy nominations. She’s built a devoted following through genre-blending music, playful visuals, and direct fan engagement.
        """
        )

    # 2. Subscriber Growth Chart
    df_sub = index_comparison.melt(
        id_vars="Day",
        value_vars=["MrBeast_Sub", "IShowSpeed_Sub", "DojaCat_Sub"],
        var_name="Creator",
        value_name="Subscriber Index",
    ).replace(
        {
            "MrBeast_Sub": "MrBeast",
            "IShowSpeed_Sub": "IShowSpeed",
            "DojaCat_Sub": "Doja Cat",
        }
    )

    sub_chart = (
        alt.Chart(df_sub)
        .mark_line(interpolate="monotone", strokeWidth=3)
        .encode(
            x=alt.X("Day:T", axis=alt.Axis(title="Date", format="%Y-%m")),
            y=alt.Y("Subscriber Index:Q", axis=alt.Axis(title="Index (Start=1.0)")),
            color=alt.Color(
                "Creator:N",
                legend=alt.Legend(title="Creator"),
                scale=alt.Scale(range=["steelblue", "orange", "green"]),
            ),
        )
        .properties(
            width=600, height=300, title="Normalized Subscriber Growth Comparison"
        )
        .configure_title(fontSize=16, anchor="start")
        .configure_axis(labelFontSize=12, titleFontSize=14)
    )

    st.subheader("🔢 Normalized Subscriber Growth")
    st.altair_chart(sub_chart, use_container_width=True)

    # 3. View Growth Chart
    df_view = index_comparison.melt(
        id_vars="Day",
        value_vars=["MrBeast_View", "IShowSpeed_View", "DojaCat_View"],
        var_name="Creator",
        value_name="View Index",
    ).replace(
        {
            "MrBeast_View": "MrBeast",
            "IShowSpeed_View": "IShowSpeed",
            "DojaCat_View": "Doja Cat",
        }
    )

    view_chart = (
        alt.Chart(df_view)
        .mark_line(interpolate="monotone", strokeWidth=3)
        .encode(
            x=alt.X("Day:T", axis=alt.Axis(title="Date", format="%Y-%m")),
            y=alt.Y("View Index:Q", axis=alt.Axis(title="Index (Start=0)")),
            color=alt.Color(
                "Creator:N",
                legend=alt.Legend(title="Creator"),
                scale=alt.Scale(range=["steelblue", "orange", "green"]),
            ),
        )
        .properties(width=600, height=300, title="Normalized View Growth Comparison")
        .configure_title(fontSize=16, anchor="start")
        .configure_axis(labelFontSize=12, titleFontSize=14)
    )

    st.subheader("📈 Normalized View Growth")
    st.altair_chart(view_chart, use_container_width=True)

    # Bar Chart: Subscriber Growth
    st.subheader("📈 Subscriber Growth (%)")
    st.bar_chart(creator_comparison.set_index("Creator")["Subscriber Growth (%)"])

    # Bar Chart: Total Twitter Engagement
    st.subheader("🐦 Total Twitter Engagement")
    st.bar_chart(creator_comparison.set_index("Creator")["Total Twitter Engagement"])

    # Grouped Bar Chart: Engagement Ratios
    st.subheader("💬 Engagement Ratios (Twitter)")

    import numpy as np

    # Map creator names to your already-loaded DataFrames
    mrbeast_tweets = pd.read_csv("mrbeast_tweets.csv")
    ishowspeed_tweets = pd.read_csv("ishowspeed_tweets.csv")
    dojacat_tweets = pd.read_csv("dojacat_tweets.csv")

    dfs = {
        "MrBeast": mrbeast_tweets,
        "IShowSpeed": ishowspeed_tweets,
        "Doja Cat": dojacat_tweets,
    }

    results = []
    for creator, df in dfs.items():
        # drop any rows where Likes is zero or missing, to avoid division errors
        df2 = df[df["Likes"] > 0].copy()

        avg_replies_to_likes = (df2["Replies"] / df2["Likes"]).mean()
        avg_retweets_to_likes = (df2["Retweets"] / df2["Likes"]).mean()

        results.append(
            {
                "Creator": creator,
                "Avg Replies-to-Likes Ratio": round(avg_replies_to_likes, 4),
                "Avg Retweets-to-Likes Ratio": round(avg_retweets_to_likes, 4),
            }
        )

    summary_df = pd.DataFrame(results)

    fig = px.bar(
        summary_df,
        x="Creator",
        y=["Avg Replies-to-Likes Ratio", "Avg Retweets-to-Likes Ratio"],
        barmode="group",
        labels={"value": "Ratio", "variable": "Metric"},
        color_discrete_map={
            "Avg Replies-to-Likes Ratio": "skyblue",
            "Avg Retweets-to-Likes Ratio": "orange",
        },
        title="🐦 Twitter Engagement Ratios",
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("What Sets IShowSpeed Apart from Others?")

    # Commentary
    st.markdown(
        """
    - Unfiltered, Raw, and Relatable Content
    - Engagement Through Audience Interaction
    - Flexibility Across Platforms
    """
    )

    st.subheader("What Can Be Learned from His Success?")

    # Commentary
    st.markdown(
        """
    - The Power of Uniqueness and Authenticity
    - Audience Engagement is Key
    - Embrace Virality and Memes
    """
    )

# === Tab 5: Conclusions ===
with tabs[5]:
    st.subheader("📊 IShowSpeed Growth Trends")

    # --- Monthly Growth Data ---
    df = pd.read_csv("ishowspeed_subscriber_growth.csv")
    # --- Monthly Growth Aggregation ---
    df["Day"] = pd.to_datetime(df["Day"])
    df["Month"] = df["Day"].dt.to_period("M")
    monthly = (
        df.groupby("Month")
        .agg({"Subscribers Gained": "sum", "Views Gained": "sum"})
        .reset_index()
    )
    monthly["Month"] = monthly["Month"].dt.to_timestamp()

    # Spike detection
    sub_mean = monthly["Subscribers Gained"].mean()
    sub_std = monthly["Subscribers Gained"].std()
    view_mean = monthly["Views Gained"].mean()
    view_std = monthly["Views Gained"].std()

    monthly["Sub Spike"] = monthly["Subscribers Gained"] > (sub_mean + 2 * sub_std)
    monthly["View Spike"] = monthly["Views Gained"] > (view_mean + 2 * view_std)

    # --- Plotly: Monthly Subscriber Growth ---
    fig1 = px.line(
        monthly,
        x="Month",
        y="Subscribers Gained",
        title="Monthly Subscriber Growth of IShowSpeed",
    )
    fig1.add_trace(
        go.Scatter(
            x=monthly[monthly["Sub Spike"]]["Month"],
            y=monthly[monthly["Sub Spike"]]["Subscribers Gained"],
            mode="markers+text",
            marker=dict(size=10, color="red"),
            text=monthly[monthly["Sub Spike"]]["Subscribers Gained"].apply(
                lambda x: f"{x:,}"
            ),
            textposition="top center",
            name="Spike",
        )
    )
    st.plotly_chart(fig1, use_container_width=True)

    # --- Plotly: Monthly View Growth ---
    fig2 = px.line(
        monthly, x="Month", y="Views Gained", title="Monthly View Growth of IShowSpeed"
    )
    fig2.add_trace(
        go.Scatter(
            x=monthly[monthly["View Spike"]]["Month"],
            y=monthly[monthly["View Spike"]]["Views Gained"],
            mode="markers+text",
            marker=dict(size=10, color="red"),
            text=monthly[monthly["View Spike"]]["Views Gained"].apply(
                lambda x: f"{x:,}"
            ),
            textposition="top center",
            name="Spike",
        )
    )
    st.plotly_chart(fig2, use_container_width=True)

    # --- Audience Demographics ---
    st.subheader("🌍 Audience Demographics (Top 10 Countries)")

    # Extract country info
    ishowspeed_followers_location = pd.read_csv("ishowspeed_followers_location.csv")
    ishowspeed_followers_location = ishowspeed_followers_location.dropna(
        subset=["location"]
    )
    us_states = {
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WI",
        "WV",
        "WY",
    }

    def extract_country(loc):
        parts = loc.split(",")
        last = parts[-1].strip()
        if last.upper() in us_states or last.upper() in ["USA", "US", "UNITED STATES"]:
            return "United States"
        return last

    ishowspeed_followers_location["country"] = ishowspeed_followers_location[
        "location"
    ].apply(extract_country)
    country_counts = (
        ishowspeed_followers_location["country"].value_counts().reset_index()
    )
    country_counts.columns = ["Country", "Count"]
    top10 = country_counts.head(10)

    # Plotly horizontal bar chart
    import plotly.colors as pc

    fig3 = px.bar(
        top10.sort_values("Count", ascending=False),
        x="Count",
        y="Country",
        orientation="h",
        title="Top 10 IShowSpeed Follower Countries",
        color="Country",
        color_discrete_sequence=pc.qualitative.Set3,
    )
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)


# === Tab 6: Conclusions ===
with tabs[6]:
    st.header("🔮 Final Thoughts & Future")
    st.markdown(
        """
    - **Future Growth**: Forecast indicates steady viewership and subscriber growth.
    - **Next Country?** Brazil and Portugal show strong signals from audience mentions.
    - **New Formats**: Strong rise in skits, music-related content, and meme formats.
    - **Opportunities**: Potential to expand into music collabs, brand deals, or live event streams.
    """
    )
