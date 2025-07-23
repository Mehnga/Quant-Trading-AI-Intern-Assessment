# README.md

## How to Run the Code (Beginner Guide)

1. **Install Python**
   - Make sure you have Python installed on your computer (version 3.7 or higher is best).

2. **Install the Required Packages**
   - Open a terminal or command prompt in this project folder.
   - Run this command to install all the needed packages:
     ```
     pip install -r requirements.txt
     ```

3. **Prepare Your Input File**
   - Make sure you have a file called `trade_book.json` in the same folder.
   - This file should have a list of trades, with each trade having at least a `strategy` and `pnl` (profit and loss) value.

4. **Run the Script**
   - In the terminal, run:
     python signal_extractor.py
     
   - The script will process your data and create two output files: `output.json` and `text_summary.txt`.

---

## Sample Input

**trade_book.json**
```json
[
  {"strategy": "A", "pnl": 100},
  {"strategy": "B", "pnl": -50},
  {"strategy": "A", "pnl": 200},
  {"strategy": "C", "pnl": 30}
]
```

## Sample Output

**output.json**
```json
{
  "A": 300,
  "B": -50,
  "C": 30
}
```

**text_summary.txt**
```
Strategy: A
Total PnL: ₹300
Summary: (AI-generated explanation)

Strategy: B
Total PnL: ₹-50
Summary: (AI-generated explanation)

...etc.
```

---

## How the AI Tool Helped
- The AI tool (TinyGPT2) automatically writes a short explanation for the top 5 strategies based on their profit and loss.
- This makes it easier to understand why certain strategies performed well or badly, even if you are new to trading or data analysis.
- The tool saves you time by quickly summarizing the results in plain language.

**In short:**
- You just provide your trade data, and the agent does the grouping, analysis, and explanation for you! 