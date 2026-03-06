# SEO Command Center

A Claude Code-powered SEO toolkit for GSC, GA4, Google Ads and AI visibility.

## Quick Start

1. Clone: `git clone https://github.com/kenneththapelo29/SEO-Command-Centre-.git`
2. Install: `pip install -r requirements.txt`
3. Add `service-account-key.json` to project root
4. Edit `config.json` with your site details
5. Run: `python run_fetch.py --sources gsc,ga4`

## Setup

### Google Cloud (GSC + GA4)

1. Create a project at https://console.cloud.google.com
2. Enable Search Console API and Google Analytics Data API
3. Create a service account and download the JSON key
4. Add service account email to your GSC and GA4 properties

### Google Ads (optional)

Run `python scripts/setup_auth.py` after getting a developer token from Google Ads API Center.

## Usage

```bash
python run_fetch.py --sources gsc,ga4
python run_fetch.py --sources gsc,ga4,ads,ai
```

Open Claude Code in this directory and ask questions like:

- Which keywords am I paying for that I already rank for organically?
- Which pages have high impressions but low CTR?
- Which pages have high bounce rates but strong GSC positions?

See CLAUDE.md for the full prompt library.

## AI Visibility

Supports Bing Webmaster Tools (free), DataForSEO, SerpApi and direct LLM API calls.

## Security

service-account-key.json and google-ads.yaml are in .gitignore - never commit them.

## License

MIT
