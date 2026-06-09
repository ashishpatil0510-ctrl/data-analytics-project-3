# Marketing Funnel & Conversion Analysis | Python + Chart.js | Data Analytics 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Analysis-150458?logo=pandas)
![Chart.js](https://img.shields.io/badge/Chart.js-Dashboard-ff6384)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tasks](https://img.shields.io/badge/All%20Tasks-3%20of%203-gold)

---

## 📌 Task Overview

## 📸 Dashboard Preview

![KPI Cards](1.png)
![Funnel Chart](2.png)
![Segment Analysis](3.png)

Analyze a bank's telemarketing campaign data to understand the lead-to-customer conversion funnel:
- Map **funnel stages** from contact → engaged → interested → hot lead → converted
- Identify **drop-off points** at each stage
- Evaluate **channel performance** (cellular vs telephone)
- Segment conversion rates by **job, age, education, month, call volume**
- Deliver **actionable recommendations** to improve overall CVR

---

## 📁 Project Structure

```
FUTURE_DS_03/
│
├── dashboard.html              ← 🎨 Interactive funnel dashboard (open in browser)
├── analysis.py                 ← 🐍 Full Python funnel analysis script
├── README.md                   ← 📄 This file
│
└── Dataset Files (from Kaggle):
    ├── bank-additional-full.csv   ← Primary dataset (41,188 rows)
    └── bank-full.csv              ← Secondary dataset (45,211 rows)
```

---

## 📊 Dataset — UCI Bank Marketing

| Field | Detail |
|---|---|
| **Source** | UCI Machine Learning Repository — Bank Marketing Dataset |
| **Primary File** | `bank-additional-full.csv` |
| **Rows** | 41,188 telemarketing call records |
| **Features** | 21 (age, job, marital, education, contact, month, duration, campaign, poutcome, etc.) |
| **Target** | `y` — Did the customer subscribe to a term deposit? (yes/no) |
| **Campaign Period** | 2008–2013 (Portuguese banking institution) |

---

## 🔢 Key Performance Indicators

| Metric | Value |
|---|---|
| Total Leads Contacted | **41,188** |
| Total Conversions | **4,640** |
| Overall CVR | **11.3%** |
| Cellular Channel CVR | **14.7%** |
| Telephone Channel CVR | **5.2%** |
| Prev. Success Re-contact CVR | **65.1%** |
| Avg Call Duration (Converted) | **553 seconds** |
| Avg Call Duration (Not Converted) | **221 seconds** |

---

## 🔻 Marketing Funnel Breakdown

| Stage | Count | % of Total | Drop-off |
|---|---|---|---|
| Contacted (All Leads) | 41,188 | 100.0% | — |
| Engaged (Call > 0s) | 41,184 | ~100.0% | ~0% |
| Interested (Call > 2 min) | 28,271 | 68.6% | **31.4%** |
| Hot Lead (Call > 5 min) | 11,204 | 27.2% | **60.4% ← Biggest leak** |
| Converted | 4,640 | 11.3% | 58.6% |

---

## 📈 Key Insights

### 1. 🚨 Biggest Funnel Leak — Interested → Hot Lead (60.4% drop-off)
Most leads disengage between 2–5 minutes into the call. This is the primary optimization target.

### 2. 📱 Cellular Dominates Telephone (2.8×)
| Channel | Contacts | CVR |
|---|---|---|
| Cellular | 26,144 | **14.7%** |
| Telephone | 15,044 | 5.2% |

### 3. 📅 Seasonal Performance
| Month | CVR |
|---|---|
| March | **50.6%** ← Best |
| December | 48.9% |
| September | 44.9% |
| **May** | **6.4%** ← Worst (highest volume!) |

### 4. 👤 Best Converting Segments
| Segment | CVR |
|---|---|
| Age 65+ | **46.8%** |
| Students | 31.4% |
| Retirees | 25.2% |
| Prior Campaign Success | 65.1% |

### 5. 📞 Diminishing Returns After 3 Calls
| Calls | CVR |
|---|---|
| 1 call | **13.0%** |
| 3 calls | 10.7% |
| 6-10 calls | 6.3% |
| 10+ calls | 3.1% |

---

## 💡 Recommendations

1. **Fix the Interested → Hot Lead drop-off**: Train agents with structured call scripts designed to extend call quality past 5 minutes.

2. **Switch entirely to cellular**: Reallocating telephone budget to cellular could increase conversions by up to 2.8×.

3. **Prioritize re-contact lists**: Previous campaign successes convert at 65.1% — always exhaust this list first before new outreach.

4. **Shift budget to Mar/Sep/Oct/Dec**: These months deliver 44–51% CVR. May campaigns waste budget at only 6.4%.

5. **Hard cap at 3 call attempts**: CVR drops from 13% to 3.1% beyond 10 calls. Stop wasting agent time on non-responders.

6. **Build dedicated tracks for Students, Retirees, and 65+**: Highest-converting segments — create tailored scripts and increase their volume.

---

## 🛠️ How to Run

### Prerequisites
```bash
pip install pandas numpy
```

### Run Analysis
```bash
# Place bank-additional-full.csv in same folder, then:
python analysis.py
```

### View Dashboard
Open `dashboard.html` in any modern browser — no server required.

---

## 🖼️ Dashboard Features

- ✅ 5 KPI summary cards
- ✅ Visual funnel with stage-by-stage drop-off percentages
- ✅ Channel comparison (Cellular vs Telephone)
- ✅ Previous campaign outcome impact
- ✅ Monthly CVR trend with contact volume overlay
- ✅ CVR by call volume (diminishing returns curve)
- ✅ Conversion by Job (horizontal segment bars)
- ✅ Conversion by Age Group (bar chart)
- ✅ Conversion by Education level
- ✅ Day-of-week performance (polar area chart)
- ✅ Call duration distribution (converted vs not)
- ✅ 6 insight cards with actionable recommendations

---

## 🧹 Data Cleaning & Feature Engineering

1. No missing values in the primary dataset — clean out-of-box
2. Target column `y` encoded as binary `converted` (1/0)
3. Funnel stages derived from `duration` field thresholds
4. `call_bucket` feature binned from `campaign` column
5. `age_group` feature binned from `age` column
6. Month ordered categorically for trend analysis

---

## 📚 Tools Used

| Tool | Purpose |
|---|---|
| Python + Pandas | Data cleaning, funnel metrics, segment analysis |
| Chart.js (CDN) | Interactive dashboard visualizations |
| HTML + CSS | Client-ready, single-file dashboard |

---

## 🏆 Internship Completion

| Task | Repo | Status |
|---|---|---|
| Task 1 — Sales Analytics | FUTURE_DS_01 | ✅ Complete |
| Task 2 — Churn & Retention | FUTURE_DS_02 | ✅ Complete |
| Task 3 — Marketing Funnel | FUTURE_DS_03 | ✅ Complete |

---
