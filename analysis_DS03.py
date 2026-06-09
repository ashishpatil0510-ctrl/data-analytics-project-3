"""
— Marketing Funnel & Conversion Analysis
Bank Marketing Dataset | 

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("=" * 64)
print("FUTURE_DS_03 — Marketing Funnel & Conversion Analysis")
print("=" * 64)

# ─────────────────────────────────────────
# 1. LOAD & CLEAN DATA
# ─────────────────────────────────────────
df = pd.read_csv('bank-additional-full.csv', sep=';')
print(f"\n[DATA LOADED]  Rows: {df.shape[0]:,}  |  Columns: {df.shape[1]}")

# Engineer features
df['converted']   = (df['y'] == 'yes').astype(int)
df['call_bucket'] = pd.cut(df['campaign'], bins=[0,1,2,3,5,10,100],
                            labels=['1 call','2 calls','3 calls','4-5 calls','6-10 calls','10+ calls'])
df['age_group']   = pd.cut(df['age'], bins=[0,25,35,45,55,65,100],
                            labels=['<25','25-35','35-45','45-55','55-65','65+'])

total = len(df)
converted_n = df['converted'].sum()

# ─────────────────────────────────────────
# 2. KEY PERFORMANCE INDICATORS
# ─────────────────────────────────────────
overall_cvr     = converted_n / total * 100
avg_calls_conv  = df[df['converted']==1]['campaign'].mean()
avg_calls_noconv= df[df['converted']==0]['campaign'].mean()
avg_dur_conv    = df[df['converted']==1]['duration'].mean()
avg_dur_noconv  = df[df['converted']==0]['duration'].mean()
cellular_cvr    = df[df['contact']=='cellular']['converted'].mean()*100
telephone_cvr   = df[df['contact']=='telephone']['converted'].mean()*100
prev_success_cvr= df[df['poutcome']=='success']['converted'].mean()*100

print(f"""
╔══════════════════════════════════════════════════════╗
║           KEY PERFORMANCE INDICATORS                 ║
╠══════════════════════════════════════════════════════╣
║  Total Leads Contacted   : {total:>8,}               ║
║  Total Conversions       : {converted_n:>8,}               ║
║  Overall Conversion Rate : {overall_cvr:>8.2f}%              ║
║  Cellular Channel CVR    : {cellular_cvr:>8.2f}%              ║
║  Telephone Channel CVR   : {telephone_cvr:>8.2f}%              ║
║  Prev. Success → CVR     : {prev_success_cvr:>8.2f}%              ║
║  Avg Calls (Converted)   : {avg_calls_conv:>8.2f}               ║
║  Avg Calls (Not Conv.)   : {avg_calls_noconv:>8.2f}               ║
║  Avg Duration (Conv.)    : {avg_dur_conv:>8.0f}s              ║
║  Avg Duration (Not Conv.): {avg_dur_noconv:>8.0f}s              ║
╚══════════════════════════════════════════════════════╝
""")

# ─────────────────────────────────────────
# 3. MARKETING FUNNEL STAGES
# ─────────────────────────────────────────
stages = {
    'Contacted (All Leads)':       len(df),
    'Engaged (Call >0s)':          len(df[df['duration']>0]),
    'Interested (Call >2min)':     len(df[df['duration']>120]),
    'Hot Lead (Call >5min)':       len(df[df['duration']>300]),
    'Converted (Subscribed)':      converted_n,
}
prev = None
print("── FUNNEL STAGES ──────────────────────────────────────────")
for stage, count in stages.items():
    pct_total = count / total * 100
    drop = f"  ↓ {(1-count/prev)*100:.1f}% drop-off" if prev else ""
    bar  = '█' * int(pct_total / 2)
    print(f"  {stage:<30} {count:>6,}  ({pct_total:>5.1f}%) {bar}{drop}")
    prev = count

# ─────────────────────────────────────────
# 4. CHANNEL PERFORMANCE
# ─────────────────────────────────────────
print("\n── CHANNEL CONVERSION RATES ───────────────────────────────")
ch = df.groupby('contact')['converted'].agg(['sum','count','mean']).reset_index()
ch.columns = ['Channel','Conversions','Contacts','CVR']
ch['CVR%'] = (ch['CVR']*100).round(2)
print(ch[['Channel','Contacts','Conversions','CVR%']].to_string(index=False))

# ─────────────────────────────────────────
# 5. MONTHLY PERFORMANCE
# ─────────────────────────────────────────
print("\n── MONTHLY CONVERSION RATES ───────────────────────────────")
monthly = df.groupby('month')['converted'].agg(['sum','count','mean']).reset_index()
monthly.columns = ['Month','Conversions','Contacts','CVR']
monthly['CVR%'] = (monthly['CVR']*100).round(1)
monthly = monthly.sort_values('CVR%', ascending=False)
for _, r in monthly.iterrows():
    bar = '█' * int(r['CVR%'] / 2)
    print(f"  {r['Month']:<4}  {r['Contacts']:>5,} contacts  {r['CVR%']:>5.1f}%  {bar}")

# ─────────────────────────────────────────
# 6. SEGMENT ANALYSIS
# ─────────────────────────────────────────
print("\n── CONVERSION BY JOB ──────────────────────────────────────")
job_c = df.groupby('job')['converted'].agg(['sum','count','mean']).reset_index()
job_c.columns = ['Job','Conversions','Contacts','CVR']
job_c['CVR%'] = (job_c['CVR']*100).round(1)
for _, r in job_c.sort_values('CVR%', ascending=False).iterrows():
    bar = '█' * int(r['CVR%'] / 2)
    print(f"  {r['Job']:<16} {r['CVR%']:>5.1f}%  {bar}")

print("\n── CONVERSION BY CALL VOLUME ──────────────────────────────")
cb = df.groupby('call_bucket', observed=True)['converted'].agg(['sum','count','mean']).reset_index()
cb.columns = ['Calls','Conversions','Contacts','CVR']
cb['CVR%'] = (cb['CVR']*100).round(1)
for _, r in cb.iterrows():
    bar = '█' * int(r['CVR%'] / 2)
    print(f"  {r['Calls']:<12} {r['CVR%']:>5.1f}%  {bar}")

print("\n── PREVIOUS CAMPAIGN OUTCOME ──────────────────────────────")
po = df.groupby('poutcome')['converted'].agg(['sum','count','mean']).reset_index()
po.columns = ['Prev Outcome','Conversions','Contacts','CVR']
po['CVR%'] = (po['CVR']*100).round(1)
for _, r in po.iterrows():
    print(f"  {r['Prev Outcome']:<14} {r['CVR%']:>5.1f}%  ({r['Conversions']:,} / {r['Contacts']:,})")

print("\n── CONVERSION BY AGE GROUP ────────────────────────────────")
ag = df.groupby('age_group', observed=True)['converted'].agg(['sum','count','mean']).reset_index()
ag.columns = ['Age','Conversions','Contacts','CVR']
ag['CVR%'] = (ag['CVR']*100).round(1)
for _, r in ag.iterrows():
    bar = '█' * int(r['CVR%'] / 2)
    print(f"  {r['Age']:<10} {r['CVR%']:>5.1f}%  {bar}")

# ─────────────────────────────────────────
# 7. EXPORT SUMMARIES
# ─────────────────────────────────────────
monthly.to_csv('monthly_conversion.csv', index=False)
ch.to_csv('channel_performance.csv', index=False)
job_c.to_csv('job_conversion.csv', index=False)
cb.to_csv('callvolume_conversion.csv', index=False)

print("""
── INSIGHTS & RECOMMENDATIONS ─────────────────────────────

📉  BIGGEST DROP-OFF: Interested → Hot Lead stage loses
    60.4% of leads. This is the funnel's weakest point.

📞  CHANNEL WIN: Cellular converts at 14.7% vs telephone
    at 5.2% — cellular is 2.8x more effective.

🗓️  BEST MONTHS: Mar, Dec, Sep, Oct all above 40% CVR.
    May has 13,769 contacts but only 6.4% CVR — worst month.

👴  AGE INSIGHT: 65+ converts at 46.8%, <25 at 20.9%.
    Older segments are dramatically underserved in volume.

🏆  BEST JOB SEGMENTS: Students (31.4%) and Retired (25.2%)
    are top converters — target more of these profiles.

💡  REC 1: Reduce call volume after 3 attempts — CVR drops
    from 13% at 1 call to 3.1% at 10+ calls. Stop at 3.

💡  REC 2: Shift budget from telephone to cellular channel
    entirely — 2.8x better conversion rate.

💡  REC 3: Retarget previous campaign successes first —
    they convert at 65.1% vs 8.8% for new contacts.

💡  REC 4: Focus outreach in Mar/Sep/Oct/Dec windows.
    May campaigns waste budget at only 6.4% CVR.

💡  REC 5: Create dedicated tracks for Students and Retirees
    — highest CVR segments with room to scale volume.
""")

print("✅ Analysis complete. Open dashboard.html for the visual report.")
