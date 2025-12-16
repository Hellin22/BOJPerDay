from datetime import datetime, timedelta

utc_now = datetime.utcnow()
kst_now = utc_now + timedelta(hours=9)

print(kst_now.strftime("%Y-%m-%d"))
