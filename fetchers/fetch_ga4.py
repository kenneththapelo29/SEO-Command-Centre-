import json,os
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest,DateRange,Dimension,Metric
def main():
    with open("config.json") as f: c=json.load(f)
    pid=c["ga4_property_id"]
    creds=service_account.Credentials.from_service_account_file("service-account-key.json",scopes=["https://www.googleapis.com/auth/analytics.readonly"])
    client=BetaAnalyticsDataClient(credentials=creds)
    req=RunReportRequest(property=f"properties/{pid}",date_ranges=[DateRange(start_date="90daysAgo",end_date="yesterday")],dimensions=[Dimension(name="sessionDefaultChannelGroup")],metrics=[Metric(name="sessions"),Metric(name="totalUsers"),Metric(name="bounceRate")])
    resp=client.run_report(req)
    rows=[{resp.dimension_headers[i].name:rv.value for i,rv in enumerate(r.dimension_values)}|{resp.metric_headers[i].name:mv.value for i,mv in enumerate(r.metric_values)} for r in resp.rows]
    os.makedirs("data/ga4",exist_ok=True)
    open("data/ga4/channel_traffic.json","w").write(json.dumps(rows,indent=2))
    print(f"  Saved {len(rows)} rows to data/ga4/channel_traffic.json")
    print("GA4 done.")