import sqlite3

con = sqlite3.connect('GYM.db')
gym = con.cursor()

# 1. بنمسح الجدول القديم خالص ونبني واحد نظيف عشان نبدأ من الصفر
gym.execute("DROP TABLE IF EXISTS members")
gym.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
      status TEXT 
    )
""")

# 2. بنضيف الجهاز التجريبي
gym.execute("INSERT INTO members (name , status) VALUES ('Captain Ali', 'Active')")
# بنضيف جهاز تاني حقيقي عشان نتأكد إن الجدول مش هيبقى فاضي بعد الحذف
gym.execute("INSERT INTO members (name , status) VALUES ('Test User', 'Expired')")

# 3. هنا بقا بنفذ أمر الـ DELETE (بعد ما البيانات انضافت)
gym.execute("DELETE FROM members WHERE name = 'Test User'")

# 4. بنقرأ الجدول عشان نتأكد إن ghg اتمسح والـ Treadmill بس اللي باقي
gym.execute("SELECT  * FROM members")

date_coaches = gym.fetchmany(2)
for row in date_coaches:
    print(row)

con.commit()
con.close()