import pandas as pd
import json
from transformers import pipeline
from datetime import datetime
import uuid
from tqdm import tqdm

# Load LLM model
print("[INFO] Loading open-source LLM...")
try:
    summarizer = pipeline("text-generation", model="sshleifer/tiny-gpt2", device=-1)
    print("[INFO] LLM model loaded.")
except Exception as e:
    print(f"[ERROR] Failed to load model: {e}")
    exit(1)

# Load trade_book.json
try:
    df = pd.read_json("trade_book.json")
    print(f"[INFO] Loaded {len(df)} trades from trade_book.json")
except Exception as e:
    print(f"[ERROR] Could not load trade_book.json: {e}")
    exit(1)

if 'strategy' not in df.columns or 'pnl' not in df.columns:
    print("[ERROR] Missing required columns: 'strategy' and/or 'pnl'")
    exit(1)

# Group by strategy
strategy_pnl_df = df.groupby("strategy")["pnl"].sum().reset_index()
strategy_pnl_df["pnl"] = strategy_pnl_df["pnl"].round(2)

# Save raw JSON output
pnl_dict = dict(zip(strategy_pnl_df["strategy"], strategy_pnl_df["pnl"]))

# Generate summaries 

print("[INFO] Generating AI explanations for top 5 strategies...")
summaries = []

top_strategies = strategy_pnl_df.copy()
top_strategies["abs_pnl"] = top_strategies["pnl"].abs()
top_strategies = top_strategies.sort_values(by="abs_pnl", ascending=False).head(5)

for _, row in tqdm(top_strategies.iterrows(), total=5):
    strategy = row["strategy"]
    pnl = row["pnl"]
    prompt = f"The strategy '{strategy}' had a total profit and loss (PnL) of {pnl} INR. Briefly explain the likely reason behind this performance."

    try:
        response = summarizer(prompt, max_new_tokens=30)[0]["generated_text"]
        explanation = response[len(prompt):].strip()
    except Exception as e:
        explanation = f"[ERROR] Summary generation failed: {e}"

    summaries.append({
        "strategy": strategy,
        "total_pnl": pnl,
        "summary": explanation
    })

# Save JSON data
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(pnl_dict, f, indent=2)
    print("[INFO] Saved output.json")

# Save human-readable summary
with open("text_summary.txt", "w", encoding="utf-8") as f:
    for item in summaries:
        f.write(
            f"Strategy: {item['strategy']}\n"
            f"Total PnL: ₹{item['total_pnl']}\n"
            f"Summary: {item['summary']}\n\n"
        )
    print("[INFO] Saved text_summary.txt")

integrity_token = f"{datetime.now().isoformat()}--{uuid.uuid4().hex}"
print(f"[INTEGRITY TOKEN] {integrity_token}")
