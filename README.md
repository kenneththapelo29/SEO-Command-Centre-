# SEO Command Center

### Stop switching tabs. Start asking questions.

One setup. Every SEO answer in seconds.

---

## The problem with SEO analysis today

| The old way | With SEO Command Center |
|-------------|------------------------|
| Export CSVs from GSC, GA4, Ads | Run one command |
| Open Excel, VLOOKUP everything | Ask Claude a question |
| Spend 3 hours building analysis | Get your answer |
| Repeat next month | Ask a follow-up |

> *Which keywords am I paying for that I already rank for organically?*
> Answered in 90 seconds instead of an afternoon.

---

## What you can ask

**Find wasted ad spend**

```
Compare GSC rankings against Ads search terms.
Find every keyword where we pay for clicks but already rank positions 1-5 organically.
```

**Find quick ranking wins**

```
Which queries are stuck on page 2 with over 500 impressions?
```

**Find content gaps**

```
Which paid search terms have zero organic presence?
```

**Fix high-bounce pages**

```
Which pages rank well in GSC but have high bounce rates in GA4?
```

**Track AI visibility**

```
Are our pages being cited in Google AI Overviews or Copilot?
```

**Generate client reports**

```
Write a full monthly SEO report. Save to reports/ as markdown.
```

**Connect lead data**

```
Which organic keywords drove the most form submissions this month?
```

---

## Real results

When run for a higher education client:

- **2,742** search terms with wasted ad spend
- **351** opportunities to reduce paid spend where organic was already strong
- **33** organic queries that paid could amplify
- **41** content gaps where paid was the only presence

That analysis took **90 seconds**. The manual equivalent takes **most of an afternoon**.

---

## What it connects

| Source | What you get |
|--------|--------------|
| Google Search Console | Queries, pages, clicks, impressions, CTR, position |
| Google Analytics 4 | Sessions, bounce rates, conversions by channel |
| Google Ads | Search terms, spend, conversions, impression share |
| Google Forms | Lead data - connect traffic to actual enquiries |
| AI Visibility | Citations in ChatGPT, Copilot, Perplexity, AI Overviews |

---

## Setup

### 1. Clone

```bash
git clone https://github.com/kenneththapelo29/SEO-Command-Centre-.git
cd SEO-Command-Centre-
```

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Google Cloud

1. Create a project at https://console.cloud.google.com
2. Enable Search Console API and Google Analytics Data API
3. Create a service account and download the JSON key
4. Save key as `service-account-key.json` in project root
5. Add service account email to your GSC and GA4 properties

### 4. Configure

Edit `config.json` with your site details.

### 5. Fetch and ask

```bash
python run_fetch.py --sources gsc,ga4
```

Open Claude Code in this directory. See `CLAUDE.md` for the full prompt library.

---

## Google Ads (optional)

```bash
python scripts/setup_auth.py
```

Requires a developer token from Google Ads API Center. Approval: 24-48 hours.

---

## AI Visibility

| Source | Cost | Tracks |
|--------|------|--------|
| Bing Webmaster Tools | Free | Copilot citations |
| DataForSEO | ~$0.01/query | Google AI Overviews |
| SerpApi | $75/mo | Full SERP + AI Overviews |
| Direct LLM calls | <$20/mo | ChatGPT, Claude, Perplexity |

---

## Notes

- `service-account-key.json` is in `.gitignore` - never commit it
- Verify Claude outputs against source JSON before sending to clients
- AI citation data is directional - useful for trends, not precise counts
- Complements but does not replace tools like Semrush or Ahrefs

---

**Built to eliminate the spreadsheet grind. Point it at any site. Start asking questions.**
