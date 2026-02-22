"""
python_master_v2.py
Comprehensive demo script:
- Core Python basics (brief)
- NumPy basics
- Pandas basics (DataFrame creation, IO)
- Matplotlib (basic plotting, save figure)
- SQLite (create DB, insert/query)
- Multithreading (ThreadPoolExecutor example)
- asyncio + aiohttp example (async HTTP fetch)
- requests (sync HTTP fetch)
- Small examples interleaved with comments and prints

Run: python python_master_v2.py
"""

import sys
import os
import math
import json
import re
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3
import asyncio

# Try imports that may not exist and give helpful error
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import requests
    import aiohttp
except Exception as e:
    print("One or more optional packages are missing. Install them with:")
    print("  pip install numpy pandas matplotlib requests aiohttp")
    print("Error:", e)
    # We'll still continue, but some sections will be skipped.
    # If you want, exit here: sys.exit(1)

# ---------------------------
# 1. Small refresher (core)
# ---------------------------
def core_demo():
    print("\n=== CORE PYTHON DEMO ===")
    a, b = 7, 4
    print("a + b =", a + b)
    print("Power, floor division, remainder:", a ** b, a // b, a % b)

    # function with *args, **kwargs
    def func(x, *args, **kwargs):
        return x, args, kwargs
    print("func:", func(1, 2, 3, name="Alice"))

    # generator
    def count_up(n):
        for i in range(n):
            yield i
    print("generator output:", list(count_up(5)))

# ---------------------------
# 2. NumPy basics
# ---------------------------
def numpy_demo():
    print("\n=== NUMPY DEMO ===")
    try:
        import numpy as np
    except Exception:
        print("NumPy not installed; skipping numpy_demo.")
        return

    a = np.array([[1, 2], [3, 4]])
    print("array a:\n", a)
    print("shape:", a.shape, "dtype:", a.dtype)
    print("transpose:\n", a.T)
    print("matrix multiplication:\n", a.dot(a))

    # broadcasting
    v = np.array([1, 10])
    print("broadcast add:", a + v)

    # random numbers and basic stats
    r = np.random.default_rng(seed=0).normal(size=(1000,))
    print("mean ~", r.mean(), "std ~", r.std())

# ---------------------------
# 3. Pandas basics
# ---------------------------
def pandas_demo():
    print("\n=== PANDAS DEMO ===")
    try:
        import pandas as pd
        import numpy as np
    except Exception:
        print("Pandas/NumPy not installed; skipping pandas_demo.")
        return

    # Create a DataFrame
    df = pd.DataFrame({
        "id": range(1, 6),
        "name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
        "age": [25, 30, 35, 28, 22],
        "score": np.random.randint(50, 101, size=5)
    })
    print("DataFrame:\n", df)

    # Basic operations
    print("Describe:\n", df.describe())
    print("Filter age > 25:\n", df[df.age > 25])

    # Add computed column
    df["passed"] = df.score >= 60
    print("With passed column:\n", df)

    # Save & read CSV (temporary)
    csv_path = "demo_users.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved demo DataFrame to {csv_path}")
    df2 = pd.read_csv(csv_path)
    print("Read back:\n", df2)

# ---------------------------
# 4. Matplotlib (plot and save)
# ---------------------------
def matplotlib_demo():
    print("\n=== MATPLOTLIB DEMO ===")
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except Exception:
        print("Matplotlib/NumPy not installed; skipping matplotlib_demo.")
        return

    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x) * np.exp(-x * 0.15)
    plt.figure(figsize=(6, 3.5))
    plt.plot(x, y)
    plt.title("Damped sine wave")
    plt.xlabel("x")
    plt.ylabel("sin(x) * exp(-0.15 x)")
    plt.grid(True)
    fig_path = "demo_plot.png"
    plt.tight_layout()
    plt.savefig(fig_path)
    plt.close()
    print(f"Plot saved to {fig_path}")

# ---------------------------
# 5. SQLite demo
# ---------------------------
def sqlite_demo():
    print("\n=== SQLITE DEMO ===")
    db_path = "demo.db"
    if os.path.exists(db_path):
        os.remove(db_path)  # start fresh for demo
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # Create table
    cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        created_at TEXT
    )
    """)
    # Insert some rows
    users = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    for name, age in users:
        cur.execute("INSERT INTO users (name, age, created_at) VALUES (?, ?, ?)",
                    (name, age, datetime.utcnow().isoformat()))
    conn.commit()

    # Query
    cur.execute("SELECT id, name, age FROM users WHERE age > ?", (26,))
    rows = cur.fetchall()
    print("Users with age>26:", rows)

    # Use pandas to read sql (if available)
    try:
        import pandas as pd
        df = pd.read_sql_query("SELECT * FROM users", conn)
        print("Users DataFrame from SQLite:\n", df)
    except Exception:
        pass

    conn.close()
    print(f"SQLite DB created at {db_path}")

# ---------------------------
# 6. Threading example (I/O-bound simulation)
# ---------------------------
def threading_demo():
    print("\n=== THREADING DEMO ===")
    # Simple function that "does work" (simulated I/O via sleep)
    import time

    def worker(n):
        print(f"Worker {n} starting")
        # simulate I/O wait
        time.sleep(random.uniform(0.3, 0.8))
        result = f"Result-{n}"
        print(f"Worker {n} finished")
        return result

    results = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(worker, i) for i in range(6)]
        for fut in as_completed(futures):
            results.append(fut.result())

    print("Threading results:", results)

# ---------------------------
# 7. asyncio + aiohttp (concurrent HTTP GET)
# ---------------------------
async def async_fetch_demo():
    print("\n=== ASYNCIO + AIOHTTP DEMO ===")
    try:
        import aiohttp
    except Exception:
        print("aiohttp not installed; skipping async_fetch_demo.")
        return

    # We'll fetch small JSON endpoints from a public API (placeholder).
    # NOTE: When running, ensure you have internet access. If offline, these will fail.
    urls = [
        "https://api.github.com",                # GitHub API root
        "https://httpbin.org/get",               # simple GET echo
        "https://api.github.com/events"          # events (could be large)
    ]

    async def fetch(session, url):
        async with session.get(url, timeout=10) as resp:
            text = await resp.text()
            # return first 200 chars to avoid huge prints
            return url, resp.status, text[:200]

    timeout = aiohttp.ClientTimeout(total=15)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [fetch(session, u) for u in urls]
        for coro in asyncio.as_completed(tasks):
            url, status, snippet = await coro
            print(f"[{status}] {url} -> {snippet!r}")

# ---------------------------
# 8. requests (synchronous HTTP)
# ---------------------------
def requests_demo():
    print("\n=== REQUESTS DEMO ===")
    try:
        import requests
    except Exception:
        print("requests not installed; skipping requests_demo.")
        return

    url = "https://httpbin.org/get"
    try:
        r = requests.get(url, timeout=8)
        print("requests status:", r.status_code)
        # print small JSON reply
        try:
            data = r.json()
            print("origin:", data.get("origin"))
        except ValueError:
            print("Non-JSON response")
    except requests.RequestException as e:
        print("HTTP request failed:", e)

# ---------------------------
# 9. Small utilities: regex, json, logging
# ---------------------------
def utilities_demo():
    print("\n=== UTILITIES DEMO ===")
    text = "Contact: alice@example.com or bob.smith@company.co.uk"
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    print("Found emails:", emails)

    obj = {"time": datetime.utcnow().isoformat(), "value": random.random()}
    s = json.dumps(obj)
    print("JSON dump:", s)
    print("Loaded back:", json.loads(s))

# ---------------------------
# 10. Small algorithm examples (search/sort)
# ---------------------------
def algorithms_demo():
    print("\n=== ALGORITHMS DEMO ===")
    def binary_search(arr, x):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    arr = [1, 2, 3, 5, 8, 13, 21]
    print("binary_search 5 ->", binary_search(arr, 5))
    print("bubble_sort [3,1,2] ->", bubble_sort([3, 1, 2]))

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

# ---------------------------
# 11. Example: tiny ETL pipeline combining tools
# ---------------------------
def tiny_etl_demo():
    """
    - Use pandas to construct small dataset
    - Save into SQLite
    - Read back and plot with matplotlib
    """
    print("\n=== TINY ETL DEMO ===")
    try:
        import pandas as pd
        import sqlite3
        import matplotlib.pyplot as plt
    except Exception:
        print("Pandas/SQLite/Matplotlib not available; skipping tiny_etl_demo.")
        return

    # Create sample data
    df = pd.DataFrame({
        "date": pd.date_range(end=pd.Timestamp.today(), periods=10),
        "value": (pd.Series(range(10)) + pd.Series(np.random.randn(10))).cumsum()
    })
    print("ETL DataFrame:\n", df.head())

    # Save to SQLite
    db = "etl_demo.db"
    if os.path.exists(db):
        os.remove(db)
    conn = sqlite3.connect(db)
    df.to_sql("series", conn, index=False)
    print(f"Saved to SQLite DB: {db}")

    # Read back and plot
    df2 = pd.read_sql_query("SELECT * FROM series", conn, parse_dates=["date"])
    conn.close()
    plt.figure()
    plt.plot(df2["date"], df2["value"])
    plt.title("ETL Demo Series")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    out = "etl_demo_plot.png"
    plt.savefig(out)
    plt.close()
    print(f"ETL plot saved to {out}")

# ---------------------------
# 12. Main runner (runs all demos)
# ---------------------------
def main():
    print("Python Master v2 demo — starting")
    core_demo()
    numpy_demo()
    pandas_demo()
    matplotlib_demo()
    sqlite_demo()
    threading_demo()

    # asyncio part: run the coroutine if aiohttp available
    # Use event loop to run async demo; wrap in try to handle environments with no internet
    try:
        asyncio.run(async_fetch_demo())
    except Exception as e:
        print("Async demo failed or skipped:", e)

    requests_demo()
    utilities_demo()
    algorithms_demo()
    tiny_etl_demo()
    print("\nAll done — check generated files (csv/png/db) in the working directory.")

if __name__ == "__main__":
    main()