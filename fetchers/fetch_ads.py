import json,os,glob,csv
def main():
    os.makedirs("data/ads",exist_ok=True)
    files=glob.glob("data/ads/*.csv")
    if not files:
        print("No CSV files found in data/ads/ - drop Google Ads CSV exports there and rerun.")
        return
    rows=[]
    for path in files:
        with open(path,newline="",encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                rows.append({"search_term":row.get("Search term",row.get("keyword","")),"impressions":int(str(row.get("Impr.","0")).replace(",","") or 0),"clicks":int(str(row.get("Clicks","0")).replace(",","") or 0),"cost":float(str(row.get("Cost","0")).replace(",","").replace("$","") or 0)})
    open("data/ads/search_terms.json","w").write(json.dumps(rows,indent=2))
    print(f"  Saved {len(rows)} rows to data/ads/search_terms.json")
    print("Ads done.")