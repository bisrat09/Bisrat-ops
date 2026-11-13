# Indie iOS revenue and categories: what actually makes money for solo developers (as of 2026-11-13)

Reading notes for the report writer:
- "Verified" below means published by a data platform from its own transaction data (RevenueCat, Adapty, Sensor Tower, Appfigures). "Self-reported" means a developer's own post with no audit.
- Both RevenueCat and Adapty datasets only contain apps that integrated a paid-subscription SDK and (for RevenueCat) passed a minimum install or revenue threshold. Apps that never earned anything are largely excluded, so real-world medians are lower than the figures here.
- Several pages returned 403 (Indie Hackers, Medium). Where a number comes only from a search-result summary and the page was not opened, it is marked "(snippet only)".

## 1. RevenueCat State of Subscription Apps (2026 edition, 2025 data): revenue distribution, conversion, churn, pricing

### Takeaway
The typical subscription app earns pocket change: median about $72/month one year after launch, top quartile $429/month, top 10% above $2,574/month, and only 17% reach $1K/month within two years (4.6% reach $10K). Both shares fell from the prior year, and growth is concentrating at the top.

### Cited Findings

Scope
- Dataset: 115,000+ apps, $16B+ revenue, 1B+ transactions; target period 2025. Included apps have active subscription revenue, meet a minimum install or revenue threshold, and use RevenueCat. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Report release was March 2026 (coverage gives March 12, 2026). — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)

Monthly revenue one year after launch
- All categories: median about $72; upper quartile $429; top 10% above $2,574; middle 50% spans $16 to $429. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- By category (median): Photo & Video $124, Gaming $56, Travel $35. Gaming top 10% reaches $4,554. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Conflict: PPC Land reports $4,554 as the Business category figure "at the 75th percentile", Education $3,614, Productivity $1,250 (top quartile), Travel $822, Gaming $552 (top quartile). This does not match the RevenueCat page extract, where $4,554 is Gaming's top 10%. Treat PPC Land's category table as unreliable until checked against the report charts. — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/); contradicted by [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Older comparison point (RevenueCat 2024 report, 2023 data): top 5% of newly launched apps made at least $8,880/month after one year; bottom 25% made no more than $19 (snippet only). — [MacRumors, 2024-03-13](https://www.macrumors.com/2024/03/13/most-subscription-apps-do-not-make-money/)

Reaching $1K and $10K monthly revenue (within 2 years of launch)
- $1K: 17.3% overall (Photo & Video 21.4%, Gaming 20.0%, Business 14.7%). $10K: 4.6% overall (Gaming 8.9%, Photo & Video 7.3%, Business 1.6%). — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Year-over-year decline: $1K share fell from 19% to 17%; $10K share fell from 5.3% to 4.6%. — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)
- Among apps that do get there, median days to $1K: 58 overall (Gaming 32, Business 113). Median days to $10K: 109 overall. This is conditional on success, so it describes winners only. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)

Growth concentration
- Median year-over-year MRR growth 5.3%. Top 10% grew 306%+, top 25% grew 80%+, bottom 25% shrank 33%+. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)

Conversion
- Download-to-paid by day 35: 2.0% overall median. Hard paywall 10.7% (top quartile above 20%); freemium 2.1%. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- By category (day 35): Health & Fitness 2.9%, Business 2.6%, Shopping 1.3%, Gaming 1.0%. North America 2.6% to 2.8% (page gives both). — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Trial-to-paid by trial length: 17 to 32 days 42.5%; 5 to 9 days 37.4%; 4 days or less 25.5%. By category: Travel 43.5%, Health & Fitness 37.7%, Gaming 25.0%, Photo & Video 22.2%. North America 34.2%. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Day-0 trial cancellation: 55.4% for 3-day trials, 39.8% for 7-day, 31.1% for 30-day. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Revenue per install: day 14 median $0.23 overall (hard paywall $2.32 vs freemium $0.27); day 60 $0.34 overall, North America $0.55. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- One-year retention of converted users is nearly identical for hard paywall (27%) and freemium (28%). — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)

Retention and LTV
- Year-1 realized LTV per payer: global median $23, top quartile $44+, North America $32. By category: Health & Fitness $35.64, Business $35.48, Gaming $11.22. By price tier: high $62.19, mid $28.75, low $10.69. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- One-year retention (median): high-priced plans 23%, low-priced 36%. Monthly plans at one year: 10.8% (low-priced), 6.1% (high-priced). Weekly plans at one year: 1.3% (low), 1.0% (high). — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)
- AI apps generate 41% more revenue per payer and churn 30% faster than non-AI apps. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)

Pricing and plan mix
- Most common prices: weekly $5, monthly $10, yearly $30. Median yearly price rose from $31.60 to $34.80; weekly median about $5.99. North America: monthly $9.99, yearly $39.99. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Plan mix about 42% monthly and 34% yearly. Productivity is 77% yearly. 46.5% of trials are 4 days or shorter (up from 42.1%). — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)

Adapty cross-check (State of In-App Subscriptions 2026; 16K apps, about $3B revenue, 2023 to 2025)
- Top 10% of apps capture 94.5% of subscription revenue, up from 92.7% in 2023. Median monthly revenue fell 22% year over year, from $627 to $492. 57.7% of new subscription apps earn under $1,000 in total revenue; 7.9% exceed $100,000. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- Weekly plans went from 43.3% of revenue (2023) to 55.5% (2025); monthly fell 21.1% to 11.7%; annual 29.2% to 22.5%. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- Day-380 retention for trial subscribers: annual 19.9%, monthly 14.2%, weekly 5.5% (snippet only). — [Adapty weekly/monthly/annual post](https://adapty.io/blog/weekly-monthly-annual-subscription-plan/)
- 12-month LTV: weekly with trial $49.27 to $54.50 (the article gives both), annual with trial $49.92. Trials raise LTV in Utilities (+85.1%), Health & Fitness (+63.6%), Education (+50.4%) and lower it in Productivity (-13.7%) and Lifestyle (-21.2%). — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- iOS takes 84.75% of subscription revenue vs Android 15.25%. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- Apps running 50+ paywall experiments had median revenue $914,734 vs $48,848 for apps running one. This is correlation; bigger apps can afford more tests. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)

### Inferences
- The two medians ($72/month RevenueCat, $492/month Adapty) differ because the samples and definitions differ (RevenueCat: new apps at 12 months; Adapty: all apps on its platform, which skew toward paid-acquisition teams). Both agree on the shape: a tiny head and a long near-zero tail.
- A realistic planning base case for one new solo subscription app is $16 to $429/month at 12 months. $1K/month is roughly a 1-in-6 outcome among apps that got far enough to be counted; counting apps that never earned, it is worse.
- At a North America year-1 LTV of about $32 per payer and 2.6% to 2.8% download-to-paid, each 1,000 US downloads is worth roughly $800 to $900 over a year at the median. Reaching $1K/month therefore needs on the order of 1,200 to 1,500 quality downloads per month, sustained. The bottleneck is distribution, not building.
- Weekly plans drive revenue share but mostly in paid-acquisition apps; with about 1% of weekly subscribers left after a year, they suit one-shot utility use, not an app relying on organic growth and reputation.
- Hard paywalls convert about 5x better with the same one-year retention, but that comparison is confounded by which apps choose hard paywalls (high-intent traffic).

### Gaps
- Exact 12-month revenue percentiles for every category (Health & Fitness, Utilities, Productivity, Education, Lifestyle) were not readable from the page; the secondary table that lists them conflicts with the primary page.
- No refund-rate figures retrieved.
- No "State of Subscription Apps 2025" numbers pulled separately; the 2026 edition's year-over-year comparisons stand in for it.
- Neither report isolates solo developers from teams.

## 2. Number of new App Store apps in 2025 to 2026 and what share earn anything

### Takeaway
New app supply roughly doubled in 2026 while downloads grew about 2%, so each new app competes for a thinner slice of attention. No source measures the share of all new apps that earn money; the best proxies say most earn nothing or close to it.

### Cited Findings
- Sensor Tower (via New York Times): about 600,000 new App Store apps in 2025, up 30%; about 560,000 in H1 2026 alone. Downloads rose 3% to 35.4B in 2025 and 2% to 17.6B in H1 2026. — [9to5Mac, 2026-07-20](https://9to5mac.com/2026-07-20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/)
- Sensor Tower (via The Information): 235.8K new App Store submissions in Q1 2026, up 84% year over year. Submissions had fallen 48% from 2016 to 2024 before rebounding. The data does not isolate AI-generated apps. — [Rokos Bas newsletter, 2026-04-16](https://rokosbas.beehiiv.com/p/april-16-2026)
- Appfigures: Q1 2026 releases up 60% year over year across both stores and up 80% on iOS; April 2026 to date up 104% both stores, 89% iOS. No absolute counts published. TechCrunch calls AI coding tools a "working hypothesis", not a confirmed cause. — [TechCrunch, 2026-04-18](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/)
- Category ranking of new releases, Q1 2026: Games first, Utilities second, Lifestyle third (up from fifth), Productivity newly in the top five, Health & Fitness fifth. — [TechCrunch, 2026-04-18](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/)
- Apple says it reviews 90% of submissions within 48 hours and holds all apps to the same standards. — [9to5Mac, 2026-07-20](https://9to5mac.com/2026-07-20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/)
- Apple's 2024 enforcement figures: 320,000+ submissions rejected as spam, copies, or misleading. — [TechCrunch, 2026-04-18](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/)
- Proxy for "share earning anything": 57.7% of new subscription apps on Adapty earn under $1,000 total; only 7.9% exceed $100,000. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- Proxy from a hackathon population (RevenueCat Shipaton 2026): 3,336 projects, 88.6% solo-built; only about 35 (roughly 1%) report any revenue or MRR figure. The analysis cannot tell non-earning from non-disclosing. — [PricePush Shipaton analysis, 2026-10-03](https://pricepush.app/blog/shipaton-2026-data)

### Inferences
- About 560K new apps in six months is roughly 93K per month or 3,000 per day on the App Store, against flat downloads. Organic discovery for an undifferentiated app is worse in late 2026 than at any point in the last decade.
- Because Apple rejects spam and copies under its design guidelines, template-like AI-built apps face a higher rejection risk as volume grows; this is inferred from the volume and Apple's stated standards, not from a published 2026 rejection rate.

### Gaps
- No source gives the share of all new App Store apps that earn any revenue. Sensor Tower and Appfigures publish release counts, not earnings distributions.
- No 2025 or 2026 Apple rejection statistics found (latest are for 2024).
- H2 2026 release counts not found.

## 3. Saturated categories vs categories with room for small developers

### Takeaway
Hard data shows where new apps are piling in (Health & Fitness, Productivity, Lifestyle, Games, Utilities; within them focus blockers, workout trackers, journals, habit trackers, budgeting). Evidence for "open" niches is mostly opinion; the data-backed signal is that Utilities and Health & Fitness monetize best per user, and Business/B2B converts well but ramps slowly.

### Cited Findings

Crowding (measured)
- Shipaton 2026 (2,139 published indie apps): Health & Fitness is the largest category at 304 apps (14.2%), then Productivity 288 (13.5%), Lifestyle 230, Games 204, Education 185; top five are 57% of apps. — [PricePush Shipaton analysis](https://pricepush.app/blog/shipaton-2026-data)
- Same dataset, keyword clusters: screen-time/focus blockers about 105, workout trackers about 100, journals/mood about 84, sleep/meditation 80, habit trackers 72, budgeting 70. 229 apps have "AI" in the name or tagline. — [PricePush Shipaton analysis](https://pricepush.app/blog/shipaton-2026-data)
- Utilities, Lifestyle, Productivity, and Health & Fitness are the fastest-rising categories for new releases in 2026 after Games. — [TechCrunch, 2026-04-18](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/)
- In Lifestyle, the top 10% of apps capture 97.9% of subscription revenue. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- AI apps earn 41% more per payer but churn 30% faster. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Opinion-level sources say generic AI chat wrappers are saturated and often rejected under App Store Guideline 4.3 (spam/copycat), and that a generic habit tracker "will not rank" (snippet only; blog sources). — [howtomakemoneyfromhome.online niche guide](https://howtomakemoneyfromhome.online/apps/best-app-niches-2026/); [pawelkarniej.com](https://pawelkarniej.com/blog/ai-mobile-app-ideas-for-indie-founders-2026/)

Where monetization is stronger (measured)
- Health & Fitness: highest download-to-paid (2.9%) and highest year-1 LTV per payer ($35.64); trial-to-paid 37.7%. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Health & Fitness also has the lowest first-renewal retention (30.3%) in Adapty's data, so it converts well and churns fast. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- Utilities: trial subscribers renew at 58.1% after the first cycle, more than 1 in 4 still pay at the fifth renewal, and trials add 85.1% to LTV. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- Business: download-to-paid 2.6%, year-1 LTV $35.48, download-to-trial 9.1% (highest), but only 1.6% reach $10K/month and median time to $1K is 113 days vs 58 overall. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Photo & Video: highest median 12-month revenue ($124/month) and highest share reaching $1K (21.4%), but lowest trial-to-paid (22.2%). — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Gaming: fastest to $1K (32 days) and highest $10K share (8.9%) but lowest LTV ($11.22) and conversion (1.0%). — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Opinion: profession-specific productivity tools are called "one of the most underserved" indie spaces (single blog author, snippet only). — [howtomakemoneyfromhome.online niche guide](https://howtomakemoneyfromhome.online/apps/best-app-niches-2026/)

### Inferences
- "Crowded" and "unprofitable" are not the same: HabitKit and Loggd (section 4) both earn in habit tracking, the most crowded niche, but one took years plus a large audience and the other makes about €250 MRR. Crowding raises the distribution bar, not the ceiling.
- For a solo owner with little marketing time, the measured profile that fits best is a narrow utility or a Health & Fitness sub-niche with a specific audience: high intent, decent retention (utilities) or high conversion (fitness), and keyword-driven discovery.
- Business/B2B micro tools look like slow-ramp, low-ceiling, good-LTV products: plausible for steady $500 to $2K/month, unlikely to hit $10K.
- The owner already ships a workout logger (Fitlog). That sits in the single most crowded Shipaton cluster (workout trackers, about 100 entries), so differentiation by audience would matter more than features.

### Gaps
- No reliable data found on faith/religious apps, kids apps, or hobby tools for small developers (revenue, competition, or conversion). These remain untested hypotheses in this file. Kids apps also carry extra App Store rules (Kids Category, ad and data limits) that were not researched here.
- No App Store keyword-competition data (search volume vs number of competing apps) was gathered; that is the direct way to test a niche and needs an ASO tool.
- No Sub Club or Launched episode was opened for category commentary.

## 4. Public revenue reports from solo indie iOS developers, 2024 to 2026

### Takeaway
All figures here are self-reported. The visible winners took years and credit distribution (US keyword ranking, audience, media), while the far more common outcome is tens to hundreds of dollars a month. Survivorship bias is severe: people with good numbers post them.

### Cited Findings

High earner
- HabitKit (Sebastian Röhl, solo, Germany; habit tracker on iOS and Android, originally Flutter): $602,000 total revenue in 2025, $28,000 MRR, 25,100 active subscribers, 272K App Store and 290K Google Play downloads. January 2025 alone was $112K. He credits reaching top 5 for "habit tracker" in the US App Store, a YouTube feature, a Starter Story interview, and building in public (20K X followers). Self-reported. — [Sebastian Röhl, 2025 recap, 2025-12-31](https://sebastianroehl.substack.com/p/2025-the-year-that-changed-everything)
- Trajectory: about $3,000 MRR at end of 2023 and $15,000+ MRR at end of 2024, i.e. multiple years to scale (snippet only). — [Starter Story](https://www.starterstory.com/habit-kit-breakdown)
- Same developer's second app, FocusKit (native SwiftUI, built with Cursor): one month after launch, 1,600 downloads, $874 total revenue, $52 MRR, despite his existing audience. — [Sebastian Röhl, 2025 recap](https://sebastianroehl.substack.com/p/2025-the-year-that-changed-everything)

Mid and low earners
- Loggd (Eusebiu Balan, solo; habits/tasks/journal app on web, iOS, Android): after 8 months, 6,012 registered users, 75 paying, about €250 MRR, €3,525 total. Monthly revenue peaked at €1,133 in June 2026 after the iOS launch and lifetime deals. Over 70% of users came from daily posting on Threads. — [loggd.life, 2026-07-22](https://loggd.life/blog/build-in-public-habit-tracker-saturated-niche)
- Habit Pixel (solo, iOS/Android habit tracker): about 8 months to roughly $1K MRR; one December report shows 697 subscribers, $840 MRR, $4,743 monthly revenue (snippet only; page returned 403). — [Indie Hackers](https://www.indiehackers.com/post/from-0-to-1k-mrr-in-8-months-bootstrapping-habit-pixel-as-a-solo-dev-53d8687d15)
- Roman Koch: shipped 8 apps in 2025, $1,464 total revenue after Apple fees, best app about $700 (snippet only; Medium returned 403). — [Roman Koch, Medium](https://medium.com/@romankoch/my-2025-recap-as-an-indie-developer-6846593eaad6)
- "Max" (Latvia): 28 apps in 8 months, $84K total 2025 revenue, about $3K per app on average (secondary article, snippet only, unverified). — [buildmvpfast.com](https://www.buildmvpfast.com/blog/portfolio-app-strategy-multiple-apps-revenue-solo-founder-2026)
- Shipaton 2026 self-reports: Buck ($13K+ revenue, $6K MRR), Mio ($30,000 revenue), Paternal ($23,385 first month), Ritmo ($830 MRR), Mekuru ($7 to $369 MRR in three weeks), Clucky ($261 MRR), Hitoiro ($509 gross in 28 days, still negative after ad spend). These are the roughly 1% of entrants who disclosed anything. — [PricePush Shipaton analysis](https://pricepush.app/blog/shipaton-2026-data)

AI-built ("vibe coded") examples
- Marco Pérez: InfoDrizzle, 7 weeks of work, 1,300 downloads, about $500 profit. Stampa, released May 2026 after about a week of work, 20,000 downloads, about $3,000 profit. Reported by the New York Times. — [9to5Mac, 2026-07-20](https://9to5mac.com/2026-07-20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/)
- David Svensson: 11 niche apps in five months, treats it as a hobby (no revenue given). — [9to5Mac, 2026-07-20](https://9to5mac.com/2026-07-20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/)
- In Shipaton 2026, 107 projects list Claude Code, 129 Codex, 38 Cursor among tools used; about 29% list an AI model. Swift/SwiftUI is the most common stack at 38.2%. — [PricePush Shipaton analysis](https://pricepush.app/blog/shipaton-2026-data)
- One commentator asserts vibe-coded apps tend to monetize with ads rather than in-app purchase; this is an assertion without measurement (snippet only). — [TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html)
- Apple removed a vibe-coding app in March 2026 and restricted updates to platforms like Replit, over rules against executing code that bypasses review. This targets app-builder apps, not apps written with AI assistance; Apple itself integrates Claude and Codex into Xcode. — [Rokos Bas newsletter, 2026-04-16](https://rokosbas.beehiiv.com/p/april-16-2026)

### Inferences
- Every growth story above credits distribution, not the product: a US keyword ranking, a daily social habit, a creator partner, or press. None credits build speed. AI coding removes the build cost but leaves the distribution cost unchanged.
- FocusKit is the most useful data point for expectations: a developer with a $600K/year app, 20K followers, and a polished native SwiftUI app still made $52 MRR in month one. A newcomer without an audience should expect less.
- The portfolio approach (many small apps) shows a wide spread: 8 apps for $1,464 in one case, 28 apps for a claimed $84K in another. The difference is not explained in the sources.
- There is no aggregate revenue data for AI-built apps. The two vibe-coded cases with numbers ($500 and $3,000 profit) are consistent with the general median, not better.

### Gaps
- Indie Hackers and Medium pages could not be opened (403); figures marked "snippet only" need verification before quoting.
- No Sub Club or Launched podcast episodes were reviewed beyond a pointer that RevenueCat's Launched interviewed Röhl in 2026 ([RevenueCat blog](https://www.revenuecat.com/blog/growth/sebastian-rohl-habitkit-launched-podcast-2026)).
- No Reddit r/iOSProgramming or r/SideProject threads were retrieved; these would add more low-earner reports.
- No independent verification exists for any developer figure listed here.

## 5. One-time purchase vs subscription vs ads vs paid upfront for small apps

### Takeaway
The data favors subscription with an annual plan plus a lifetime option for small apps; paid-upfront is nearly extinct among new indie apps, and ads only pay at a scale solo apps rarely reach. Direct, measured comparisons of one-time vs subscription for indie apps were not found.

### Cited Findings
- Paid upfront: only 7 of the Shipaton 2026 apps charge up front ($1.99 to $9.99); the rest are free to download. — [PricePush Shipaton analysis](https://pricepush.app/blog/shipaton-2026-data)
- One-time/lifetime is growing inside subscription apps: in Lifestyle, one-time purchases rose from 5.9% of revenue (2023) to 26.3% (2025). — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/)
- One-time, consumable, and lifetime plans grew from 6.4% to 10.3% of plan-type share between 2023 and 2025 (snippet only). — [Airbridge](https://www.airbridge.io/en/blog/subscription-vs-one-time-purchase-app)
- Loggd's revenue jump coincided with adding lifetime deals alongside the subscription. Self-reported. — [loggd.life](https://loggd.life/blog/build-in-public-habit-tracker-saturated-niche)
- Annual plans retain best: day-380 retention 19.9% annual vs 14.2% monthly vs 5.5% weekly (snippet only). — [Adapty weekly/monthly/annual post](https://adapty.io/blog/weekly-monthly-annual-subscription-plan/)
- Weekly plans produce 55.5% of subscription revenue but about 1% of weekly subscribers remain after a year. — [Adapty](https://adapty.io/blog/mobile-app-monetization-2026/); [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)
- Hard paywall vs freemium: 10.7% vs 2.1% download-to-paid, $2.32 vs $0.27 revenue per install at day 14, with near-equal one-year retention. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Higher prices earn more per payer despite lower retention: year-1 LTV $62.19 (high tier) vs $10.69 (low tier). — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps/)
- Fee structure: under the Small Business Program, subscriptions after their first year drop to 10% commission; one-time purchases stay at 15%. — [Apple Small Business Program](https://developer.apple.com/app-store/small-business-program/)
- Ads: eCPM benchmarks vary widely by source (banners $0.20 to $1.50, interstitials $2.50 to $8, rewarded video $8 to $30; one developer with 12 free iOS apps reports a blended $8.57). One source says ads are "pocket change" for indie apps and become viable around 1M+ monthly active users. All vendor or self-reported, snippet only. — [MonetizeMore](https://www.monetizemore.com/blog/how-much-ad-revenue-can-apps-generate/); [developer AdMob post](https://portfolio-site-ab3.pages.dev/blog/admob-reality); [appsfinboard](https://appsfinboard-landing-page.pages.dev/blog/mobile-app-monetization-strategies-2026/)
- An unverified secondary claim says RevenueCat found subscription apps earn 4.5x more lifetime revenue per user than one-time-purchase apps; it could not be confirmed in RevenueCat's report (snippet only). — [The Swift Kit](https://theswiftk.it.com/blog/how-to-monetize-ios-app-indie-developer)

### Inferences
- Ads arithmetic at indie scale: at an $8.57 blended eCPM, 10,000 monthly users each seeing 20 ads yields about $1,700/month, but an app with 10,000 active users is already far above the median. At 500 active users the same math gives about $85/month.
- For a narrow utility that people use occasionally, a one-time unlock or lifetime tier matches user expectations and avoids churn; the data supports offering it next to an annual plan, not instead of one.
- The 10% long-term subscription rate under the Small Business Program makes retained annual subscribers the most fee-efficient revenue.

### Gaps
- No measured head-to-head comparison of one-time vs subscription revenue for comparable indie apps.
- No reliable, independent ad-revenue dataset for small iOS apps; all eCPM numbers come from vendors or single developers.
- No data on paid-upfront conversion or revenue in 2025 to 2026.

## 6. Costs: Apple fees, US external payment links, RevenueCat, LLM API cost per user

### Takeaway
Fixed costs are low: Apple takes 15% (10% on subscriptions after year one) under the Small Business Program, RevenueCat is free under $2,500/month tracked revenue, and LLM cost per user ranges from about a cent to a few dimes per month depending on model. US external-link purchases currently carry zero Apple commission, but the rate is being re-litigated and could rise.

### Cited Findings

Apple
- Small Business Program: 15% commission on paid apps and in-app purchases for developers with up to $1M in proceeds in the prior calendar year, and for developers new to the App Store. Enrollment is required. Exceeding $1M mid-year returns future sales to the standard rate. — [Apple Small Business Program](https://developer.apple.com/app-store/small-business-program/)
- The same page states subscriptions after their first year get a further reduced 10% commission. — [Apple Small Business Program](https://developer.apple.com/app-store/small-business-program/)
- The page also describes Private Cloud Compute access: enrolled developers with fewer than two million first-time downloads can use Apple Foundation Models on PCC with no cloud API cost, subject to an entitlement. — [Apple Small Business Program](https://developer.apple.com/app-store/small-business-program/)

US external payment links (Epic v. Apple)
- April 2025: Judge Gonzalez Rogers found Apple in contempt and barred any commission on external-link purchases. December 2025: the Ninth Circuit upheld contempt but reversed the total ban, telling the district court to set a rate limited to "genuinely and reasonably necessary" costs, and allowed Apple to stop links being more prominent than in-app purchase options. — [Dataconomy, 2025-12-12](https://dataconomy.com/2025/12/12/court-affirms-apple-violated-injunction-while-allowing-outside-commissions/); [MacDailyNews, 2026-08-14](https://macdailynews.com/2026/08/14/u-s-supreme-court-clears-path-for-app-store-commission-showdown-as-apple-must-defend-its-rates-in-lower-court/)
- As of August 14, 2026: Apple charges zero commission on US external purchases. Justice Kagan denied Apple's stay on August 13, 2026, so the district court can proceed to set a rate. Apple proposed 15% standard, 10% for certain programs and subscription renewals, and 5% for Small Business Program apps. Epic argues the justified rate approaches zero. The Supreme Court agreed to review the contempt finding in its October 2026 term. — [MacDailyNews, 2026-08-14](https://macdailynews.com/2026/08/14/u-s-supreme-court-clears-path-for-app-store-commission-showdown-as-apple-must-defend-its-rates-in-lower-court/)

RevenueCat
- Free up to $2,500 in monthly tracked revenue; 1% of tracked revenue once past that. Growth tools (paywalls, web funnels, A/B tests) are charged at 1% of revenue on conversions from those tools. — [RevenueCat pricing](https://www.revenuecat.com/pricing/)

LLM API prices (Anthropic list prices, per million tokens, fetched 2026-11-13)
- Claude Haiku 5.5: $0.10 input, $0.50 output (prompts up to 100K tokens). Claude Haiku 4.5: $1 input, $5 output. Claude Sonnet 5.5: $2 input, $10 output. Claude Opus 5.5: $4 input, $20 output. Batch API gives 50% off; cache hits cost a small fraction of base input. — [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)

### Inferences
- LLM cost per active user (calculated from the list prices above, assuming 30 requests/month at 2,000 input and 500 output tokens each, i.e. 60K input and 15K output tokens): about $0.014/month on Haiku 5.5, about $0.14 on Haiku 4.5, about $0.27 on Sonnet 5.5, about $0.54 on Opus 5.5. Heavy chat-style use (10x that volume) scales linearly to roughly $0.14 to $5.40.
- Against a $9.99/month or $39.99/year price, a small-model AI feature costs well under 2% of revenue per paying user. The risk is free users: with about 2% of downloads paying, an ungated AI feature on a mid-tier model can cost more across free users than payers bring in. AI features should sit behind the paywall or a tight free quota.
- Net to developer on a $39.99 annual plan in year one: about $33.99 after Apple's 15%; RevenueCat adds nothing below $2,500/month.
- Not found in sources but standard: the Apple Developer Program fee is $99/year (the owner already has an account paid through 2027-09-10 per his own records).
- External web checkout at zero Apple commission would cost only payment-processor fees today, but with Apple's own proposal at 5% for small developers and the rate undecided, the saving over 15% in-app is uncertain and adds a web checkout to build and support. For a solo developer under $2,500/month it is not worth planning around yet.
- On-device Apple models (and the Private Cloud Compute offer above) could make AI features free to run for a native SwiftUI app; eligibility and capability need checking.

### Gaps
- No ruling setting the final US external-link commission was found as of this research; status after August 2026 (district court hearing, Supreme Court argument) was not retrieved and should be rechecked before any decision relies on it.
- OpenAI and Google API prices were not fetched; only Anthropic's were verified.
- No measured data on actual LLM spend per user from shipping indie apps; the per-user figures are calculations from list prices under stated assumptions.
- Details and availability of Apple's Private Cloud Compute developer access were not verified beyond the one mention on the Small Business Program page.
