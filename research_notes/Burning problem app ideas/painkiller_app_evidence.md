# Painkiller iOS apps: evidence on burning problems people pay for (solo and tiny teams, 2024 to 2026)

Research date: 2026-11-13. US App Store focus.

Evidence labels used throughout:
- **[V]** verified or first-party platform data (RevenueCat aggregate data, Apple documentation, App Store listing prices)
- **[SR]** self-reported by the founder, unaudited
- **[EST]** third-party estimate (Sensor Tower, Trend Apps, Apprank). Treat as order of magnitude only
- **[BLOG]** vendor, SEO or marketing blog with no primary data shown

Overall caution for the report writer: I found far fewer verified solo-developer revenue figures in the "burning problem" niches than the brief hoped for. Most named solo successes that publish numbers are in non-urgent categories (habit trackers, photo vaults, widgets). For most of the urgent niches listed in the brief, the only revenue evidence I found is third-party estimates of category incumbents, which are mostly not solo developers. This is stated per section under Gaps.

---

## 1. Which app types show high willingness to pay because the need is urgent and specific?

### Takeaway
The best category-level evidence found (one third-party catalogue, estimates only) ranks trade invoice and estimate makers well above exam prep, personal finance micro-tools and caregiver or medication apps on the share of apps earning at least $1K a month. RevenueCat's first-party data shows Business and Health & Fitness have the highest payer value, but I found no verified solo-developer revenue figure for any of the specific urgent niches in the brief.

### Cited Findings

**Category-level share of apps earning money [EST, Trend Apps catalogue of 61,814 apps that reached a US top chart, as of 2026-10-12; revenue "rounded into bands"; "earning" means $1K+ a month; median is among earners only, so it is survivorship-skewed by construction]**
- Invoice and estimate makers for trades: 156 apps, 39% earning $1K+/mo, median earner about $60K/mo, 43 "small apps earning" (over $1K/mo on 10,000 or fewer monthly downloads); iOS 31% earning vs Android 53%. Examples named: Joist, Billdu, Invoice2go, HoneyBook (none are solo developers) — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- Exam prep for one licence or certification: 239 apps, 18% earning, median earner about $20K/mo, 30 small apps earning. Examples named: Pocket Prep EMS, Sporty's Pilot Training, MedicTests (established companies, not solo) — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- Personal finance micro-tools (includes mileage trackers such as Everlance): 743 apps, 19% earning, median earner about $20K/mo, 90 small apps earning; iOS 14% earning vs Android 30% — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- AI note takers and transcription: 130 apps, 40% earning, median earner about $100K/mo — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- Collectible and nature identifiers: 177 apps, 54% earning, median earner about $40K/mo — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- Faith apps (Bible, prayer, devotionals): 748 apps, 19% earning, median earner about $20K/mo. Relevant because the owner rejected a faith-companion app: by this data faith is roughly level with exam prep and personal finance, and half the rate of trade invoicing — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- Caregiver and medication coordination: 62 apps, only 11.3% earning; the source dropped it from its recommended list. Pet health: 14% earning. Perimenopause tracker (5 apps) and postpartum recovery coach (17 apps) had too few apps to judge — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)
- The same source's "small apps earning" metric (over $1K/mo with 10,000 or fewer monthly downloads) is its proxy for whether a small newcomer can earn; it is the closest thing found to a high-intent, low-volume signal — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/)

**First-party payer value by category [V, RevenueCat State of Subscription Apps 2025, web preview]**
- Median revenue per install at day 60 is $0.31 overall; Health & Fitness median $0.63 (P90 $4.19); Education median $0.40 (P90 $3.13) — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)
- Day-14 revenue per install medians: Health & Fitness $0.44, Business $0.29, Education $0.27, Gaming $0.08 — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)
- One-month realized LTV per payer: Health & Fitness median $16.44; Business median $14.82 (P90 $52.41). Business and Health & Fitness median year-1 LTV per payer both exceed $25 — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)
- Download-to-paid P90: Health & Fitness 12.1%, Business 10.1% (category medians not in the preview) — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)
- Refund rates: Education 4.86%, Health & Fitness 4.71%, Business and Gaming 2.67 to 2.88% — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)

**Trades and field work (estimates, invoices)**
- Incumbent prices quoted by one gap-analysis site (pricing table not sourced on the page): Invoice Simple $9/mo; Joist $10 (5 docs/mo), $16, $32; Jobber $39 Core; Tradify $47 per user; Housecall Pro $59 base — [MicroGaps](https://www.microgaps.com/gaps/solo-contractor-estimate-invoice-app) [BLOG]
- Complaints it cites: Joist outages lasting days (Capterra, June 2025), no scheduling or e-signature; Invoice Simple "continuous and significant price increases" (Trustpilot, 2025); Jobber "overkill" for solo operators — [MicroGaps](https://www.microgaps.com/gaps/solo-contractor-estimate-invoice-app) [BLOG]
- Its projection of $6K MRR (about 200 customers) to $44K MRR (about 1,500 customers) at $29/mo is a hypothetical model with no pilot, survey or pre-order data — [MicroGaps](https://www.microgaps.com/gaps/solo-contractor-estimate-invoice-app) [BLOG]
- A low-end competitor already exists: SoloTradeKit sells a field service app for solo tradespeople at $12/mo — [SoloTradeKit](https://www.solotradekit.com/)

**Scanning, PDF and document utilities [EST]**
- Category leaders are large and not indie: iScanner about $4M last month on 400K downloads; CamScanner about $6M on 2M downloads; Tiny Scanner about $500K on 20K downloads — [Sensor Tower iScanner](https://app.sensortower.com/overview/1040093707?country=US), [Sensor Tower CamScanner](https://app.sensortower.com/overview/388627783), [Sensor Tower Tiny Scanner](https://sensortower.com/ios/us/appxy/app/scanner-app-scan-pdf-document/595563753)
- TapScanner about $500K/mo on 100K downloads (Aug 2026) — [Apprank](https://apprank.io/pdf-scanner-app-tapscanner-4905)
- TurboScan Pro (Piksoft Inc., a $14.99 paid-up-front app) estimated at about $10K/mo, a small-developer data point with a one-time price — [Trend Apps](https://trendapps.dev/app/ios/342548956/)
- Tiny Scanner's ratio (about $500K on about 20K downloads) implies very high revenue per download, consistent with an aggressive subscription on high-intent search traffic; this is my reading of the estimate, not a source claim — [Sensor Tower Tiny Scanner](https://sensortower.com/ios/us/appxy/app/scanner-app-scan-pdf-document/595563753)

**Health conditions with daily management (pricing only; no revenue found)**
- Migraine tracker App Store listings show $2.99/mo or $24.99/yr on one app and $5.99/mo or $59.99/yr on Migraine Tracker: Pressure Pal — [App Store listing 1](https://apps.apple.com/us/app/migraine-tracker-headache/id6757488751), [Pressure Pal](https://apps.apple.com/us/app/migraine-and-headache-tracker/id6463206739) [V for price]
- Bearable (small team, founder has chronic migraines) says an optional subscription is its only revenue stream, $34.99/yr, often discounted — [Bearable](https://bearable.app/migraine-tracker-app/) [V for price]
- A user review cited in search results says Migraine Buddy is too costly at nearly $20/mo, a sign of price resistance among chronic-condition users — [Migraine Buddy listing](https://apps.apple.com/ca/app/migraine-buddy/id975074413)
- Several migraine tracker listings carry App Store IDs in the 67xxxxxxxx range (new 2025 to 2026 entrants), indicating the niche is being crowded by new small apps — [MigrAid](https://apps.apple.com/us/app/migraid-migraine-tracker/id6757091931), [HeadAlly](https://apps.apple.com/us/app/-/id6745738746)

**Exam and test prep**
- Writing9, a solo-built IELTS writing prep product, is reported at about $12K/mo. This is a secondhand summary of a founder claim, and the product is primarily web, not a native iOS app — [Goodreads author blog mirror](https://www.goodreads.com/author_blog_posts/25971945-solo-founder-earning-12k-month-from-exam-prep-assistant?tab=book) [SR, secondhand]
- A study app listed for sale shows 88.3% of traffic from App Store search but zero revenue at snapshot: search traffic alone did not produce income — [TrustMRR listing](https://trustmrr.com/startup/education-app-with-strong-aso-ready-for-social-media-growth?metric=mrr) [SR]

### Inferences
- On the one cross-niche dataset found, "the user makes money with it" (trade invoicing, 39% earning) beats "the user must pass or comply" (exam prep 18%, personal finance tools 19%) and clearly beats "the user is worried about someone" (caregiver and medication 11%). That ordering matches the general rule that tools tied to the buyer's income convert best.
- Android out-earns iOS on share-earning in trade invoicing (53% vs 31%) and personal finance tools (30% vs 14%). For a native SwiftUI-only developer this is a real constraint in trades: a meaningful share of US tradespeople are on Android.
- Health-condition trackers show low price points ($25 to $60 a year) and visible price resistance. With no ad budget and a crowded search page, the payer value shown by RevenueCat for Health & Fitness is probably driven by fitness and diet apps, not condition trackers. I could not confirm this split.
- Scanner and PDF utilities are proven money but the top of search is owned by companies earning millions a month who buy Apple Search Ads. The surviving small-developer pattern (TurboScan) predates the subscription era.

### Gaps
- No revenue figures (verified, self-reported or estimated) found for solo-built apps in: mileage logs, tax receipt tools, landlord or tenant documentation, HOA, small-claims evidence, blood pressure, glucose, medication, post-surgery, pregnancy, elder caregiving, sleep training, custody or co-parenting logs, debt or bill negotiation, or high-stakes language help. Searches returned listings and opinion pieces only.
- No ratings counts were retrieved for individual apps. The App Store pages surfaced in search did not return counts in the summaries, and I did not query the iTunes Search API. The report writer should not cite ratings counts from these notes.
- RevenueCat's per-category medians for price, conversion and retention are in the full 263-page PDF, which I could not access.
- Trend Apps methodology page was not read; its estimates are unaudited and limited to apps that reached a top chart, which excludes most failures.
- Could not determine team size for TurboScan (Piksoft), Tiny Scanner or TapScanner.

---

## 2. Documented solo-developer successes 2024 to 2026 in "boring" high-intent niches

### Takeaway
The documented solo wins that run on App Store search are real but mostly in utility categories rather than acute-pain niches, and all figures are self-reported. The base rate from RevenueCat is that 17.3% of new apps reach $1K MRR within two years and 4.6% reach $10K.

### Cited Findings
- **Vaultaire** (private photo and video vault, end-to-end encrypted). Solo founder Rasty Turek, no prior iOS experience, built with AI assistants writing the Swift/SwiftUI in about three weeks. Month one $66; about five or six months later roughly $41,000 in a single month (the article is internally inconsistent on five vs six). Subscription plus lifetime purchase; prices not given. Channel: App Store search via descriptive title, subtitle and keyword field; no paid ads or TikTok. The article itself calls the figures "founder-reported and not independently audited" and attributes them to a Starter Story interview — [Stork.ai](https://www.stork.ai/blog/41k-from-a-boring-appwithout-ads) [SR]
- **HabitKit** (habit tracker, Sebastian Röhl, solo). Reported at $15K MRR in a Starter Story interview, built through build-in-public, ASO and a low-budget Apple Search Ads campaign; operating costs about $200 to $300/mo — [Starter Story mirror](https://rosetta.to/u/starterstory/how-i-built-it-15k-month-mobile-app) [SR]. A later secondary write-up puts it at about $28K MRR and about $602K 2025 revenue with distribution "almost 100% App Store Optimization" — [Medium, Tamim](https://tamimbuilds.medium.com/8-solo-founders-who-quietly-hit-20k-62k-mrr-in-the-last-6-months-5032e610badc) [SR, secondhand]. Not a burning-problem app; included as the best-documented ASO-only solo case. His own year review is at [Substack](https://sebastianroehl.substack.com/p/2024-my-indie-app-business-year-in) (not read in full).
- **Max's portfolio** (full-time iOS developer, side project). 28 apps in 8 months earning $10K/mo per Starter Story; later 30+ apps at about $22K/mo per Indie Hackers. Main channel is ASO; learning ASO lifted impressions, downloads and revenue by about 50% — [Starter Story mirror](https://rosetta.to/u/starterstory/i-make-10k-month-from-28-apps), [Indie Hackers](https://www.indiehackers.com/post/tech/from-failed-app-to-30-app-portfolio-making-22k-mo-in-less-than-a-year-myy3U7K9evxGOVOHti8s) [SR]. A secondary analysis notes this averages about $800 per app per month — [BuildMVPFast](https://www.buildmvpfast.com/blog/portfolio-app-strategy-multiple-apps-revenue-solo-founder-2026) [BLOG]
- **Portfolio to $60K/mo after Apple froze his developer account** — headline only; the Indie Hackers page returned HTTP 403, so details are unverified — [Indie Hackers](https://www.indiehackers.com/post/tech/building-an-app-portfolio-to-60k-mo-after-apple-froze-his-developer-account-LD7oNYzKSmWucRfKV1AO) [SR, unread]
- **Platform-risk counterexample**: a developer with ten iOS apps reports a best month of $9K that later fell to about $1.5K — [Indie Hackers](https://www.indiehackers.com/post/jChJ6O2CpPMaLCa4NypB) [SR]
- **Slow-ramp counterexample**: Habit Pixel took eight months of consistent work to reach $1K MRR — [Indie Hackers](https://www.indiehackers.com/post/from-0-to-1k-mrr-in-8-months-bootstrapping-habit-pixel-as-a-solo-dev-53d8687d15) [SR]
- **Failure-mode example**: an Anki-replacement language app reports 1,000 users and $21 MRR — [Indie Hackers](https://www.indiehackers.com/post/i-built-a-language-learning-app-to-replace-anki-1-000-users-21-mrr-3a730ebad2) [SR]
- Other Starter Story solo or tiny-team mobile figures surfaced, none in urgent niches: Momego $30K MRR; MonAI expense tracker $300 to $35K/mo; a three-app iOS portfolio at about $10.4K MRR combined — [Starter Story mirror index](https://rosetta.to/u/starterstory/how-i-built-a-30k-month-mobile-app), [MonAI](https://rosetta.to/u/starterstory/this-app-makes-35k-month-with-one-influencer), [3 apps](https://rosetta.to/u/starterstory/i-make-120k-year-from-3-mobile-apps) [SR]. MonAI's growth was influencer-led, not search.

**Base rates [V, RevenueCat SOSA 2026 as summarised by SaaStr]**
- 17.3% of new apps reach $1K MRR within two years; 4.6% reach $10K MRR — [SaaStr](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/)
- New subscription app launches rose from about 2,000 a month (Jan 2022) to 14,700 a month (Jan 2026). Apps launched before 2020 hold 69% of subscription revenue; apps launched in 2025 or later hold 3% — [SaaStr](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/)
- Median time to $1K MRR: 32 days for gaming, 113 days for business apps — [SaaStr](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/)
- From the 2025 edition: top 5% of newly launched apps earn $8,880 after the first year; bottom 25% earn no more than $19 — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)

### Inferences
- Survivorship bias is heavy here. Every named case comes from Starter Story, Indie Hackers or founder posts, which select for winners and for founders who gain from publicity. The RevenueCat base rates (roughly 1 in 6 reach $1K MRR in two years, among apps serious enough to integrate RevenueCat) are the honest denominator, and even they exclude apps that never added a subscription SDK.
- The two cleanest "App Store search only" solo cases (Vaultaire, HabitKit) are in categories with very large search volume and are not painkillers in the strict sense. Vaultaire is closest: privacy of sensitive photos is an acute, specific, private need that people search for by function ("photo vault") and will not ask friends about. That profile (embarrassing or private, searched by function, no social sharing needed) is worth noting as a pattern.
- Vaultaire is also direct evidence that an AI-agent-built native SwiftUI app with no hand-written code can reach meaningful revenue on search alone, which matches the owner's setup. It is one self-reported case.
- The portfolio approach (Max) is a hedge against not knowing which keyword will hit, at about $800 per app average. With an AI coding agent, build cost per app is low, so this strategy fits, but Apple guideline 4.3 (spam, duplicate apps) is a known risk for portfolios; I did not source that risk here.

### Gaps
- I found no documented solo success from 2024 to 2026 that publishes revenue AND target keywords in a strictly urgent niche (exam prep, trades, compliance, health condition, custody). The brief's hoped-for evidence largely does not exist in the public sources I reached, or is behind paywalls (Indie Hackers IH+, Starter Story).
- Specific App Store keywords were not disclosed in any case found.
- Sub Club podcast and Superwall blog were not searched directly; Superwall surfaced titles only ("How I make $42k/mo passively with simple no-code apps", "$0 to $100K MRR") which I did not read.
- A Reddit r/AppBusiness post about 65 small utility apps earning about $4,200/mo combined appeared in a search summary but I could not tie it to a URL, so it is unverified.
- A roundup claiming one developer's first year brought $1,464 across eight apps was at a URL that now returns HTTP 410; unverified.

---

## 3. B2B or prosumer micro-apps versus consumer apps for solo developers

### Takeaway
Evidence is thin and mostly indirect: RevenueCat shows Business apps have payer value comparable to Health & Fitness with lower refunds but a slower ramp (113 days median to $1K MRR), and higher price points produce both better trial conversion and about 6x the payer LTV. I found no solo-specific B2B versus consumer comparison.

### Cited Findings
- Business category: one-month realized LTV per payer median $14.82, P90 $52.41; year-1 LTV per payer above $25; download-to-paid P90 10.1%; refund rate about 2.7 to 2.9% vs 4.7 to 4.9% for Health & Fitness and Education — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]
- Business apps take a median 113 days to reach $1K MRR vs 32 days for gaming — [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/) [V]
- Price tolerance: high-priced apps convert download-to-trial at 8.9 to 9.8% vs 4.3 to 4.4% for low-priced; realized LTV per payer after year 1 is $62.19 for high-priced vs $10.69 for low-priced — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025), [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/) [V]
- Hard paywall vs freemium: median download-to-paid 10.7% vs 2.1%; day-60 revenue per install $3.09 vs $0.38 (2026 edition). 2025 edition: 12.11% vs 2.18%. Refunds are higher on hard paywalls (5.8% vs 3.4%) — [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/), [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]
- Retention by plan: year-1 retention 44.1% yearly, 17.0% monthly, 3.4% weekly. Nearly 30% of annual subscriptions are cancelled in the first month. First annual renewal 61.7% — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]
- Median consumer subscription annual price rose from $31.60 to $34.80; common bands $4.99 to $6.99 weekly, $7.99 to $9.99 monthly, $29.99 to $39.99 annual — [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/) [V]
- North America: day-60 revenue per install $0.55, download-to-paid 2.8%, annual price $39.99 — [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/) [V]
- Trade-tool price anchors are 3 to 15 times consumer norms: Joist $10 to $32/mo, Jobber $39+, Tradify $47 per user, Housecall Pro $59+ (unsourced table) — [MicroGaps](https://www.microgaps.com/gaps/solo-contractor-estimate-invoice-app) [BLOG]
- Trade invoicing has the highest share of earning apps among "boring" niches in the Trend Apps catalogue (39% vs 18 to 19% for exam prep, finance tools and faith) — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/) [EST]

### Inferences
- A prosumer tool at $10 to $30 a month sits in RevenueCat's "high-priced" band, where trial conversion is about double and payer LTV about six times the low-priced band. Fewer customers are needed: at $20/mo net of Apple's 15% small-business commission, about 60 payers equals $1K MRR.
- The trade-off is speed: business apps ramp slowly (113-day median to $1K MRR among those that get there), and B2B users expect support, data export and reliability (Joist's outage complaints are the opening, but also the bar).
- Low refund rates in Business suggest buyers know what they are buying, which is consistent with high-intent search.

### Gaps
- No source compared churn for solo-built B2B or prosumer iOS apps against consumer apps. RevenueCat's retention by category is chart-only in the preview.
- A claim that "median monthly churn for indie apps is 12 to 25%" appeared in an SEO guide whose URL now returns HTTP 410; unverified, do not cite.
- A dated survey claim (enterprise developers twice as likely to reach $10K/mo) surfaced via a Fox News syndication with no date or method; too weak to use.
- No data found on Apple Business Manager or volume purchase use by micro-apps.

---

## 4. Methods to validate urgency cheaply without a waitlist, and thresholds practitioners use

### Takeaway
Practitioner thresholds converge on targeting keywords with Apple popularity roughly 20 to 55 and tool difficulty under about 35 to 40, then checking the top 10 results for a "free giant" and reading 1 to 3 star reviews for repeated complaints. All thresholds come from tool vendors and bloggers, and keyword data quality was disrupted between October 2025 and October 2026.

### Cited Findings

**Keyword popularity and difficulty**
- Apple's Search Popularity runs 5 to 100; a score of 5 is treated as no detectable volume, and many niche terms are floored at 5 — [Sonar](https://trysonar.app/blog/keyword-difficulty-explained) [BLOG, vendor]
- Vendor guides put the indie "sweet spot" at popularity about 35 to 55 with difficulty 15 to 35; another says aim for popularity 20 to 55 because above 55 you compete with apps with huge install bases; another ranks by ratio, arguing popularity 25 with difficulty 15 beats popularity 70 with difficulty 90 — [Sonar keyword research guide](https://trysonar.app/blog/keyword-research-guide), [Sonar indie guide](https://trysonar.app/blog/indie-developer-aso-guide), [AppSprint](https://appsprint.app/aso/blog/app-store-keyword-research) [BLOG; the search summary did not attribute each number to a specific page, so verify before quoting]
- Sonar's difficulty bands: 0 to 30 low (few top apps have the term in the title, incumbents have modest review counts, mostly long-tail); 31 to 60 moderate ("winnable when the strongest of the top few apps is close to your size"); 61 to 80 hard; 81 to 100 very hard — [Sonar](https://trysonar.app/blog/keyword-difficulty-explained)
- Across 87 category head terms on the US App Store (refreshed Sept 2026), none scored 30 or below and the median difficulty was 69; Health & Fitness median 74, Photo & Video 70, Finance 59. Easiest head terms were things like "kanban board" 33, "unit converter" 36, "tip calculator" 37 — [Sonar](https://trysonar.app/blog/keyword-difficulty-explained)
- "Gap" = popularity minus difficulty; large positive gap is the target zone, no numeric cutoff given. A keyword "out of reach for a brand-new app can be winnable for one with a few thousand ratings" — [Sonar](https://trysonar.app/blog/keyword-difficulty-explained)
- Scores differ across tools; compare keywords only within one tool — [Sonar](https://trysonar.app/blog/keyword-difficulty-explained)
- Data-quality warning: after an Apple change, one source says Astro's keyword popularity data was frozen from before October 2025 and Astro restored a backup from early October; Sonar says that from 2026-10-22 Apple reports real values down to about 20 and it shows a capped proxy below that. Sources do not fully agree; check current tool status before relying on any popularity number — [Indie App Devs #4](https://indieappdevs.substack.com/p/indie-app-devs-4), [Sonar](https://trysonar.app/blog/keyword-difficulty-explained)
- Tool pricing in one roundup: Astro about $9/mo (Mac-only, iOS-only), Appfigures from $9.99/mo (web, both stores) — [Anything.com ASO tools roundup](https://www.anything.com/blog/aso-tools-indie-app-builders) [BLOG]

**Counting weak incumbents with free data**
- Apple's iTunes Search API (free, no key; `https://itunes.apple.com/search?term=...&country=us&entity=software&limit=25`) returns `userRatingCount`, `averageUserRating`, `price` and `currentVersionReleaseDate` (days since last update). Sort by ratings count and inspect the top 10. "Ratings count is the best public demand signal on iOS" — [DEV, jack_fruit](https://dev.to/jack_fruit/how-to-check-an-app-idea-against-real-app-store-data-before-you-build-it-4cp0) [BLOG]
- That author scores Demand, Competition (high = easy) and Revenue 0 to 10 each; build at average 7.5 or more, skip below 6. Kill checks: a "giant" (hundreds of thousands of ratings at 4.9) and especially a free giant, because "a paid plan competes with $0". Consumer apps "rarely score above 5 on Competition". Worked example: ADHD habit tracker, leader with 768K ratings at 4.95, verdict skip — [DEV, jack_fruit](https://dev.to/jack_fruit/how-to-check-an-app-idea-against-real-app-store-data-before-you-build-it-4cp0) [BLOG; the author sells an automation tool]
- 61% of App Store apps have zero ratings, so most listed "competitors" are inactive — [Preuve.ai](https://preuve.ai/blog/is-my-app-idea-already-taken) [BLOG; figure's origin not checked]
- Revenue-per-download screen: look for apps earning over $1K/mo on 10,000 or fewer monthly downloads as evidence a small entrant can earn — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/) [EST]

**Review and complaint mining**
- Read competitors' 1 to 3 star reviews and look for complaints that repeat across apps: "the numbers show whether to enter; the reviews show how" — [DEV, jack_fruit](https://dev.to/jack_fruit/how-to-check-an-app-idea-against-real-app-store-data-before-you-build-it-4cp0)
- Practitioners disagree on which stars matter: one says 1-star reviews are mostly transient bugs and 2 to 3 star reviews hold product gaps; another reads 1-star for raw frustration and 3-star for fixable gaps — [BigIdeasDB](https://bigideasdb.com/find-saas-ideas-from-negative-reviews-g2-app-store), [GetAppNiche](https://getappniche.com/guides/validate-app-idea) [BLOG; attribution between the two is from a search summary]
- Example of the method applied to trades: Capterra, Trustpilot and Reddit complaints about Joist outages and Invoice Simple price increases used as the wedge — [MicroGaps](https://www.microgaps.com/gaps/solo-contractor-estimate-invoice-app)

**Conversion sanity checks to apply to any demand estimate [V]**
- Median trial start rate is 6.2% of downloads (P90 20.3%); 82% of trial starts happen on install day; North America download-to-paid 2.8% — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025), [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/)

### Inferences
Checklist of burning-problem signals, assembled from the findings above. Items marked (inferred) are my synthesis, not a sourced practitioner rule.
1. People search for it by function, not by brand, and the keyword has Apple popularity roughly 20 to 55 with tool difficulty under about 35 to 40. Head terms are out of reach (median difficulty 69).
2. The top 10 search results contain no free giant (hundreds of thousands of ratings, 4.9 stars, $0).
3. At least some top-10 apps charge, and charge above consumer norms (over $40/yr or $10+/mo), showing existing spend.
4. Leaders have many ratings but stale `currentVersionReleaseDate` and repeated 1 to 3 star complaints about the same thing (price hikes, outages, missing feature).
5. Third-party estimates show small apps earning over $1K/mo on under 10K monthly downloads in the niche.
6. The user already pays a human or a pricier tool for the same job (trade software at $39 to $59/mo is the anchor for a $15 to $29 app). (inferred)
7. There is a deadline or a consequence: an exam date, a tax filing, a court date, an unpaid invoice. (inferred)
8. The need recurs at least monthly for the same person, or the price is charged up front for a one-time need. (inferred, see section 6)
9. The payer is the user and has income tied to the task. (inferred, see section 6)
10. A simple arithmetic check passes: estimated monthly downloads from target keywords x 2 to 3% download-to-paid (or about 10% with a hard paywall) x price clears the income target. (inferred from RevenueCat medians)

- The October 2025 to October 2026 disruption in keyword popularity data means any tool reading should be cross-checked against the free ratings-count method, which does not depend on Apple's popularity feed.

### Gaps
- No practitioner threshold found for Apple Search Ads keyword volume as a validation tool, and no public guidance on running a small Search Ads test as a demand probe. The owner has no ad budget, so this matters less.
- No practitioner thresholds found for Google Trends or for Reddit complaint counts (for example, "N threads per month").
- No numeric rule found for "weak incumbent" in terms of ratings count plus months since last update; the DEV post pulls the fields but gives no cutoff.
- Appfigures and AppTweak primary blog posts on validation were not reached; the thresholds above are mainly from Sonar, a smaller vendor with a product to sell.
- I could not verify the exact nature of the Apple change behind the Astro data freeze.

---

## 5. Categories where AI capability newly unlocked in 2025 to 2026 makes a painkiller feasible for a solo developer, and App Store rules that constrain them

### Takeaway
AI-heavy categories show the highest share of earning apps in the one dataset found (identifiers 54%, AI note takers 40%) and AI apps earn 41% more per payer but churn 30% faster. Apple's on-device model is free to call but capped at 4,096 tokens per session, and since November 2025 any personal data sent to a third-party AI needs explicit, separate consent.

### Cited Findings
- AI apps generate 41% more revenue per payer than non-AI apps and churn 30% faster — [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/) [V]; AI apps' day-60 revenue per install is above $0.63, matched only by Health & Fitness (2025 edition) — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]
- Vision-based identifiers (coins, cards, birds): 177 apps, 54% earning $1K+/mo. AI note takers and transcription: 130 apps, 40% earning, median earner about $100K/mo, with Android far ahead of iOS on share earning (63% vs 33%). Plant identification: 204 apps, 25% earning — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/) [EST]
- Apple's Foundation Models framework gives apps the on-device model behind Apple Intelligence; Apple's health and fitness developer page explicitly lists foundation models among on-device options for processing health data — [Apple Developer, HealthKit](https://developer.apple.com/healthkit) [V]
- The on-device model has a context window of 4,096 tokens per session, shared between input and output; exceeding it throws `exceededContextWindowSize` rather than truncating, and handling is the developer's job. Apple suggests splitting work across sessions — [Apple TN3193](https://developer.apple.com/tutorials/data/documentation/technotes/tn3193-managing-the-on-device-foundation-model-s-context-window.md), [Apple docs: managing the context window](https://developer.apple.com/documentation/foundationmodels/managing-the-context-window.md), [Apple forum](https://developer.apple.com/forums/thread/790736) [V]
- A consultant reports Foundation Models features that work in demos break in shipped apps because real data overflows the window and older phones are not eligible — [Drobinin](https://drobinin.com/consulting/foundation-models-apple-intelligence/putting-apple-foundation-models-in-a-real-app/) [BLOG]
- Device requirement of A17 Pro or M1 and later is stated in one blog comparison table only — [DEV, jovan_chan](https://dev.to/jovan_chan_9500711396d4e6/apple-foundation-models-for-developers-in-2026-on-device-swift-ai-xcode-263-agentic-coding-and-1gpa) [BLOG, unverified against Apple]
- Guideline 5.1.2(i), updated November 2025 (several secondary sources say 2025-11-13): apps must clearly disclose where personal data is shared with third parties, "including with third-party AI", and obtain explicit permission first — [Apple Developer News](https://developer.apple.com/news/?id=ey6d8onl) [V]
- Secondary guidance on how review applies it: name the model provider, ask before the first transmission, keep it separate from ATT and other permissions, provide a way to withdraw consent, and make the App Privacy label match — [DEV, arshtechpro](https://dev.to/arshtechpro/apples-guideline-512i-the-ai-data-sharing-rule-that-will-impact-every-ios-developer-1b0p), [ptkd](https://ptkd.com/journal/rejection-guideline-5-1-2-ai-data-sharing) [BLOG]
- Guideline 1.4.1: medical apps that could provide inaccurate data or be used for diagnosing or treating patients may get greater scrutiny; a developer forum thread shows a wellness-only app still flagged as medical and asked about regulatory clearance — [Apple forum thread 807508](https://developer.apple.com/forums/thread/807508) [V for the incident]; guideline wording via [2020 change list gist](https://gist.github.com/bjtitus/f7d8ef2fb7f7f5fba74a111b7f913e42) (dated 2020, check live text)
- Guideline 5.1.3: health, fitness and medical data may not be used or disclosed to third parties for advertising or data mining — [ConductAtlas copy](https://conductatlas.com/platform/apple/apple-app-store-review-guidelines/health-data-use-and-sharing-restrictions/) (secondary copy); Apple says health apps must comply with 5.1.3 and that from spring 2026 Medical and Health & Fitness apps can indicate regulatory status in certain regions — [Apple Developer, HealthKit](https://developer.apple.com/healthkit) [V]

### Inferences
- Candidate "newly feasible" painkillers for a solo SwiftUI developer, based on what the capabilities allow (this list is my inference, not sourced demand evidence): photographing a document, invoice, receipt or form and extracting structured fields on device (Vision text recognition plus the on-device model for short extraction); voice-to-estimate or voice-to-inspection-note for tradespeople with dirty hands; turning a photo of a bill, lease or notice into a plain-language summary and a deadline; logging a symptom or incident by voice with automatic timestamps for a doctor or court.
- The 4,096-token cap means the on-device model suits short extraction, classification and rewriting of one page at a time, not long documents such as a full lease or medical record. Long-document features need a cloud model, which triggers 5.1.2(i) consent and adds per-use cost that a weekly or monthly subscription must cover.
- On-device processing sidesteps the third-party AI consent flow and has zero marginal cost, which fits a no-budget solo developer, but only recent devices qualify, shrinking the reachable market (notably for tradespeople on older phones).
- AI apps' faster churn (30%) suggests AI novelty alone does not make a painkiller; the durable examples in the Trend Apps list (identifiers, note takers) solve a repeatable job.

### Gaps
- No source ties specific 2025 to 2026 AI capabilities to named solo-developer painkiller successes in the urgent niches; the link is inferred.
- Apple's official supported-device list for Foundation Models was not retrieved.
- I did not read the live text of App Review Guidelines 1.4.1, 5.1.1(ix) (regulated fields such as banking, healthcare, legal requiring a legal entity) or 3.1.x for services; the report writer should treat regulated-field specifics as unverified.
- The claim that on-device inference is exempt from 5.1.2(i) disclosure appeared without a clear origin; it follows logically (no third party receives data) but is not confirmed by Apple in what I read.
- WWDC 2026 changes to Foundation Models (a session index surfaced) were not reviewed; the 4,096 limit may have changed on newer OS versions, though an Apple forum reply said the limit is fixed.

---

## 6. Common traps: urgent but rare, urgent but no money, and regulated areas

### Takeaway
The data supports three concrete cautions: subscriptions for one-off needs leak out fast (weekly plans retain 3.4% at one year and nearly 30% of annual plans cancel in month one), niches where the worried person is not earning from the task show low earning rates (caregiver and medication apps 11.3%), and health apps draw heightened review and higher refunds. Direct evidence on "urgent but broke" users is missing.

### Cited Findings
- Year-1 retention: weekly 3.4%, monthly 17.0%, yearly 44.1%. Under 5% of weekly payers reach month six (Thomas Petit). Nearly 30% of annual subscriptions are cancelled in the first month — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]
- 55% of 3-day-trial cancellations happen on day 0; 50% of paid conversions also happen on day 0 — [SaaStr on SOSA 2026](https://www.saastr.com/the-top-10-learnings-from-revenuecats-state-of-subscription-apps/) [V]
- Over 35% of apps mix subscriptions with consumables or lifetime purchases — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]. TurboScan Pro earns an estimated $10K/mo as a $14.99 one-time purchase — [Trend Apps](https://trendapps.dev/app/ios/342548956/) [EST]. Vaultaire offers a lifetime purchase alongside subscription — [Stork.ai](https://www.stork.ai/blog/41k-from-a-boring-appwithout-ads) [SR]
- Caregiver and medication coordination: 11.3% of 62 apps earn $1K+/mo, the weakest measured niche in the Trend Apps list; pet health 14% — [Trend Apps](https://trendapps.dev/blog/trends/profitable-mobile-app-ideas-2026/) [EST]
- Chronic-condition price resistance: Bearable at $34.99/yr "often discounted by up to 76%"; a Migraine Insight listing gives tracking and doctor reports away free; a reviewer calls Migraine Buddy too costly at nearly $20/mo — [Bearable](https://bearable.app/migraine-tracker-app/), [Migraine Insight on Google Play](https://play.google.com/store/apps/details?id=com.shinynewapp.migraineinsight2&hl=en_US), [Migraine Buddy listing](https://apps.apple.com/ca/app/migraine-buddy/id975074413)
- Refund rates are highest in Education (4.86%) and Health & Fitness (4.71%), and hard paywalls refund at 5.8% vs 3.4% for freemium — [RevenueCat SOSA 2025](https://www.revenuecat.com/state-of-subscription-apps-2025) [V]
- Search traffic without urgency does not pay: a study app with 88.3% of traffic from App Store search had zero revenue; an Anki alternative had 1,000 users and $21 MRR — [TrustMRR](https://trustmrr.com/startup/education-app-with-strong-aso-ready-for-social-media-growth?metric=mrr), [Indie Hackers](https://www.indiehackers.com/post/i-built-a-language-learning-app-to-replace-anki-1-000-users-21-mrr-3a730ebad2) [SR]
- Platform risk: one ten-app developer fell from $9K to about $1.5K a month; another had his developer account frozen by Apple — [Indie Hackers](https://www.indiehackers.com/post/jChJ6O2CpPMaLCa4NypB), [Indie Hackers](https://www.indiehackers.com/post/tech/building-an-app-portfolio-to-60k-mo-after-apple-froze-his-developer-account-LD7oNYzKSmWucRfKV1AO) [SR]
- Regulatory scrutiny: a wellness-only app was flagged as medical under 1.4.1 — [Apple forum thread 807508](https://developer.apple.com/forums/thread/807508) [V]
- TikTok and ad-led niches are a separate game: MonAI's growth came from one influencer, not search — [Starter Story mirror](https://rosetta.to/u/starterstory/this-app-makes-35k-month-with-one-influencer) [SR]
- Incumbent pricing power is itself a trap signal in reverse: scanner leaders earn millions a month and can outbid anyone on Search Ads — [Sensor Tower iScanner](https://app.sensortower.com/overview/1040093707?country=US) [EST]

### Inferences
- Urgent but rare (exam prep for one licence, small-claims evidence, post-surgery, custody dispute, sleep training): the need ends, so a recurring subscription will churn by design. The fit is a one-time unlock or a short fixed-term pass priced against the stakes, as paid-up-front TurboScan and Vaultaire's lifetime tier illustrate. Exam prep's 18% earning rate with a $20K median among earners suggests the model works when priced this way, but new cohorts must be re-acquired through search every cycle.
- Urgent but no money (debt negotiation, tenants in dispute, caregivers): I found no direct evidence either way; the caregiver and medication 11.3% figure is the nearest proxy and it is weak. Treat as unproven, not disproven.
- Regulated areas: an app that logs, organises and exports (for a doctor, accountant, lawyer or court) stays on the safe side of 1.4.1 and advice rules; an app that interprets or recommends (diagnosis, legal or financial advice) invites review scrutiny and liability. This framing is my inference from the 1.4.1 incident and the guideline wording, not a sourced rule.
- Android skew is a trap specific to this owner: in trades invoicing and personal finance tools, Android apps are roughly twice as likely to be earning as iOS apps in the Trend Apps data, so an iOS-only build addresses the smaller half of that demand.
- Estimated-revenue leaderboards overstate opportunity for a no-budget entrant because incumbents' revenue is partly bought with paid acquisition; the "small apps earning on under 10K downloads" count is the better lens.

### Gaps
- No quantitative evidence found on one-time-use apps' lifetime value versus subscription for urgent-but-rare problems.
- No data on willingness to pay among financially distressed users (debt, bill negotiation, benefits).
- No sourced examples of App Store rejections for legal or financial advice apps; searches returned only AI data-sharing material.
- Apple guideline 4.3 (duplicate or spam apps), relevant to a multi-app portfolio strategy, was not researched.
- FDA, HIPAA and state unauthorised-practice-of-law exposure for small app developers was not researched.
