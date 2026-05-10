# IPL Pulse - Cricket & Stock Market Impact Analyzer 🏏📈

## Project Overview
An end-to-end **data science project** analyzing the impact of IPL match results on NSE-listed sponsor company stock prices using **event study methodology**. This project combines cricket analytics with financial market analysis to uncover correlations between IPL match outcomes and sponsor stock performance.

## Key Findings
- **673 IPL match events** analyzed across 2008-2025
- **49% positive return rate** after team wins (D+1)
- **Best performer:** Deccan Chargers (SUNPHARMA) - **+1.5% avg return** with 67.7% win rate
- **RCB (UNITDSPR)** - **+0.591% avg return** with 68.4% win rate
- **KKR (JSWSTEEL)** - **+0.440% avg return** across 128 matches

## Features
✅ **Event Study Analysis** - Match date → D+1, D+2 stock return calculations  
✅ **SQL Database** - 673+ match events with stock price data  
✅ **NLP Sentiment Analysis** - News headline sentiment scoring  
✅ **Interactive Streamlit Dashboard** - Real-time data exploration  
✅ **Power BI Visualizations** - Team-wise stock impact charts  
✅ **Professional Charts** - Season-wise trends and sponsor comparisons  

## Tech Stack
- **Python 3.14** - Core language
- **Pandas & NumPy** - Data manipulation
- **SQLite** - Database (ipl_stock.db)
- **yFinance** - NSE stock data
- **TextBlob** - NLP sentiment analysis
- **Streamlit** - Interactive dashboard
- **Matplotlib & Seaborn** - Data visualization
- **Power BI** - Advanced analytics

## Project Structure




## Installation & Setup

### Prerequisites
- Python 3.13+
- pip package manager

### Steps
```bash
# Clone repository
git clone https://github.com/nikhilofficial7666/IPL-PULSE-PROJECT
cd IPL-PULSE-PROJECT

# Install dependencies
pip install pandas numpy yfinance textblob streamlit matplotlib seaborn

# Run Jupyter notebook for analysis
jupyter notebook 01_explore_data.ipynb

# Run Streamlit dashboard
streamlit run app.py
```

## Usage

### 1. Data Analysis (Jupyter Notebook)
```python
# Load IPL matches
matches = pd.read_csv('archive/matches.csv')

# Map teams to NSE sponsor stocks
sponsor_map = {
    'Mumbai Indians': 'RELIANCE',
    'Chennai Super Kings': 'INDIACEM',
    'Kolkata Knight Riders': 'JSWSTEEL',
    ...
}

# Event study analysis
event_df = calculate_stock_returns_after_win(matches, stock_data)
```

### 2. Interactive Streamlit Dashboard
```bash
streamlit run app.py
# Opens at localhost:8501
# Features: Team selector, season analysis, match explorer
```

### 3. SQL Queries for Insights
```sql
-- Top performing teams after wins
SELECT winner, sponsor, 
    COUNT(*) as total_wins,
    ROUND(AVG(return_d1_pct), 3) as avg_return,
    ROUND(100.0*SUM(CASE WHEN return_d1_pct>0 THEN 1 ELSE 0 END)/COUNT(*), 1) as win_rate_pct
FROM event_study
GROUP BY winner, sponsor
ORDER BY avg_return DESC;
```

## Results

### Stock Impact by Team (D+1 Returns)
| Team | Sponsor | Avg Return | Win Rate | Total Wins |
|------|---------|-----------|----------|-----------|
| Deccan Chargers | SUNPHARMA | +1.50% | 67.7% | 31 |
| RCB | UNITDSPR | +0.591% | 68.4% | 19 |
| KKR | JSWSTEEL | +0.440% | 53.1% | 128 |
| Mumbai Indians | RELIANCE | +0.184% | 52.3% | 130 |

### Season-wise Analysis
- **2009** - Best season (+2.60% avg return)
- **2014** - Strong performance (+1.03% return)
- **2025** - Positive trend (+0.47% return)

## Methodology

### Event Study Framework
1. **Event Definition**: IPL match win on date D
2. **Stock Price**: Match day (D) vs. next trading day (D+1) & (D+2)
3. **Return Calculation**: `(Price_D+1 - Price_D) / Price_D * 100`
4. **Analysis**: Aggregated by team, season, stage (league/playoffs)

### Why This Approach?
- **Academic rigor**: Event study used in financial research
- **Real-world relevance**: Cricket events impact stock markets
- **Unique angle**: No other fresher project combines IPL + NSE analysis
- **Scalable**: Can extend to other sports/leagues

## Dashboard Features
🔹 **3 Key Metrics** - Total events, seasons covered, positive return rate  
🔹 **Team Comparison** - Side-by-side sponsor stock performance  
🔹 **Season Trends** - Historical analysis of market reaction  
🔹 **Match Explorer** - Filter by team, view detailed D+1 & D+2 returns  

## Future Enhancements
- Real-time news sentiment analysis on match days
- Machine learning prediction model for stock movement
- Mobile app deployment
- API integration for live match data
- Comparison with other sports events (IPL vs PSL vs T20 World Cup)

## Key Learnings
✨ **Data Pipeline Design** - End-to-end workflow from raw data to insights  
✨ **SQL & Database** - Relational schema design for financial events  
✨ **Statistics** - Event study methodology, return calculations  
✨ **Visualization** - Storytelling with data through multiple mediums  
✨ **Full-stack** - Python backend + Streamlit frontend + database  

## Resume Talking Points
- "Analyzed 673 IPL match events using event study methodology - standard approach in financial research"
- "Built SQL-based event database with complex join operations across matches and stock data"
- "Discovered 68.4% win rate correlation for RCB sponsor stock after match wins"
- "Deployed interactive Streamlit dashboard for real-time data exploration"
- "Combined NLP sentiment analysis with quantitative financial analysis"

## Author
**Nikhil Kshirsagar**  
Data Science | Python | SQL | Machine Learning  
[GitHub](https://github.com/nikhilofficial7666) | [LinkedIn](https://www.linkedin.com/in/nikhil-kshirsagar)

## License
MIT License - Feel free to use for educational purposes

---

**Built with ❤️ for the data science community**

for diploy - ## Live Demo
[Click here to view the app](https://your-app-link.streamlit.app)
