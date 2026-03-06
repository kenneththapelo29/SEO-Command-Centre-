# SEO Command Center — Claude Code Guide

## Data locations

| File | Contents |
|------|----------|
| `data/gsc/queries.json` | GSC queries: clicks, impressions, CTR, position |
| `data/gsc/pages.json` | GSC pages: same metrics by URL |
| `data/ga4/channel_traffic.json` | Sessions, bounce rate by channel |
| `data/ga4/top_pages.json` | Top pages with engagement metrics |
| `data/ads/search_terms.json` | Paid search terms: impressions, clicks, cost |
| `data/ai-visibility/bing_copilot.json` | Bing Copilot citation data |
| `config.json` | Client context: domain, industry, competitors |

## Prompt library

### 1. Paid-organic gap analysis
Read data/gsc/queries.json and data/ads/search_terms.json.
Find keywords where we're paying for ads but already rank positions 1-5 organically.
Also find keywords where paid is the only presence — those are content gaps.
Output a prioritised table for each category.
### 2. CTR opportunity finder
Read data/gsc/queries.json.
Find queries in positions 1-10 with impressions over 500 but CTR below 3%.
These pages need title tag or meta description improvements.
Rank by impression volume.
### 3. Topic cluster analysis
Read data/gsc/queries.json.
Group queries into topic clusters by intent.
Show total impressions, average position, and top 3 queries per cluster.
Which clusters have most potential?
### 4. High-bounce organic pages
Read data/ga4/channel_traffic.json and data/gsc/pages.json.
Find pages with strong GSC positions but high bounce rates in GA4.
Sort by traffic volume times bounce rate.
### 5. Quick wins — page 2 to page 1
Read data/gsc/queries.json.
Find queries with average position between 8-20 and impressions over 500.
These are easiest ranking improvements. Sort by impression volume.
### 6. Full monthly SEO report
Read all JSON files in data/gsc/, data/ga4/, data/ads/, data/ai-visibility/.
Write a report with: Executive Summary, Organic Performance,
Paid vs Organic Overlap, Content Opportunities, AI Visibility,
Recommended Actions. Save to reports/report-YYYY-MM-DD.md
## Tips
- Always verify numbers against source JSON before sharing with clients
- GSC has ~3 day lag, GA4 has ~1 day lag
- AI visibility data is directional — treat as a wind sock not GPS

## Google Forms prompts

### 7. Lead source analysis
Read data/forms/all_leads.json and data/gsc/queries.json.
Which organic keywords are driving the most form submissions?
Cross-reference submission timestamps with GSC click data.
### 8. Cost per lead
Read data/forms/all_leads.json and data/ads/search_terms.json.
Calculate cost per lead from paid vs organic traffic.
Which campaigns are generating leads vs burning budget?
### 9. Lead to traffic ratio
Read data/forms/all_leads.json and data/ga4/channel_traffic.json.
Which traffic channels convert best to form submissions?
Show conversion rate by channel.
### 10. Full funnel report
Read all data sources including data/forms/.
Show the complete funnel: impressions to clicks to sessions to leads.
Where are we losing people? Where should we invest more?
