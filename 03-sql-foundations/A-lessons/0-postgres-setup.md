## 🔹 Lesson 0 — Setup PostgreSQL

### What You'll Need

1. **PostgreSQL** — the database server
2. **pgAdmin** or **DBeaver** — a visual tool to write and run SQL queries

### Installation Steps

1. Go to [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
2. Download the version for your operating system (Windows/Mac/Linux)
3. During installation, set a **password** for the default user (`postgres`) — don't forget it!
4. After install, open **pgAdmin** (it comes bundled) or install **DBeaver** separately

### Verify It Works

Open pgAdmin, connect to your server, and run:

```sql
SELECT version();
```

If you see PostgreSQL version info, you're good to go! ✅
