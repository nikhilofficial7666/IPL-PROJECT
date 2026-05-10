You are a senior Data Scientist, Quant Analyst, and Software Engineer.

I am building a **production-ready, resume-level project** called:

**"IPL Pulse — Cricket Events & Stock Market Impact Analyzer"**

---

## 🎯 OBJECTIVE

Analyze whether the winning team in the Indian Premier League (IPL) has a measurable impact on the **next-day (D+1) and D+2 stock returns** of its sponsor company listed on NSE.

---

## 📦 DATA AVAILABLE

### IPL Dataset

* Matches (2008–2025)
* Columns: match_id, date, season, winner, stage

### Sponsor Mapping

* MI → RELIANCE
* CSK → INDIACEM
* KKR → JSWSTEEL
* RCB → UNITDSPR
* SRH → SUNPHARMA
* Delhi → GMR
* Punjab → CENTRALBK

### Stock Data

* Source: yfinance
* Frequency: Daily Close Prices
* Time Range: 2008–2025

### Database

* SQLite DB: `ipl_stock.db`
* Tables:

  * matches
  * stock_prices

---

## 🧠 TASK REQUIREMENTS

### 1. Event Study Analysis (CORE)

* For each match:

  * Identify sponsor of winning team
  * Compute:

    * Match day closing price (D0)
    * Next trading day (D+1)
    * D+2
  * Calculate:

    * % return D+1
    * % return D+2

* Handle:

  * Non-trading days
  * Missing values
  * Stock availability

---

### 2. Statistical Analysis

* Mean return by sponsor
* Overall average return
* Win vs Loss comparison (if possible)
* T-test to check statistical significance

---

### 3. Visualization

Use matplotlib/seaborn:

* Distribution of D+1 returns
* Boxplot by sponsor
* Time series overlay (IPL season vs stock movement)

---

### 4. NLP Sentiment Analysis (ADVANCED)

* Fetch match-related news or tweets (mock or real)
* Use TextBlob
* Compute sentiment score
* Correlate sentiment with stock movement

---

### 5. Streamlit App (IMPORTANT)

Build an interactive dashboard:

* Select team/sponsor
* Show:

  * Avg returns
  * Graphs
  * Match-level insights

---

### 6. Code Quality

* Modular code (functions/classes)
* Clean structure:

  * data/
  * notebooks/
  * src/
  * app/
* Add comments + docstrings

---

### 7. Output

Give:

* Complete working Python code
* Step-by-step execution instructions
* Expected outputs
* Folder structure
* Requirements.txt

---

### 8. Resume Impact

Make this project:

* Industry-level
* Unique (not generic Kaggle)
* Strong storytelling for recruiters

---

DO NOT give vague explanations.

Act like a mentor + senior engineer guiding me step-by-step.

Start from **Event Study Analysis implementation** and guide sequentially.

---

# ⚙️ 🔧 EXTRA INSTRUCTIONS (IMPORTANT — Yeh Claude ko alag se bolna)

Ye part aur bhi important hai 👇

---

## 🧠 HOW YOU SHOULD WORK

1. Break problem into small steps
2. Give code → then explain
3. Wait for my confirmation before next step
4. Debug like a senior engineer
5. Never assume data is clean
6. Always handle edge cases
7. Optimize for real-world use (not toy code)

---

## ⚠️ STRICT RULES

* No pseudo code — only working code
* No skipping steps
* No unnecessary theory
* Always print sample outputs
* Always validate results

---

## 💡 BEHAVIOR

* Act like my personal project mentor
* Help me build something that can impress recruiters
* Suggest improvements proactively

---

# 🎯 PRO TIP (Important)

Jab Claude output de:

👉 Blindly copy mat kar
👉 Har step run kar
👉 Error aaye → turant paste kar ke debug karwa

---

# 🔥 FINAL STRATEGY

Tu basically bana raha hai:

👉 Sports + Finance + Data Science combo project
👉 Yeh rare hai → resume pe standout karega

