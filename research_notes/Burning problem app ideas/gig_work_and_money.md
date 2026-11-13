# Gig work and money problems for immigrant (Habesha) workers: burning-problem test, iOS competition, solo-dev openings

Research date: 2026-11-13. App Store ratings counts, prices and "last updated" dates below were pulled the same day from the iTunes Search API (US storefront) and from App Store listing pages; each is linked to its listing. In-app purchase prices are as listed on the App Store page and may include legacy or promo SKUs.

Method caveats that apply throughout:
- Reddit threads (r/uberdrivers, r/lyftdrivers, r/doordash_drivers) did not surface in search, so driver sentiment comes from App Store reviews and trade press, not Reddit.
- The World Bank Remittance Prices Worldwide corridor page returned HTTP 403, so corridor cost data is second-hand and dated.
- Several numbers come from search-result summaries of the linked page rather than a full read of the page. Those are marked "(snippet)".

## 1. Rideshare and delivery driver tools: is it a burning, paid-for problem, and how crowded is iOS?

### Takeaway
Drivers do pay ($9 to $19 a month) for earnings and mileage tools, but the category is crowded with funded incumbents and a free leader (Stride, about 100K ratings), and the highest-value feature (multi-app auto-accept) is under active attack from Uber and Lyft. The less-served pain is deactivation: it is frequent, income-destroying, appeals are in-app and English-heavy, and no App Store app targets it, though in Washington the Drivers Union already does appeals for free.

### Cited Findings

Mileage, expense and tax trackers (iOS, US store, 2026-11-13)
- Stride: 99,516 ratings, 4.84 stars, free with no paid tier; listing claims "Join 2,600,000 people saving, for FREE" and an average $710/year tax saving — [App Store](https://apps.apple.com/us/app/stride-mileage-tax-tracker/id1041591359)
- Stride Health is a benefits/insurance company that had raised about $96M by its $47M Series C (Oct 2021); the mileage app is free (snippet) — [PR Newswire](https://prnewswire.com/news-releases/stride-raises-47m-to-provide-affordable-benefits-for-independent-workers-301408370.html)
- MileIQ: 116,182 ratings, 4.76 — [App Store](https://apps.apple.com/us/app/mileiq-mileage-tracker-log/id578830929). Third-party pricing trackers list a consumer "Unlimited" tier at $13.99/month and team tiers at $8 to $10 per user (snippet) — [PricingSaaS](https://pricingsaas.com/companies/mileiq)
- Everlance: 53,539 ratings, 4.83. In-app purchases: Starter $10.99/month or $89.99/year, Professional $119.99/year. Free plan includes 30 automatic trips per month. Negative reviews: trips split after a 10-minute stop (burning through the 30 free trips), unclassified trips pile up, no way to edit a trip's end point, worry that missed or split trips create tax risk — [App Store](https://apps.apple.com/us/app/mileage-tracker-by-everlance/id985378916)
- Hurdlr: 21,134 ratings, 4.74 — [App Store](https://apps.apple.com/us/app/hurdlr-mileage-expenses-tax/id951737201)
- Driversnote: 39,460 ratings, 4.78 — [App Store](https://apps.apple.com/us/app/mileage-tracker-by-driversnote/id924418916)
- TripLog: 4,809 ratings, 4.54 — [App Store](https://apps.apple.com/us/app/mileage-tracker-app-by-triplog/id585918522)
- QuickBooks (absorbed Self-Employed): 278,017 ratings — [App Store](https://apps.apple.com/us/app/intuit-quickbooks-for-business/id584606479)

Earnings and gig-assistant apps
- Gridwise: 28,651 ratings, 4.86; listing claims "1,000,000+ workers". Gridwise Plus is $14.99/month or $107.99/year. Features: auto mileage, earnings sync across platforms, airport and event insights, 50% off Keeper tax prep. Negative reviews: linked accounts log out and need reconnecting, duplicate earnings, sync not fully accurate, cluttered for delivery-only drivers — [App Store](https://apps.apple.com/us/app/gridwise-gig-driver-assistant/id1215991382)
- Gridwise has raised about $16M (2020 seed $3.3M, 2022 Series A $12.7M led by Crosslink); CB Insights lists $19.14M (snippet) — [Coverager](https://coverager.com/gridwise-raises-12-7-million/)
- Solo: 13,363 ratings, 4.73. In-app purchases from $10/month (Basic) to $15 to $20/month (Pro), $119.99/year. Negative reviews: pay guarantee not honoured, unreliable tracking, slow support, users with passkeys cannot link Uber, unease about sharing credentials — [App Store](https://apps.apple.com/us/app/solo-your-gig-business-app/id1586902173)
- Para: 6,958 ratings, 4.26, last updated 2024-05-09 (no update in about 30 months) — [App Store](https://apps.apple.com/us/app/para-gig-drivers-earn-more/id1548322258)
- TipTracker: 9,482 ratings — [App Store](https://apps.apple.com/us/app/tiptracker-track-your-income/id1161307849)
- New small entrants with almost no traction: DriverPal (123 ratings), ShiftTracker (12), ShiftMate (15), GigU on iOS (52) — [DriverPal](https://apps.apple.com/us/app/driverpal-gig-driving-tracker/id6745041790), [ShiftTracker](https://apps.apple.com/us/app/shifttracker-gig-worker-pay/id6761228803), [GigU](https://apps.apple.com/us/app/gigu-drive-smart-earn-more/id6775593538)

Multi-app and auto-accept tools, and their status under platform terms
- Mystro: 10,708 ratings, 4.54, updated 2026-11-05. $18.99/month or $139.99/year. Listing says it auto-accepts and auto-declines by filter and toggles other apps offline, for Uber, Uber Eats, Lyft, DoorDash and DiDi. Negative reviews: must stay in the foreground or it times out, missed rides, developer says platform app changes keep breaking it, several say about $18/month is not worth it — [App Store](https://apps.apple.com/us/app/mystro-driver-drive-deliver/id1524407919)
- Maxymo on iOS: 11 ratings, 3.55 — [App Store](https://apps.apple.com/us/app/maxymo-the-gig-driver-app/id6478421495)
- Lyft sent formal warnings to drivers detected using third-party apps, threatening deactivation for Terms of Service violations and citing "unauthorized credential sharing"; The Rideshare Guy says apps affected include Maxymo, Mystro, GigU, Solo and Gridwise, and notes Lyft offers no public API for driver tools (article updated 2025-06-20) — [The Rideshare Guy](https://therideshareguy.com/weekly-roundup-lyft-threatens-driver-deactivation-over-third-party-earnings-apps/)
- Uber has sent letters accusing Mystro of violating its terms; an Uber representative said using third-party tools to bypass the system breaks its Community Guidelines and Terms. A Lyft spokesperson said it had not disabled accounts for using them. Mystro and GigU claim up to 30% more earnings (snippet, 2025) — [The Hustle](https://thehustle.co/news/the-third-party-apps-uber-and-lyft-are-trying-to-kill)

Size and pay of the driver population
- Gridwise median Uber pay in 2025: $21.18/hour trip pay, $21.92/hour gross with bonuses, before expenses; Uber Eats median $14.07/hour (snippet) — [Gridwise](https://gridwise.io/blog/uber-driver-pay/how-much-do-uber-drivers-make)
- Dec 2024 to Dec 2025: rider prices up 9.6%, driver gross pay per hour up 4.1%, delivery pay per hour up 3.2% while hours on platform rose about 17% (snippet) — [Entrepreneur](https://www.entrepreneur.com/business-news/uber-lyft-rides-got-more-expensive-2025)
- An estimated 35,000 Uber drivers in Washington were covered by the 2023 appeals agreement (dated 2023) — [WA L&I](https://www.lni.wa.gov/news-events/article/23-26/)
- No government or company statistics exist on the immigrant share of ride-hail drivers nationally; one study put New York City's app ride-hail drivers at 86% immigrant (older data) (snippet) — [NELP](https://www.nelp.org/publication/app-based-workers-speak-studies-reveal-anxiety-frustration-and-a-desire-for-good-jobs/)
- King County had an estimated 40,617 East Africa-born residents on 2014 Census data (dated) (snippet) — [City of Seattle OIRA 2016](https://www.seattle.gov/documents/departments/oira/2016_oira_09_eastafricanreport_final.pdf)

Washington and Seattle specifics
- 2026 TNC minimums (effective 2026-01-01): trips in Seattle $0.70 per passenger minute and $1.63 per passenger mile, or $6.12 minimum; elsewhere in Washington $0.40 per minute and $1.38 per mile, or $3.55 minimum. Tips cannot count toward the minimum (snippet) — [WA L&I compensation](https://www.lni.wa.gov/workers-rights/industry-specific-requirements/transportation-network-company-drivers-rights/getting-paid)
- From 2026-07-01 a TNC must give each driver a downloadable record of per-trip receipt data for the previous 24 months (snippet) — [WA L&I compensation](https://www.lni.wa.gov/workers-rights/industry-specific-requirements/transportation-network-company-drivers-rights/getting-paid)
- Since 2023-01-01 Washington rideshare drivers have minimum rates, paid sick time, workers' compensation and retaliation protection; the state law covers passenger drivers only, not food or goods delivery; notices of rights are published in 16 languages — [WA L&I](https://www.lni.wa.gov/workers-rights/industry-specific-requirements/transportation-network-company-drivers-rights/)
- The Driver Resource Center is run by Drivers Union under contract with L&I. It represents drivers in eligible deactivation appeals (loss of access for 3 or more consecutive days, with exclusions such as assault, harassment and wilful fraud) and provides "culturally appropriate" services. Deactivation notices must give the reason, policy violated, dates, appeal rights and the right to use paid sick time during deactivation. Contact: 206-812-0829 — [WA L&I](https://lni.wa.gov/workers-rights/industry-specific-requirements/transportation-network-company-drivers-rights/resource-center-and-deactivations)
- Drivers Union (Teamsters Local 117 affiliate) has helped more than 2,000 drivers get reinstated over five years. One Washington driver won an Uber appeal after about four years; appeals run through the app, which is hard for drivers with English as a second language — [The American Prospect, 2026-09-23](https://prospect.org/2026/09/23/rideshare-drivers-want-fair-hearing-before-losing-their-jobs/)
- A UW study of Seattle's 2021 to 2023 resolution centre found about 80% of drivers assisted by Drivers Union were reactivated (dated 2023) (snippet) — [The Columbian](https://www.columbian.com/news/2023/aug/07/uw-study-finds-racial-bias-in-rideshare-driver-deactivations/)
- Contrast case without a strong appeals body: Chicago data for 2019-01-01 to 2026-07-20 show 30,881 rideshare drivers deactivated and 1,085 reinstated (about 3.5%). Top reasons: account sharing 30.4%, fraudulent onboarding documents 26.8%, safety conduct 21.7%. One driver was deactivated after logging in on a new iPhone and lost an estimated 60% of income — [The American Prospect](https://prospect.org/2026/09/23/rideshare-drivers-want-fair-hearing-before-losing-their-jobs/)
- Illinois enacted a law in August 2026 creating a path to a deactivation appeals process; Maryland, Virginia and Ohio have proposed or passed appeal-transparency laws — [The American Prospect](https://prospect.org/2026/09/23/rideshare-drivers-want-fair-hearing-before-losing-their-jobs/)
- Seattle's App-Based Worker Deactivation Rights Ordinance (effective 2025-01-01) covers delivery-type app workers; a city fact sheet says it does not apply to TNC (rideshare) drivers. The Ninth Circuit upheld it in May 2026 (snippet) — [Seattle OLS fact sheet](https://www.seattle.gov/documents/Departments/LaborStandards/ABWDEAC_FactSheet_contrast_ADA.pdf); [Race to the Bottom](https://www.theracetothebottom.org/rttb/2026/5/22/ninth-circuit-upholds-seattles-app-based-worker-deactivation-rights-ordinance)
- Seattle app-based (delivery) minimum pay as reported for 2025: the greater of $0.44 per minute plus $0.74 per mile, or $5 per offer (2025 figure, may have been adjusted) (snippet) — [Seyfarth](https://seyfarth.com/news-insights/additional-protections-for-seattle-app-based-workers-take-effect-on-january-1-2025.html)
- Seattle OLS resolved deactivation cases in Q2 2026 against Uber Eats, DoorDash and Grubhub, including one DoorDash reinstatement with $1,278.16 paid (snippet) — [Seattle OLS](https://www.seattle.gov/laborstandards/investigations/resolved-investigations/april-june-2026)

### Inferences
- Mileage and expense tracking is solved for free (Stride) and by at least six apps with 20K to 116K ratings each. A generic tracker from a solo developer has no opening. The only angle is language: none of the listings checked mention Amharic, Tigrinya, Oromo or Somali, but a language skin on a commodity feature is a weak reason to pay.
- Auto-accept and multi-app tools carry the highest willingness to pay ($19/month) and the highest risk. They rely on driver credentials or on reading the platform apps, the platforms call this a terms violation, and Lyft has threatened deactivation. Shipping one to a community that trusts you, and getting members deactivated, would burn the trust edge. Avoid.
- Paid tiers cluster at $9 to $19/month and about $90 to $140/year, which shows the price ceiling drivers accept for a tool that directly raises or protects income.
- Deactivation is the most "burning" item here (sudden total income loss, low reinstatement outside Washington, English-only in-app process). But in Washington the paid fix is already free via Drivers Union, so a Seattle-first app would compete with a free union service. The gap is in states without a resource centre (DC, Minnesota, Colorado, Illinois until its new process starts) and in prevention, for example warning that a new phone login or shared account triggers deactivation.
- Washington's July 2026 rule giving drivers 24 months of downloadable trip data creates a clean, terms-safe data source: an app could import the driver's own export rather than scraping with credentials. This is a possible wedge for a "did I get paid the legal minimum, what did I actually net" checker, in-language.

### Gaps
- No current count of active Uber, Lyft or DoorDash drivers nationally or in Washington was found; the 35,000 Washington Uber figure is from 2023.
- No source quantifies the East African share of Seattle, DC, Minneapolis or Denver drivers. The brief's premise is plausible from press coverage but unmeasured.
- Washington paid sick time accrual rate and the per-trip funding of the Driver Resource Center were not on the pages retrieved.
- Whether Mystro's auto-accept is fully functional on iOS (versus Android) could not be verified beyond its own App Store description.
- Revenue for any of these apps was not found. Funding found only for Gridwise and Stride; none found for Solo, Everlance, Mystro or Para.
- No Reddit evidence was retrieved.

## 2. Tax filing for 1099 gig workers and immigrants: 2025 law changes, ITIN, existing apps and prices

### Takeaway
The 2025 law created real confusion and real money for drivers (tip deduction up to $25,000 through 2028, with app-based rideshare and delivery added to the occupation list in April 2026), but filing itself is dominated by giants and by free or near-free options. The opening is explanation and preparation in-language, not a filing product, and it must stop short of tax advice.

### Cited Findings
- IRS Fact Sheet FS-2026-07 (March 2026): eligible gig workers can deduct up to $25,000 of qualified tips per return for tax years 2025 to 2028; for the self-employed the deduction is limited to net income from that business; tips must be reported on Form 1099-NEC, 1099-MISC or 1099-K; for 2025 those forms do not separately show tips; the 1099-K threshold reverted to more than $20,000 and more than 200 transactions; QBI deduction made permanent; 100% bonus depreciation for assets such as vehicles acquired after 2025-01-19 with more than 50% business use — [IRS](https://www.irs.gov/newsroom/the-working-families-tax-cuts-what-gig-economy-workers-should-know)
- Final regulations listing tipped occupations were issued 2026-04-10 (IR-2026-49); gig workers qualify if their occupation is listed; there is an "800s Transportation and Delivery" group; tips must appear on W-2, 1099-NEC, 1099-MISC, 1099-K or Form 4137 — [IRS](https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-listing-occupations-where-workers-customarily-and-regularly-receive-tips-under-the-one-big-beautiful-bill)
- Practitioner summary: the final rule revised "Goods Delivery People" and "Taxi and Rideshare Drivers and Chauffeurs" to include app or platform-based workers (snippet) — [Western CPE](https://www.westerncpe.com/blog-post/irs-finalizes-no-tax-on-tips-regulations/)
- Conflicting guidance is still circulating: a mid-2026 consumer guide says it is safest to assume gig workers do not get the tip deduction (snippet) — [CountryTaxCalc](https://www.countrytaxcalc.com/tax-guides/usa/gig-delivery-tips-tax-guide-2026/)
- Tax Notes reported that messaging around the tip deduction misled some workers about how it works (snippet) — [TaxProf Blog, 2026-07-03](https://taxprofblog.aals.org/2026/07/03/tax-notes-check-please-workers-react-to-no-tax-on-tips-one-year-in/)
- Quarterly estimates: in a 1-800Accountant survey of 300 small business owners, 45% named quarterly estimated taxes as the deadline they were most likely to miss (not a gig-specific sample) (snippet) — [Stacker, 2026-10-29](https://stacker.com/stories/small-business/americas-side-hustle-economy-has-tax-problem)
- Prices people pay today: TurboTax Self-Employed about $139 federal plus $64 per state; H&R Block Self-Employed about $85 to $130 plus $37 to $49 per state; TaxSlayer Self-Employed $64.95 plus $39.95; FreeTaxUSA free federal including self-employed forms plus $15.99 per state (aggregator figures) (snippet) — [SuperMoney](https://www.supermoney.com/turbotax-vs-freetaxusa); [Work Club](https://work-club.com/best-tax-software-self-employed-2026/?noamp=mobile)
- iOS filing apps: TurboTax 937,850 ratings; H&R Block 115,616; Keeper 12,799 (4.78); FlyFin 549 — [TurboTax](https://apps.apple.com/us/app/turbotax-file-your-tax-return/id940247939); [H&R Block](https://apps.apple.com/us/app/h-r-block-tax-prep-file-taxes/id482050344); [Keeper](https://apps.apple.com/us/app/keeper-tax-filing-expenses/id1471090941); [FlyFin](https://apps.apple.com/us/app/flyfin-1099-taxes/id1560766719)
- Keeper is listed by one aggregator at about $16.58/month with no public pricing page (unverified) (snippet) — [Toolradar](https://toolradar.com/tools/keeper-tax/pricing)
- Stride (free) bundles tax filing prompts and deduction finding with its mileage tracker — [App Store](https://apps.apple.com/us/app/stride-mileage-tax-tracker/id1041591359)
- App Store search for "Amharic tax" and "gig worker tax ITIN" returned only mainstream apps (H&R Block, Solo, Gridwise); no Amharic or ITIN-specific tax app surfaced — [iTunes Search API](https://itunes.apple.com/search?term=Amharic+tax&entity=software&country=us)

### Inferences
- The overtime deduction applies to wage overtime, so it is relevant to W-2 airport, parking and home care workers, not to 1099 drivers. This is an inference from the IRS gig fact sheet not mentioning it; it was not directly verified.
- "Do I qualify for no tax on tips, and how much is it worth to me?" is a live, confusing, time-boxed question (2025 to 2028) with no in-language explainer found. It fits a calculator or checklist feature inside a driver app, and it is strong content for community reach, but on its own it is a seasonal hook rather than a subscription.
- Filing is not a solo-dev market: e-file requires IRS authorisation and incumbents have 100K to 900K ratings. A realistic shape is "tax-ready packet" (mileage total, tips total from platform summaries, quarterly reminders) that hands off to a human preparer. Many Habesha drivers already use a community preparer, so the app's customer could be the preparer.
- Risk: anything that tells a user what to claim reads as tax advice. Keep to calculators with IRS citations and "confirm with a preparer" language.

### Gaps
- Whether ITIN holders can claim the tip deduction (SSN requirement) was not addressed on the IRS pages retrieved. This matters for part of the audience and needs checking against the statute or Schedule 1-A instructions.
- Income phaseout thresholds for the tip deduction were not on the pages retrieved.
- No survey was found measuring how many drivers understand the tip deduction or miss estimated payments.
- ITIN application costs, IRS Direct File status for the 2027 season, and immigrant fears about IRS data sharing were not researched to a citable level.
- What Habesha community tax preparers charge and how many drivers use them is unknown; this is a question for direct interviews.

## 3. Remittance to Ethiopia and Eritrea, 2025 to 2026: is a rate-comparison or alert app viable?

### Takeaway
The pain is large and current: most diaspora money still moves informally because of the rate gap, and on the same day licensed apps differed by roughly 10% on the birr rate. But comparison is already free (Monito covers USD to ETB with an app), affiliate payouts are small per user, and the corridor's real competitor is the informal market, which an App Store app cannot list. Viable only as a low-cost feature or audience builder, not as a business on its own.

### Cited Findings

Size and behaviour
- Ethiopia's diaspora remittances reached $8.2 billion in fiscal 2025/26 according to the Ethiopian Diaspora Service (snippet) — [Ethiopian Business Review, Sep 2026](https://ethiopianbusinessreview.net/?p=18010)
- A UNDP profile reports remittance inflows of $3.3 billion "by May 2026" (snippet); this conflicts with the $8.2B figure and likely reflects a different period or definition — [UNDP, June 2026](https://www.undp.org/sites/g/files/zskgke326/files/2026-07/quarterly_economic_profile_june_2026_4_final.pdf)
- Commercial Bank of Ethiopia's October 2025 estimate: 22% of remittances are formal, 78% go through informal networks such as hawala and black-market dealers (snippet) — [Ethiopian Business Review](https://ethiopianbusinessreview.net/?p=18010)
- "Despite floating the Birr, Ethiopia's formal remittance system remains underutilized"; informal channels endure for undocumented migrants and low-wage workers (2025-06-14, teaser only) — [Shega](https://shega.co/news/why-most-ethiopians-abroad-still-avoid-banks-to-send-money-home)

Exchange-rate gap
- May 2026: official weighted rate 159.6 birr per USD, parallel market close to 180 (about 13% premium) (snippet) — [UNDP, June 2026](https://www.undp.org/sites/g/files/zskgke326/files/2026-07/quarterly_economic_profile_june_2026_4_final.pdf)
- Analysts estimate the premium above 15% while NBE officials say below 11%; parallel rates spiked to about 190 against an official rate under 160 (snippets) — [Capital Ethiopia](https://capitalethiopia.com/?p=80916); [Capital Ethiopia](https://capitalethiopia.com/?p=73926)
- Addis Fortune reported a parallel rate of 189.48, over 23% above official (snippet) — [Addis Fortune](https://addisfortune.news/?p=46274)
- IMF flagged a premium of roughly 15% in July 2025 (snippet) — [The Star, 2025-08-06](https://www.the-star.co.ke/news/africa/2025-08-06-ethiopia-bans-four-us-based-money-transfer-firms)

Regulatory pressure on informal channels
- NBE banned or flagged four US-based money transfer firms in August 2025, has repeatedly warned the diaspora against unlicensed operators, said about 100 firms are licensed, and warned of confiscation (snippets) — [The Star](https://www.the-star.co.ke/news/africa/2025-08-06-ethiopia-bans-four-us-based-money-transfer-firms); [NBE press release](https://nbe.gov.et/nbe_news/press-release-notice-on-the-use-of-licensed-money-transfer-agents-for-remittances-to-ethiopia/); [Addis Fortune](https://addisfortune.news/nbe-expands-diaspora-warning-over-unlicensed-remittance-firms)

Prices among licensed providers
- Monito live comparison for 100 USD to an Ethiopian bank account (fetched 2026-11-13): Taptap Send no fee at 180.20; XE $5 fee at 181.00; Remitly no fee at 165.05; Western Union no fee at about 161.00; mid-market shown as 163.19. Providers listed include Ria, Wise, Remitly, Western Union, WorldRemit, XE, Taptap Send and MoneyGram — [Monito](https://www.monito.com/send-money/united-states/ethiopia/usd/etb)
- World Bank Remittance Prices Worldwide, US to Ethiopia, Q3 2024 as quoted by an aggregator: median total cost 6.36% for $200, range 2.99% to 10.60% across 19 providers (dated, second-hand) (snippet) — [moneytransferbycountry](https://moneytransferbycountry.pages.dev/send-money-to-ethiopia/)

US 1% remittance excise tax
- Effective for transfers from 2026-01-01; applies when the sender pays with cash, a money order, a cashier's check or a similar physical instrument; providers collect it, deposit semi-monthly and file quarterly; proposed regulations issued 2026-04-10 (REG-114499-25) and are not final (snippet) — [IRS](https://www.irs.gov/newsroom/treasury-irs-issue-proposed-regulations-on-the-new-remittance-transfer-tax-established-under-the-one-big-beautiful-bill)
- Digital providers are marketing "send digitally to avoid the 1% tax" (vendor source) (snippet) — [Western Union](https://www.westernunion.com/blog/en/us-remittance-tax/)
- Commentary notes the tax falls on unbanked senders with the fewest channel options (snippet) — [JD Supra](https://www.jdsupra.com/legalnews/un-banked-tax-101-the-irs-proposes-6744962/)

Existing comparison tools and corridor apps
- Monito: free comparison, states it "receives a referral fee from the provider you selected", has iOS and Android apps, and claims 6 million users a year (its pages give inconsistent user figures) — [Monito](https://www.monito.com/send-money/united-states/ethiopia/usd/etb)
- Indie comparison apps on iOS have near-zero traction: RemitRate (1 rating), FloExchange (4 ratings) — [RemitRate](https://apps.apple.com/us/app/remitrate-compare-remittance/id6780613100); [FloExchange](https://apps.apple.com/us/app/floexchange-compare-rates/id6760972874)
- ET Forex: Birr Exchange Rates, an indie birr-rate app, has 0 ratings (updated 2026-09-23) — [App Store](https://apps.apple.com/us/app/et-forex-birr-exchange-rates/id6811115038)
- A parallel-rate app can gain traction in other corridors: Aboki Forex (Nigerian naira rates) has 3,106 US ratings — [App Store](https://apps.apple.com/us/app/aboki-forex-currency-converter/id1144186124)
- Senders' apps by US ratings: Remitly 2,826,854; Western Union 1,356,994; Xoom 1,213,640; MoneyGram 714,841; Ria 305,331; WorldRemit 215,475; Wise 114,038; Taptap Send 101,965; Sendwave 87,272 — [Remitly](https://apps.apple.com/us/app/remitly-send-money-transfer/id674258465); [Taptap Send](https://apps.apple.com/us/app/taptap-send-money-transfer/id1413346006); [Sendwave](https://apps.apple.com/us/app/sendwave-send-transfer-money/id846717081); [WorldRemit](https://apps.apple.com/us/app/worldremit-money-transfer-app/id875855935)
- Ethiopian bank apps are poorly rated in the US store: CBE Mobile Banking 3.23 stars (2,698 ratings), telebirr 3.64 (1,550) — [CBE](https://apps.apple.com/us/app/cbe-mobile-banking/id1534203410); [telebirr](https://apps.apple.com/us/app/telebirr/id1553601084)
- New entrants still target the corridor: "Birr Remit" (HashPay LLC) is a pre-launch, blockchain-settled US to Ethiopia service advertising a $3.99 flat fee, with FinCEN registration "in progress" — [Birr Remit](https://birrremit-website.pages.dev/)

Affiliate economics
- Remitly's affiliate programme on FlexOffers lists $1.60 per first transfer with a 30-day cookie; other directories list $4 to $20 per lead or $10 per first transfer (sources conflict) (snippets) — [FlexOffers](https://www.flexoffers.com/affiliate-programs/remitly-affiliate-program); [Lasso](https://getlasso.co/affiliate/remitly/)
- Remitly's separate Ambassador programme pays at least $40 per qualifying transfer using a personal offer code, varying by country (snippet) — [Remitly](https://www.remitly.com/us/en/partnerships/ambassador-program)

### Inferences
- The same-day spread between licensed apps (about 161 to 181 birr per dollar on Monito, roughly 12%) is worth about $20 on a $200 transfer. That is a clear, checkable saving, so rate comparison has real user value in this corridor specifically.
- Some licensed apps were quoting above the mid-market rate, close to parallel-market levels. If that holds, the classic reason to use hawala is weakening and a "today's best legal rate" alert becomes more useful. This reading rests on one Monito fetch and should be re-checked by hand before it drives a decision.
- Revenue is thin. At $1.60 to $20 per new customer, paid once, 5,000 referred first-time senders would earn roughly $8,000 to $100,000 in total, and most Habesha senders already hold accounts with these providers, so few count as "new". The Ambassador programme ($40+) is better suited to an individual with community reach than an affiliate app is.
- The 1% tax only bites cash and money-order senders. For anyone already on an app it is a non-event, so it is a one-line explainer, not a product.
- App Store and legal risk is low for display and comparison of licensed providers with outbound links (no custody of funds). Risk rises sharply if the app shows parallel-market rates or facilitates informal transfer, given NBE's enforcement posture. That risk assessment is inference, not a cited rule.
- Eritrea is a separate, thinner corridor with a fixed official rate and few licensed digital options; nothing citable was found.

### Gaps
- No Eritrea-specific data (rates, providers, volumes) was found.
- No measured data on how senders changed behaviour after the 1% tax; all sender-facing material is vendor marketing.
- US-to-Ethiopia volume specifically (versus all diaspora) was not found.
- Wise and WorldRemit affiliate payout amounts were not found; Remitly's true current rate is unconfirmed.
- Monito's app ratings count and whether it sends rate alerts for ETB were not verified.
- World Bank primary corridor data for 2025 to 2026 could not be retrieved (403).

## 4. Informal savings circles (equb): prevalence, pain, existing apps, and legal limits

### Takeaway
Equb is culturally universal, but US prevalence is unmeasured, the money-moving version needs licences a solo developer cannot get, and every tracker-only savings-circle app in the US App Store sits at 0 to 200 ratings. Venture money goes to regulated, money-moving players in Egypt, Saudi Arabia and Ethiopia. A free tracker is easy to build and hard to charge for.

### Cited Findings
- No hard numbers exist on ROSCA prevalence in the US; the main US academic study used a non-representative sample (snippets) — [In These Times](https://inthesetimes.com/article/rosca-collective-money-circles-banking-immigrants); [SuperMoney](https://www.supermoney.com/encyclopedia/rotating-savings-and-credit-association)
- In Ethiopia, a survey cited by Milken Scholars found 51% of informal business owners rely on own savings and equb for start-up capital; in digital equb "trust shifts toward the institution" (snippet) — [Milken Scholars](https://www.milkenscholars.org/features/show/how-a-community-finance-system-is-being-modernized-in-ethiopias-digital-era)
- Mission Asset Fund (San Francisco) formalised lending circles by recording contributions and payouts and reporting them to credit bureaus (2013 report, dated) (snippet) — [The World](https://theworld.org/stories/2013/08/15/california-group-helps-immigrants-move-traditional-financial-sector)

Ethiopian equb apps (all operate in Ethiopia; US App Store traction is negligible)
- eQUB (Equb Financial Technologies): 11 US ratings; English plus four local languages; added in-app payments; was raising a first seed round targeted for end of 2025, close not confirmed — [App Store](https://apps.apple.com/us/app/equb/id6450191698); [TechCrunch, 2024-02-27](https://techcrunch.com/2024/02/27/mwc-ethiopian-fintech-equb-digitizes-peer-to-peer-credit/)
- Digital Equb: 49 US ratings; describes itself as a legally recognised equb service provider with a money guarantee (own claim) — [App Store](https://apps.apple.com/us/app/digital-equb/id1592078361)
- Virtual Equb: 3 ratings; Atrafi Equb: 1 rating — [Virtual Equb](https://apps.apple.com/us/app/virtual-equb/id6478144165); [Atrafi Equb](https://apps.apple.com/us/app/atrafi-equb/id6765470583)

Funded players elsewhere
- MoneyFellows (Egypt): $13M pre-Series C in May 2025, over $60M raised in total, says it is profitable in Egypt; 184 ratings in the US store — [TechCrunch, 2025-05-04](https://techcrunch.com/2025/05/04/moneyfellows-raises-13m-to-take-its-group-savings-model-outside-egypt); [App Store](https://apps.apple.com/us/app/money-fellows-online-circles/id1113492041)
- Hakbah (Saudi Arabia): 2,184 US-store ratings; Circlys (Saudi): 5,934 — [Hakbah](https://apps.apple.com/us/app/%D9%87%D9%83%D8%A8%D9%87-hakbah/id1462286908); [Circlys](https://apps.apple.com/us/app/circlys-%D8%B3%D9%8A%D8%B1%D9%83%D9%84%D9%8A%D8%B2/id1224588436)
- Esusu (US) began with savings circles and now sells rent reporting for credit building: reported $1B valuation (Jan 2022) and a $50M Series C dated 2025-12-11 per CB Insights (snippet); its current app has 274 ratings — [CB Insights](https://www.cbinsights.com/company/esusu/financials); [App Store](https://apps.apple.com/us/app/esusu-pay-rent-build-credit/id6482578399)
- TANDA (Tanda Technologies, US, ex-Yahoo product): $4.5M seed in November 2023 (snippet). It did not appear in a US App Store search or ID lookup on 2026-11-13, although a search summary described it as still live, so its status is unclear — [FinSMEs](https://finsmes.com/2023/11/tanda-raises-4-5m-in-seed-funding.html)
- StepLadder is a UK home-deposit savings-circle fintech founded 2016; no US presence or funding figure found (snippet) — [Village](https://village.ai/company/stepladder-uk-)

US tracker-style and small apps
- Junta: Trusted Savings 200 ratings; The SUSU App 5; SaveTogether 8; Daret 3; Tandapp 0; SusuWallet 0; "Savings Circle: Group Savings" 0 — [Junta](https://apps.apple.com/us/app/junta-trusted-savings/id1530022030); [The SUSU App](https://apps.apple.com/us/app/the-susu-app-savings-circle/id6748971171); [SaveTogether](https://apps.apple.com/us/app/savetogether-savings-tracker/id6759933361); [Tandapp](https://apps.apple.com/us/app/tandapp-group-savings-tracker/id6763742265)

Legal constraints
- Money transmitter status is a facts-and-circumstances test that turns on accepting and transmitting funds; FinCEN's 2019 guidance covers both transactional and account-based models (snippet) — [FinCEN](https://www.fincen.gov/resources/statutes-regulations/administrative-rulings/application-money-services-business-2); [Greenberg Traurig](https://gtlaw.com/ko/insights/2019/6/fincen-issues-guidance-on-application-of-fincens-regulations-to-certain-business-models)
- FinCEN MSB registration does not replace state money transmitter licences, which most money-moving businesses need state by state (snippet) — [InnReg](https://www.innreg.com/licensing/by-sector/money-services-business-registration)

### Inferences
- A tracker-only equb app (members, rounds, payout order, who has paid, receipts, reminders, with payments made outside the app by Zelle or cash) does not accept or transmit funds, so it should fall outside money transmission. No source retrieved addresses tracker-only apps directly; this needs a lawyer's confirmation before launch.
- The seven-plus tracker apps at 0 to 200 ratings suggest the tracker is not a problem people search the App Store to solve; a WhatsApp group and a notebook are "good enough". The real pain (default risk, a collector who disappears) is only solved by holding or guaranteeing money, which is the licensed part.
- Esusu's pivot from circles to rent reporting, and MoneyFellows' need for $60M+, both point to circles being a weak standalone business without lending or payments.
- The Habesha trust edge is real here (an equb is run by a trusted "dagna"), so distribution through a few respected organisers is plausible. Monetisation is the weak point: charging the organiser a few dollars per round is the only clean model, and volumes would be small.
- Credit-building is the feature circle members might value enough to pay for, but credit-bureau furnishing has its own compliance burden.

### Gaps
- How many US Habesha households are in an equb, typical pot sizes, and how often disputes occur: no data found. Needs interviews.
- No state-level ruling or App Store guideline text specific to ROSCA apps was retrieved.
- Hakbah and eQUB funding amounts were not found. Pari and Bloom Money were not researched.
- TANDA's current availability is unresolved.

## 5. Small ethnic business needs, home care agencies, iddir, and immigrant truckers

### Takeaway
No clearly underserved recurring-software pain was confirmed for Habesha small businesses in this pass; evidence here is thin and mostly absence of evidence. Two items stand out for follow-up interviews: iddir dues and membership tracking (no purpose-built app found) and the 2025 to 2026 English-proficiency enforcement against truck drivers, which is an urgent, livelihood-threatening problem with no dedicated iOS app found.

### Cited Findings

Iddir (funeral and mutual-aid associations)
- A search for iddir or edir management software returned only generic dues tools (Membership and Dues Manager, Cheddar Up, MemberTies, Wild Apricot, Airtable templates); nothing built for iddirs — [Wild Apricot](https://www.wildapricot.com/blog/membership-dues); [Cheddar Up](https://www.cheddarup.com/membership-management-software)
- App Store searches for "iddir" and "edir" return no relevant app; "eDir" is an unrelated Somali mobile-wallet tool (21 ratings) — [App Store](https://apps.apple.com/us/app/edir/id1583574024)

Habesha-specific apps as a benchmark for community reach
- The largest Ethiopian or Eritrean diaspora apps found are dating apps: Jebena 1,737 ratings, Konjo 1,108, Gojo 398; a classifieds app (Menehariya) has 23; an Ethiopian calendar app has 418; an Amharic Bible app has 9,556 — [Jebena](https://apps.apple.com/us/app/jebena/id1497800659); [Gojo](https://apps.apple.com/us/app/gojo-ethiopian-dating-app/id6473385940); [Menehariya](https://apps.apple.com/us/app/menehariya-classified-ads/id6446753677); [Ethiopian Calendar](https://apps.apple.com/us/app/ethiopian-calendar-holidays/id1588675742)

Community size
- About 356,000 people in the US are Ethiopia-born or have an Ethiopia-born parent (figure traces to a 2014 MPI report, dated); about 39,000 Eritrea-born on 2015 data (weak sources) (snippets) — [EBSCO Research Starters](https://www.ebsco.com/research-starters/social-sciences-and-humanities/ethiopian-immigrants); [Wikipedia](https://en.wikipedia.com/wiki/Ethiopian-American)
- DC-area community estimates of 150,000 to 250,000 are unofficial (snippet) — [Wikipedia](https://en.wikipedia.com/wiki/Ethiopian-American)

Home care
- Washington requires electronic visit verification for home care; vendors include Alora, HHAeXchange and myEZcare (vendor pages) (snippet) — [Alora](https://www.alorahealth.com/washington-medicaid-evv/)
- Agency scheduling platforms are priced around $200 to $500/month for very small teams and $1,500 to $4,000 for 5 to 50 caregivers (vendor estimate) (snippet) — [ShiftCare](https://shiftcare.com/us/blog/scheduling-software-for-healthcare-in-2026-what-home-care-agencies-really-need)
- Caregiver-facing EVV apps are poorly rated: HHAeXchange 3.12 stars (2,237 ratings); California's IHSS EVV app 2.46 (1,098) — [HHAeXchange](https://apps.apple.com/us/app/hhaexchange/id883673336); [IHSS EVV](https://apps.apple.com/us/app/ihss-evv-mobile-app/id1566398156)

Truck drivers (added problem)
- English-language proficiency returned to roadside out-of-service criteria in June 2025 after an executive order; reports cite 6,000 and later more than 7,000 drivers placed out of service, with an industry estimate of about 2,000 a month (snippets) — [FreightWaves](https://www.freightwaves.com/news/more-than-7000-truckers-reportedly-sidelined-for-english-proficiency-violations); [Transport Topics](https://www.ttnews.com/articles/english-proficiency-rule-2026)
- FMCSA finalised a rule in February 2026 barring most foreign drivers from non-domiciled CDLs; FMCSA estimates up to 194,000 holders will exit over five years; DOT says more than 28,000 licences were revoked; litigation is expected (snippets) — [FMCSA](https://www.fmcsa.dot.gov/newsroom/trumps-transportation-secretary-sean-p-duffy-puts-safety-first-finalizes-rule-stop); [DOT fact sheet](https://www.transportation.gov/sites/dot.gov/files/2026-05/FMCSA%20EO%20Fact%20Sheet%20%281%29.pdf)
- App Store searches for "truck driver English proficiency" and "CDL English test ELP" return general CDL permit-test apps (CDL Prep Practice Test Genie 14,535 ratings; CDL Permit 2027 18,167) and generic English apps, with no app dedicated to the roadside English assessment — [CDL Prep Genie](https://apps.apple.com/us/app/cdl-prep-practice-test-genie/id1447415467); [CDL Permit 2027](https://apps.apple.com/us/app/cdl-permit-2027-practice-test/id1566343337)
- Trucker bookkeeping on iOS is thin at the indie end: TruckBooks 11 ratings, IFTA Tracking by FleetCollect 47 — [TruckBooks](https://apps.apple.com/us/app/truckbooks-trucker-expenses/id6767885838); [FleetCollect](https://apps.apple.com/us/app/ifta-tracking-by-fleetcollect/id6755805060)

### Inferences
- Iddir tracking (members, monthly dues, arrears, death benefit payouts, meeting notices, in Amharic or Tigrinya) is the closest fit to the owner's trust edge: one treasurer adopts and brings hundreds of members, and it is tracker-only, so there is no money-transmission exposure. Willingness to pay is unproven, and it sits next to the "church companion" category that was already judged nice-to-have. It needs five to ten treasurer interviews before any build.
- The trucker English-proficiency problem scores highest on "burning": loss of livelihood, a clear deadline (any roadside stop), a practice-style solution (spoken question-and-answer drills, road-sign recognition, in Amharic, Tigrinya, Somali and other languages), no licence needed, and no dedicated iOS competitor found by keyword search. Caveats: the search was keyword-based and may have missed apps; the East African share of truckers is unmeasured; drivers who lose non-domiciled CDLs under the 2026 rule cannot be helped by an app.
- Home care agency software is an enterprise, compliance-bound market (state EVV integration, Medicaid billing) and is unsuitable for a solo developer. The poorly rated caregiver apps are mandated by states or agencies, so a better third-party app cannot replace them.
- Restaurants, groceries and salons are served by Square, Toast, Clover and booking apps; no evidence of a Habesha-specific gap was found, but this was not researched in depth.

### Gaps
- No data on the number of Habesha-owned restaurants, groceries, salons, limo or parking operators, or home care agencies, nor on what software they pay for.
- No data on the number or size of US iddirs or how they keep records today.
- Event and wedding hall booking, catering orders, taxi and limo dispatch, and airport or parking worker needs were not researched.
- Current official totals for drivers placed out of service for English proficiency as of November 2026 were not found; figures above are from trade press at different dates.
- Whether English-proficiency drill apps exist under other names (or on Android only) is unverified.

## 6. Cross-cutting: which problem passes the "burning, already paid for" test, and where could a solo developer win?

### Takeaway
On the evidence gathered, nothing here is both burning and open. Ranked by urgency against competition and licence risk, the most promising are: (a) in-language help around job-loss events (deactivation prevention and appeals outside Washington, trucker English-proficiency drills), (b) a terms-safe, in-language driver "pay and tax check" built on the driver's own data, and (c) a birr rate alert as a free audience builder. Generic mileage tracking, tax filing, money-moving equb and auto-accept tools should be ruled out.

### Cited Findings
- Proof that drivers pay monthly for income tools: Mystro $18.99/month, Gridwise Plus $14.99/month, Solo $10 to $20/month, Everlance $10.99/month — [Mystro](https://apps.apple.com/us/app/mystro-driver-drive-deliver/id1524407919); [Gridwise](https://apps.apple.com/us/app/gridwise-gig-driver-assistant/id1215991382); [Solo](https://apps.apple.com/us/app/solo-your-gig-business-app/id1586902173); [Everlance](https://apps.apple.com/us/app/mileage-tracker-by-everlance/id985378916)
- Proof that the free tier is strong: Stride is fully free with a claimed 2.6 million users — [App Store](https://apps.apple.com/us/app/stride-mileage-tax-tracker/id1041591359)
- Credential-based earnings sync is both a top complaint (logouts, passkey failures, credential unease) and the practice Lyft has threatened deactivation over — [Solo reviews](https://apps.apple.com/us/app/solo-your-gig-business-app/id1586902173); [The Rideshare Guy](https://therideshareguy.com/weekly-roundup-lyft-threatens-driver-deactivation-over-third-party-earnings-apps/)
- Washington now obliges TNCs to provide drivers a downloadable 24-month trip record (from 2026-07-01) — [WA L&I](https://www.lni.wa.gov/workers-rights/industry-specific-requirements/transportation-network-company-drivers-rights/getting-paid)
- Deactivation appeals are conducted in-app and are hard for drivers with English as a second language; outside Washington reinstatement can be as low as about 3.5% (Chicago) — [The American Prospect](https://prospect.org/2026/09/23/rideshare-drivers-want-fair-hearing-before-losing-their-jobs/)
- Language coverage by the state is partial: L&I publishes rights notices in 16 languages and funds "culturally appropriate" services through Drivers Union — [WA L&I](https://www.lni.wa.gov/workers-rights/industry-specific-requirements/transportation-network-company-drivers-rights/)
- Monito already monetises remittance comparison by referral fee and covers USD to ETB — [Monito](https://www.monito.com/send-money/united-states/ethiopia/usd/etb)

### Inferences
Scorecard (judgement based on the findings above; H, M, L = high, medium, low)

| Problem | Urgency | People already pay | iOS competition | Licence or terms risk | Habesha trust or language edge | Verdict |
|---|---|---|---|---|---|---|
| Mileage and expense tracking | M | Yes, but free leader | Very high | Low | Weak | Rule out |
| Auto-accept or multi-app | H | Yes, about $19/month | Medium | High (platform terms, deactivation) | None | Rule out |
| Earnings or minimum-pay check from driver's own data export | M | Indirect | Low for this method | Low | Medium | Worth a prototype, Washington first |
| Deactivation prevention and appeal help | H | Not to apps today | None found | Medium (must not act as legal advice) | High | Strong outside Washington; in Washington, partner with or defer to Drivers Union |
| Tip-deduction and quarterly-tax explainer | M, seasonal | Pay preparers | High for filing, none in-language | Medium (tax advice) | High | Feature or content, not a product |
| Birr rate comparison and alerts | M | No (free elsewhere) | Low in-corridor, Monito generic | Low if licensed providers only | High | Free audience builder; small affiliate income |
| Equb tracker | L to M | No | Many zero-traction apps | Low if tracker-only, high if moving money | High | Weak monetisation |
| Iddir dues tracker | L to M | Unknown | None found | Low | High | Interview treasurers first |
| Trucker English-proficiency drills | H | Unknown | None found by keyword | Low | High if multilingual | Best "burning" candidate; validate audience size |

- A bundle may beat any single feature: one "Habesha driver" app with rights and minimum-pay explainers by city, a deactivation checklist and appeal letter helper, a tip-deduction calculator, quarterly tax reminders and a birr rate widget, all in Amharic and Tigrinya. Each piece alone is thin; together they match what the community asks each other in WhatsApp groups. This is a hypothesis to test, not a finding.
- Distribution would run through channels the incumbents cannot reach: driver WhatsApp and Telegram groups, airport waiting lots, churches, iddirs and community tax preparers. No source measured these channels.
- Pricing anchor: drivers accept $9 to $19/month when the tool visibly raises or protects income. A language-and-trust product with softer value should expect less, likely a low annual price or free with affiliate and referral income.
- App Store risk notes (judgement, not cited rules): avoid collecting Uber or Lyft credentials; avoid showing parallel-market rates; label tax and legal content as information with official citations; do not hold or route funds.

### Gaps
- No direct evidence of willingness to pay from Habesha drivers, truckers, treasurers or senders. Every verdict above needs 10 to 15 short interviews before a build.
- No revenue figures were found for any competitor, so "people pay" rests on price points and ratings counts, not on reported income.
- Android share among the target users is unknown; many auto-accept and equb tools are Android-first, and an iOS-only build may miss part of the community.
- DC, Minneapolis and Denver driver protections (minimum pay, deactivation rights) were not researched; they determine where a deactivation or pay-check tool is most needed.
