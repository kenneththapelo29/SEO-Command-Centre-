import argparse, sys, time, importlib
from datetime import datetime
VALID = ["gsc","ga4","ads","ai","forms"]
FETCHERS = {
    "gsc":("fetchers.fetch_gsc","Google Search Console"),
    "ga4":("fetchers.fetch_ga4","Google Analytics 4"),
    "ads":("fetchers.fetch_ads","Google Ads"),
    "ai":("fetchers.fetch_ai_visibility","AI Visibility"),
    "forms":("fetchers.fetch_forms","Google Forms")
}
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sources", default=",".join(VALID))
    args = p.parse_args()
    requested = [s.strip() for s in args.sources.split(",")]
    print(f"SEO Command Center - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    results = {}
    for source in requested:
        mod, label = FETCHERS[source]
        try:
            importlib.import_module(mod).main()
            results[source] = "OK"
        except Exception as e:
            print(f"FAIL {label}: {e}")
            results[source] = "FAIL"
    for s,r in results.items():
        print(f"  {r}  {FETCHERS[s][1]}")
if __name__ == "__main__":
    main()
