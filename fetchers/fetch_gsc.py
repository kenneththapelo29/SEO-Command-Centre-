import json,os
from datetime import datetime,timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
SCOPES=["https://www.googleapis.com/auth/webmasters.readonly"]
def main():
    with open("config.json") as f: c=json.load(f)
    creds=service_account.Credentials.from_service_account_file("service-account-key.json",scopes=SCOPES)
    svc=build("searchconsole","v1",credentials=creds)
    end=datetime.today()-timedelta(days=3)
    start=end-timedelta(days=90)
    sd,ed=start.strftime("%Y-%m-%d"),end.strftime("%Y-%m-%d")
    site=c["gsc_property"]
    print(f"Fetching GSC: {site}")
    for dim,fname in [("query","queries.json"),("page","pages.json")]:
        r=svc.searchanalytics().query(siteUrl=site,body={"startDate":sd,"endDate":ed,"dimensions":[dim],"rowLimit":1000}).execute()
        rows=[{"key":x["keys"][0],"clicks":x.get("clicks",0),"impressions":x.get("impressions",0),"ctr":round(x.get("ctr",0)*100,2),"position":round(x.get("position",0),1)} for x in r.get("rows",[])]
        os.makedirs("data/gsc",exist_ok=True)
        open(f"data/gsc/{fname}","w").write(json.dumps(rows,indent=2))
        print(f"  Saved {len(rows)} rows to data/gsc/{fname}")
    print("GSC done.")