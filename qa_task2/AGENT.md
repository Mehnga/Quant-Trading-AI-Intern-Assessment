# AGENT.md

## How My Attribution Agent Works (Beginner Explanation)

This document explains, in simple steps, how my attribution agent works to analyze trading strategies and summarize their performance.

### 1. Input (Getting the Data)
- The agent starts by loading a file called `trade_book.json`.
- This file contains a list of trades, with details like which strategy was used and how much profit or loss (PnL) each trade made.

### 2. Grouping (Organizing the Data)
- The agent looks at all the trades and groups them by the "strategy" used.
- For each strategy, it adds up all the PnL values to get the total profit or loss for that strategy.

### 3. Analysis (Finding the Top Strategies)
- The agent sorts the strategies to find the top 5 (by the biggest absolute PnL, whether profit or loss).
- This helps focus on the most important or impactful strategies.

### 4. Summary (Explaining the Results)
- For each of the top 5 strategies, the agent uses an AI model (TinyGPT2) to generate a short explanation of why that strategy performed the way it did.
- These explanations are saved in a text file (`text_summary.txt`) for easy reading.
- The total PnL for each strategy is also saved in a file (`output.json`).

### 5. Output (Saving the Results)
- The agent prints messages to show what it's doing at each step.
- At the end, you get:
  - A JSON file with the total PnL for each strategy
  - A text file with human-readable summaries for the top strategies

---

**In summary:**
- The agent takes trade data, groups it by strategy, analyzes which strategies mattered most, and uses AI to explain the results in simple language. 