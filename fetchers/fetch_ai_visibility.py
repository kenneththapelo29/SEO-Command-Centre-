import json,os,glob,csv
def main():
    os.makedirs("data/ai-visibility",exist_ok=True)
    files=glob.glob("data/ai-visibility/bing*.csv")
    if not files:
        print("No Bing CSV found. Export from Bing Webmaster Tools and drop in data/ai-visibility/")
        return
    rows=[]
    for path in files:
        with open(path,newline="",encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                rows.append({"page":row.get("Page URL",""),"query":row.get("Grounding Query",""),"citations":int(str(row.get("Citations","0")).replace(",","") or 0)})
    open("data/ai-visibility/bing_copilot.json","w").write(json.dumps(rows,indent=2))
    print(f"  Saved {len(rows)} rows to data/ai-visibility/bing_copilot.json")
    print("AI visibility done.")