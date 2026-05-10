import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(page_title='IPL Pulse', layout='wide')
st.title('IPL Pulse - Cricket and Stock Market Analyzer')
st.markdown('Analyzing IPL match results impact on NSE sponsor stocks 2008-2025')

conn = sqlite3.connect('ipl_stock.db')

col1, col2, col3 = st.columns(3)
total = pd.read_sql('SELECT COUNT(*) as c FROM event_study', conn).iloc[0,0]
seasons = pd.read_sql('SELECT COUNT(DISTINCT season) as c FROM event_study', conn).iloc[0,0]
positive = pd.read_sql('SELECT ROUND(100.0*SUM(CASE WHEN return_d1_pct>0 THEN 1 ELSE 0 END)/COUNT(*),1) as c FROM event_study', conn).iloc[0,0]

col1.metric('Total Events Analyzed', str(total))
col2.metric('IPL Seasons Covered', str(seasons))
col3.metric('Positive Return Rate', str(positive)+'%')

st.divider()
st.subheader('Team-wise Stock Impact After Win')
query = 'SELECT winner, sponsor, COUNT(*) as total_wins, ROUND(AVG(return_d1_pct),3) as avg_d1_return, ROUND(100.0*SUM(CASE WHEN return_d1_pct>0 THEN 1 ELSE 0 END)/COUNT(*),1) as win_rate_pct FROM event_study GROUP BY winner, sponsor ORDER BY avg_d1_return DESC'
df = pd.read_sql(query, conn)
st.dataframe(df, use_container_width=True)

st.subheader('Season-wise Average Return')
season_df = pd.read_sql('SELECT season, ROUND(AVG(return_d1_pct),3) as avg_return FROM event_study GROUP BY season ORDER BY season', conn)
fig, ax = plt.subplots(figsize=(12,4))
colors = ['green' if x > 0 else 'red' for x in season_df['avg_return']]
ax.bar(season_df['season'], season_df['avg_return'], color=colors)
ax.axhline(y=0, color='black', linewidth=0.8)
ax.set_xlabel('Season')
ax.set_ylabel('Avg D+1 Return (%)')
ax.set_title('Stock Market Reaction by IPL Season')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Match-level Explorer')
teams = ['All'] + sorted(pd.read_sql('SELECT DISTINCT winner FROM event_study', conn)['winner'].tolist())
selected = st.selectbox('Select Team', teams)
if selected == 'All':
    data = pd.read_sql('SELECT date, winner, sponsor, return_d1_pct, return_d2_pct, stage FROM event_study ORDER BY date DESC LIMIT 50', conn)
else:
    data = pd.read_sql(f'SELECT date, winner, sponsor, return_d1_pct, return_d2_pct, stage FROM event_study WHERE winner="{selected}" ORDER BY date DESC', conn)

st.dataframe(data, use_container_width=True)
conn.close()