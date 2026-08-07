# -*- coding: utf-8 -*-
"""
Xotira tizimi — AI hamrohning eng muhim qismi.

Uch qatlam:
  1. FAKTLAR   — siz haqingizdagi doimiy ma'lumot (kim, nima, qanday)
  2. VOQEALAR  — nima bo'lgani (savdolar, qarorlar, natijalar)
  3. KONTEKST  — joriy holat (nima ustida ishlayapmiz)
"""
import sqlite3, json, datetime as dt
from pathlib import Path
from typing import Optional, List, Dict

DB = Path(__file__).parent / "memory.db"


class Memory:
    def __init__(self, path: Path = DB):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self._init()

    def _init(self):
        c = self.db.cursor()
        # 1) FAKTLAR — kalit-qiymat, doimiy
        c.execute("""CREATE TABLE IF NOT EXISTS facts (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            updated TEXT NOT NULL
        )""")
        # 2) VOQEALAR — vaqt bo'yicha
        c.execute("""CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            kind TEXT NOT NULL,
            summary TEXT NOT NULL,
            data TEXT,
            tags TEXT
        )""")
        # 3) SUHBAT — oxirgi xabarlar
        c.execute("""CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )""")
        c.execute("CREATE INDEX IF NOT EXISTS ix_ev_ts ON events(ts)")
        c.execute("CREATE INDEX IF NOT EXISTS ix_ev_kind ON events(kind)")
        self.db.commit()

    # ---------------- FAKTLAR ----------------
    def remember(self, key: str, value: str, category: str = "general"):
        self.db.execute(
            "INSERT OR REPLACE INTO facts(key,value,category,updated) VALUES(?,?,?,?)",
            (key, value, category, dt.datetime.now().isoformat(timespec="seconds")))
        self.db.commit()

    def recall(self, key: str) -> Optional[str]:
        r = self.db.execute("SELECT value FROM facts WHERE key=?", (key,)).fetchone()
        return r["value"] if r else None

    def all_facts(self, category: Optional[str] = None) -> Dict[str, str]:
        q = "SELECT key,value FROM facts"
        args = ()
        if category:
            q += " WHERE category=?"
            args = (category,)
        return {r["key"]: r["value"] for r in self.db.execute(q, args)}

    def forget(self, key: str):
        self.db.execute("DELETE FROM facts WHERE key=?", (key,))
        self.db.commit()

    # ---------------- VOQEALAR ----------------
    def log(self, kind: str, summary: str, data: dict = None, tags: List[str] = None):
        self.db.execute(
            "INSERT INTO events(ts,kind,summary,data,tags) VALUES(?,?,?,?,?)",
            (dt.datetime.now().isoformat(timespec="seconds"), kind, summary,
             json.dumps(data or {}, ensure_ascii=False),
             ",".join(tags or [])))
        self.db.commit()

    def history(self, kind: str = None, days: int = 30, limit: int = 100):
        since = (dt.datetime.now() - dt.timedelta(days=days)).isoformat()
        q = "SELECT * FROM events WHERE ts >= ?"
        args = [since]
        if kind:
            q += " AND kind = ?"
            args.append(kind)
        q += " ORDER BY ts DESC LIMIT ?"
        args.append(limit)
        return [dict(r) for r in self.db.execute(q, args)]

    def search(self, text: str, limit: int = 20):
        return [dict(r) for r in self.db.execute(
            "SELECT * FROM events WHERE summary LIKE ? ORDER BY ts DESC LIMIT ?",
            (f"%{text}%", limit))]

    # ---------------- SUHBAT ----------------
    def add_message(self, role: str, content: str):
        self.db.execute("INSERT INTO messages(ts,role,content) VALUES(?,?,?)",
             (dt.datetime.now().isoformat(timespec="seconds"), role, content))
        self.db.commit()

    def recent_messages(self, n: int = 20):
        rows = self.db.execute(
            "SELECT role,content FROM messages ORDER BY id DESC LIMIT ?", (n,)).fetchall()
        return [{"role": r["role"], "content": r["content"]} for r in reversed(rows)]

    # ---------------- KONTEKST ----------------
    def build_context(self) -> str:
        """AI ga beriladigan kontekst — kim bilan gaplashayotganini biladi."""
        parts = []
        facts = self.all_facts()
        if facts:
            parts.append("## Foydalanuvchi haqida\n" +
                "\n".join(f"- {k}: {v}" for k, v in facts.items()))

        trades = self.history("trade", days=30, limit=200)
        if trades:
            wins = sum(1 for t in trades if json.loads(t["data"]).get("r", 0) > 0)
            total_r = sum(json.loads(t["data"]).get("r", 0) for t in trades)
            parts.append(
                f"\n## Oxirgi 30 kun savdolari\n"
                f"- Jami: {len(trades)}\n"
                f"- Yutuq: {wins} ({wins/len(trades)*100:.0f}%)\n"
                f"- Jami R: {total_r:+.1f}\n"
                f"- Expectancy: {total_r/len(trades):+.3f}R")

        recent = self.history(days=7, limit=10)
        if recent:
            parts.append("\n## Oxirgi voqealar\n" +
                "\n".join(f"- [{e['ts'][:16]}] {e['kind']}: {e['summary']}"
                          for e in recent))
        return "\n".join(parts) if parts else "(xotira bo'sh)"

    def stats(self):
        f = self.db.execute("SELECT COUNT(*) c FROM facts").fetchone()["c"]
        e = self.db.execute("SELECT COUNT(*) c FROM events").fetchone()["c"]
        m = self.db.execute("SELECT COUNT(*) c FROM messages").fetchone()["c"]
        return {"faktlar": f, "voqealar": e, "xabarlar": m}


if __name__ == "__main__":
    m = Memory()
    print("=" * 60)
    print("XOTIRA TIZIMI — demo")
    print("=" * 60)

    m.remember("ism", "Polvonnazir", "shaxsiy")
    m.remember("broker", "Exness", "savdo")
    m.remember("strategiya", "Photon MTF + BETA1 + QM/Fibo", "savdo")
    m.remember("risk", "0.5% har savdo, kuniga maks 3 zarar", "savdo")
    m.remember("maqsad", "12 oyda 3 strategiyani statistik tekshirish", "savdo")
    m.remember("akasi", "biologiya/kimyo o'quv markazi (Urganch)", "shaxsiy")

    m.log("trade", "XAUUSD short, faza A, LC-2A",
          {"pair": "XAUUSD", "r": 3.0, "phase": "A", "model": "LC-2A"}, ["savdo"])
    m.log("trade", "XAUUSD long, faza B, sweep",
          {"pair": "XAUUSD", "r": -1.0, "phase": "B", "model": "LC-1"}, ["savdo"])
    m.log("decision", "Gann strategiyasi benchmark sifatida qoldirildi", tags=["reja"])
    m.log("code", "Photon v2 Pine indikatori yozildi", tags=["kod"])

    print("\n" + m.build_context())
    print("\n" + "=" * 60)
    print("Statistika:", m.stats())
    print(f"DB: {DB}")
