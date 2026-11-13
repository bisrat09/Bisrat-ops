# Immigrant paperwork, legal status and licensing tests: burning problems and iOS app coverage (as of 2026-11-13)

Method notes for the report writer:
- All App Store ratings counts, prices, release dates and language lists below were pulled live from Apple's iTunes Search/Lookup API (US storefront) on 2026-11-13. Each app is cited by its App Store URL (`apps.apple.com/us/app/id<ID>`). "Languages" in that API means the app's declared UI localisations; an app can contain translated content without declaring it, so "no Amharic listed" is strong but not absolute proof.
- Ratings counts are lifetime US counts, not downloads or revenue. No Sensor Tower or Appfigures revenue figures were retrieved for any app; all revenue statements are flagged as inference or third-party estimate.
- Several statistics came through secondary sources (law-firm blogs, trade press). Those are flagged. Where a number could not be sourced it is in Gaps, not Findings.

## 1. US citizenship (naturalization) test prep: 2025 civics test, English portion, N-400 interview

### Takeaway
Large, recurring, high-stakes market (roughly 800K to 1M N-400s a year, a harder 128-question test since Oct 2025, denial rate reported to have doubled), but the English-language app shelf is saturated with free or $4 to $20 apps that already include AI mock interviews. The verified gap is language: no iOS app found offers Amharic, Tigrinya or Somali explanations, and the best multilingual competitor covers about 20 languages without them.

### Cited Findings

Size of the problem
- About 818,500 people naturalized in FY2024 (CRS, citing USCIS). — [CRS IF12322, Sept 2025](https://www.everycrsreport.com/files/2025-09-16_IF12322_42b1a898aecd778ae52b06eab04bcc9fc2d453d7.html)
- One secondary source cites 993,120 naturalization applications received in 2024 (different measure from completions). — [Docketwise](https://www.docketwise.com/blog/naturalization-statistics)
- FY2024 top countries of birth: Mexico about 107,700 (13.1 to 13.2%), India about 49,700 (6.1%), Philippines about 41,200 (5.0%), Dominican Republic about 39,900 (4.9%), Vietnam 4.1%. Ethiopia and Eritrea are not in the top 10 visible in these sources. — [Miller Mayer](https://millermayer.com/?p=4059); [Miller Mayer update](https://millermayer.com/?p=18916)
- Diaspora stock: about 304,000 US residents born in Ethiopia and about 45,000 born in Eritrea (MPI tabulation of 2024 ACS; snippet only, the MPI page returned HTTP 403 on fetch). — [MPI, Sub-Saharan African Immigrants in the United States](https://migrationpolicy.org/article/sub-saharan-african-immigrants-united-states)
- A USCIS "Eligible to Naturalize" fact sheet for Washington DC lists Ethiopia first among top countries of birth with 3,940 (undated in the snippet; it counts people eligible to naturalize in the DC area, not completed naturalizations). — [USCIS fact sheet, Washington DC](https://www.USCIS.gov/sites/default/files/document/fact-sheets/Eligible_to_Naturalize_Fact_Sheet_WASHINGTON_DC.pdf)
- About 536,000 naturalization applications were pending as of 2025-03-31; later backlog figures conflict (620,920 for FY2026 Q1 in one source, 647,193 by Feb 2026 in another). — [search summary of USCIS data via Boundless](https://webflow.boundless.com/blog/uscis-q2-fy2025-data); [Immiva](https://immiva.com/blog/n-400-processing-time-2026)

What changed (why urgency went up)
- The 2025 civics test applies to N-400s filed on or after 2025-10-20: 128-question bank (was 100), up to 20 questions asked (was 10), 12 correct to pass (was 6), officer stops at 12 correct or 9 wrong. About 75% of content carries over from the 2008 test. English reading, writing and speaking portions are unchanged. — [Boundless](https://boundless.com/blog/us-announces-major-changes-to-naturalization-civics-test); [Switchboard TA, guidance for service providers](https://www.switchboardta.org/2025-changes-to-the-naturalization-civics-test-what-service-providers-need-to-know/); [CI Law Group explainer](https://cilawgroup.com/news/2025/10/09/explainer-changes-to-the-u-s-naturalization-civics-test-implements-new-2025-standards/)
- One law firm gives Oct 18 rather than Oct 20 as the cutoff; most sources say Oct 20. — [Wolfsdorf](https://wolfsdorf.com/uscis-announces-the-2025-naturalization-civics-test-what-you-need-to-know/)
- NFAP policy brief (July 2026) reports the N-400 denial rate rose from 8.3% to 18.1% between May 2024 and May 2026. This is whole-application denial, not civics-test failure. (Figure from search summary; the PDF body could not be parsed.) — [NFAP, Naturalization Trends, July 2026](https://nfap.com/wp-content/uploads/2026/07/Naturalization-Trends.NFAP-Policy-Brief.July-2026.pdf)
- One law blog reports USCIS decided about 71,000 naturalization applications in April to June 2026 versus about 265,000 in the same period of 2025 (headline: approvals down 75%). Secondary source, unverified against USCIS files. — [Visa Lawyer Blog](https://www.visalawyerblog.com/u-s-citizenship-approvals-drop-75-as-naturalization-delays-increase/)
- Approval rate was about 91.1% in FY2025 Q2 and about 89% in FY2026 Q1 per law-firm summaries of USCIS quarterly data. This conflicts in level with the NFAP 18.1% denial figure for May 2026 (different periods and methods). — [Boundless Q2 FY2025](https://webflow.boundless.com/blog/uscis-q2-fy2025-data); [Manifest Law](https://manifestlaw.com/blog/n400-approval-rate)
- Older, pre-2025-test figure of about 94.4% of applicants passing the test circulates on prep sites; it likely predates the new test. — [CitizenPath](https://citizenpath.com/us-citizenship-test-interview-preparation/)

What people pay today
- N-400 filing fee: $760 paper, $710 online. A June 2026 proposed rule would raise these to $1,330 and $1,280 and eliminate the reduced-fee option and fee waivers for naturalization forms; still a proposal at the time of the sources. (From search summary; confirm on Federal Register.) — [Newsweek](https://www.newsweek.com/why-fewer-green-card-holders-could-become-us-citizens-12175364); [South Asian Herald](https://southasianherald.com/naturalization-path-grows-steeper-as-denials-and-delays-surge/)
- CitizenPath's citizenship (N-400) preparation package is reported at $199 (figure from a competitor's comparison page, unverified). — [Immiva](https://immiva.com/blog/boundless-alternatives)
- An Arabic-translation citizenship app is sold at $12.99 upfront, but has only 5 ratings and was last updated 2022-10-24. — [Arabic US Citizenship Test](https://apps.apple.com/us/app/id1571047429)

Top iOS apps (iTunes API, 2026-11-13)
- US Citizenship Test 2026 Plus (Creator Factory LLC): 104,311 ratings, 4.78, free download; description still describes the 100-question, 6-of-10 test. — [App Store](https://apps.apple.com/us/app/id1103037173)
- Citizen Now: US Citizenship (Liontude LLC): 65,882 ratings, 4.86, free download, UI English only; covers both 100 and 128 question sets; has an "AI Civics Simulator" with real-time feedback on spoken answers, plus CarPlay audio. — [App Store](https://apps.apple.com/us/app/id1492938869)
- Citizen Now in-app purchases: Monthly Premium Access $3.99, Citizen Now Premium $19.99. — [AppPricingLab](https://apppricinglab.com/app/apple/1492938869)
- US Citizenship Test 2026 (Wei Zhang): 17,874 ratings, 4.88, free, English. — [App Store](https://apps.apple.com/us/app/id1045754771)
- USCIS Civics Test App, branded "Citizenry" (Jennifer Brisbane): 13,619 ratings, 4.86, free download, first released 2023-08-17, updated 2026-11-05. Localised into AR, BN, EN, FR, GU, HT, HI, IT, JA, KO, PL, PT, RU, ZH, ES, TH, TR, UK, UR, VI. Claims to be "the only" prep app with realistic N-400 mock interviews in both English and Spanish, with speech recognition and adjustable interviewer speed; covers all 128 questions. No Amharic, Tigrinya, Somali or Dari/Farsi listed. — [App Store](https://apps.apple.com/us/app/id6451455299)
- U.S. Citizenship Test '26 (Purple Buttons LLC): 11,378 ratings, 4.77. — [App Store](https://apps.apple.com/us/app/id422709270)
- US Citizenship Test 2026 Plus. (Swetha Muktala): 5,608 ratings, EN and ES. — [App Store](https://apps.apple.com/us/app/id1623034493)
- Citizen Test Prep 2026 (MastrAPI Ltd): 3,590 ratings. — [App Store](https://apps.apple.com/us/app/id1556996704)
- New solo entrants are still launching: "US Citizenship Test: N400 Prep" (Citizen Pass, Yaniv Navot) launched 2026-03-05 with a "study coach", has 9 ratings after 8 months. "US Citizenship Test 2025" (GETBOKS) has 89 ratings. — [Citizen Pass](https://apps.apple.com/us/app/id6759070713); [GETBOKS](https://apps.apple.com/us/app/id6742466452)
- Creator-led niche example: "US Citizenship with Ameer Ali" (AR, EN, ES; launched 2025-08-05; 70 ratings) sells eBooks with audio narration and translations inside the app and cross-sells DMV permit and CDL prep. — [App Store](https://apps.apple.com/us/app/id6749251462)
- The largest USCIS case tracker bundles a free civics quiz: Case Tracker for USCIS & NVC (Immivision), 320,576 ratings, "trusted by over 2 million users". — [App Store](https://apps.apple.com/us/app/id921827126)

Language gap evidence
- App Store searches for "citizenship test amharic", "citizenship test tigrinya", "citizenship amharic" and "citizenship test somali" returned only the generic English apps above (plus Amharic keyboards); no app with Amharic, Tigrinya or Somali citizenship content appeared. — [iTunes Search API, term "citizenship test amharic"](https://itunes.apple.com/search?term=citizenship+test+amharic&entity=software&country=us); [term "citizenship test tigrinya"](https://itunes.apple.com/search?term=citizenship+test+tigrinya&entity=software&country=us)
- Existing Habesha-language apps on the US store are dictionaries, keyboards and language learners with small ratings counts (Kal Keyboard Amharic 8,216; Best Tigrinya Dictionary 525; Tigrinya AI Chat 95; LomiSpeak Tigrinya & Amharic 26), none targeting tests or paperwork. — [Kal Keyboard](https://apps.apple.com/us/app/id1125783830); [Tigrinya AI](https://apps.apple.com/us/app/id1479328623); [LomiSpeak](https://apps.apple.com/us/app/id6768473172)

### Inferences
- The test itself must be taken in English (unless an age/residency exemption applies), so the product is not "the test in Amharic" but "learn the English answers with Amharic/Tigrinya explanations, audio and a mock officer". That is exactly what the Arabic and Spanish niche apps do; nobody does it for Habesha languages.
- Price ceiling is set by Citizen Now: $3.99/month or $19.99 one-time. A native-language version could plausibly charge $9.99 to $19.99 one-time (the stakes are a $710 to $760 fee, possibly $1,280+ if the proposed rule is finalised, plus months of delay on failure), but not much more without a human-class component.
- Addressable Habesha volume is small. If Ethiopia + Eritrea are outside the top 10 and the stock is about 350K foreign-born, annual Habesha naturalizations are likely in the low tens of thousands at most; a realistic paying base is a few thousand a year. This is a wedge with strong trust and word-of-mouth, not a large standalone business, unless the same engine is localised (Somali, Dari, Haitian Creole, Vietnamese, Arabic).
- Mock-interview AI is no longer a differentiator on its own (Citizen Now and Citizenry both have it); it is table stakes. The differentiator is the explanation language and community distribution (churches, Ethiopian Community in Seattle, YouTube/TikTok in Amharic).
- The sharp fall in decisions in 2026 (if the 71K vs 265K figure holds) cuts both ways: fewer interviews near-term, but higher fear and higher willingness to over-prepare.

### Gaps
- Exact annual naturalizations of people born in Ethiopia and Eritrea: not found. The USCIS FY2024 naturalization statistics page and DHS Yearbook Table 21 would have it; the MPI data tool has a country download. MPI returned 403.
- Official USCIS full-year FY2025 naturalization totals: one source says not yet published as of July 2026.
- Pass/fail rate on the 2025 civics test specifically: no data found.
- Revenue or download estimates for Citizen Now, Citizenry or Creator Factory: none retrieved (Sensor Tower/Appfigures not accessed).
- Price of community citizenship classes and attorney N-400 fees: no reliable source found.
- Whether any Android-only or YouTube-only Amharic citizenship product exists (YouTube channels likely do; not checked).
- How many Habesha applicants qualify for the 50/20, 55/15 or 65/20 exemptions that allow the civics test in their own language with an interpreter: not researched; this group would need native-language civics content directly.

## 2. "Explain this letter": photograph official mail and get a plain explanation in the user's language

### Takeaway
The need is real and recurring, but it is already solved for free by general AI assistants and Google Translate/Lens, and every dedicated iOS app found has essentially zero traction (0 to 33 ratings). No evidence that people pay for this as a standalone app; it is better as a feature inside a paid product than as the product.

### Cited Findings
- BriefAI: Scan Official Letters (solo developer Adem Cilgin): launched 2026-06-08, 1 rating; pitch names IRS, USCIS and courts; outputs plain-English summary, deadline detection, step-by-step action plan. UI English only. — [App Store](https://apps.apple.com/us/app/id6757674090)
- xPlainly: Decode Letters (Martin Hesse): launched 2026-05-06, 0 US ratings; German-bureaucracy focus (Jobcenter, tax office), "22 languages", states it is powered by Claude, drafts a reply. — [App Store](https://apps.apple.com/us/app/id6764679503)
- Postera (Rauf Ismayilov): launched 2026-06-04, 0 ratings; explains German official letters in 16 languages. — [App Store](https://apps.apple.com/us/app/id6758720729)
- ExplainThisDoc (Julian Heger): launched 2026-03-05, 0 US ratings; 24 UI languages; monetises with per-analysis credits, no subscription. — [App Store](https://apps.apple.com/us/app/id6758530963)
- ExplainMyLetter - AI Mail (Shamil Kerimov): 0 ratings; AR, EN, DE, RU, ES, TR. — [App Store](https://apps.apple.com/us/app/id6758314545)
- WhatSays: AI Explain, Translate (Apphi): launched 2023-04-03, 33 ratings, last updated 2024-07-15. — [App Store](https://apps.apple.com/us/app/id6446993803)
- Totoy (Austrian AI document explainer), Explicame and Letterbeaver appear in web search but returned no result in the US App Store lookup on 2026-11-13 (not available in the US storefront, or removed). — [Totoy listing, non-US storefront](https://apps.apple.com/py/app/totoy-ai-document-explainer/id6451316814?l=en-GB); [Letterbeaver, Oman storefront](https://apps.apple.com/om/app/letterbeaver/id6499440027)
- General scanner/translator apps with large installed bases already sit on this use case: OneDocs Scanner Translator 105,629 ratings; Scanner (Luni) 223,500 ratings. — [OneDocs](https://apps.apple.com/us/app/id1441227627); [Luni Scanner](https://apps.apple.com/us/app/id1291962681)
- App Store risk (secondary source, a developer blog, not Apple's text): Apple and Google reject apps that provide medical diagnoses, legal advice or specific investment recommendations without appropriate disclaimers and, in some cases, professional licensing documentation; recommended practice is to scope AI output to information and education and put a disclaimer next to the output. — [dev.to, App Store rejection playbook 2026](https://dev.to/alichherawalla/enterprise-app-store-rejection-playbook-how-to-ship-ai-features-without-getting-blocked-in-2026-17ko)
- A compliance tracker reports Apple restructured and expanded the App Review Guidelines in a revision dated 2026-10-16, and summarises a requirement that AI-generated content be clearly indicated; the tracker also records a provision that "regulated and sensitive apps must be submitted by legal entities". Exact current wording not verified at developer.apple.com. — [ConductAtlas change record](https://conductatlas.com/change/2026-10-17-apple-apple-app-store-review-guidelines-5687/); [ConductAtlas provision record](https://conductatlas.com/platform/apple/apple-app-store-review-guidelines/provision/CA-P-019068/regulated-and-sensitive-apps-must-be-submitted-by-legal-entities/)

### Inferences
- Five or more solo developers shipped the same "snap a letter" idea in 2026 and none shows traction in the US store. The idea is easy to build and hard to distribute; search demand for "explain letter" appears low because people already reach for ChatGPT/Claude/Gemini or Google Translate camera.
- The one unserved angle is output quality in Amharic and especially Tigrinya, where general models and Google Translate are weaker, plus spoken (audio) explanations for users with low literacy. That is a feature-level advantage, not a defensible product.
- Liability is the highest of the five candidates: a wrong deadline on a USCIS RFE, court notice or eviction letter causes real harm. Explaining "what this letter says" is information; telling the user "what you should file" drifts toward unauthorised practice of law. A safe design summarises, extracts dates, and routes to an accredited representative or legal aid; it does not recommend legal strategy.
- Per-letter credits (ExplainThisDoc model) fit sporadic usage better than subscriptions; expect low willingness to pay ($0.99 to $2.99 per letter or bundled free inside another app).
- Best use for this owner: a free trust-building feature inside a paid test-prep app, or a lead-in for referrals, not the paid core.

### Gaps
- No data found on how many LEP households receive and misunderstand official mail per year.
- Apple's own current guideline text on legal/medical information apps was not read directly; the guideline numbers quoted by blogs are unverified.
- No state-bar opinion on AI document-explanation tools and unauthorised practice of law was retrieved; this needs a specific search (Washington State Bar, and the Washington "notario" consumer-protection statute) before building.
- Actual Amharic/Tigrinya quality of ChatGPT, Gemini, Claude and Google Lens on scanned US government letters was not tested.
- Google Translate/Lens current language coverage for Tigrinya camera translation was not verified in this round.

## 3. Driver knowledge test and CDL permit/English prep in languages DMVs do not support well

### Takeaway
This is the strongest candidate found. Washington State (the owner's home market) does not offer the driver knowledge test in Amharic, Tigrinya or Somali; no iOS DMV app serves those languages; and since mid-2025 federal English-proficiency enforcement has put more than 26,000 commercial drivers out of service, with CDL testing moving to English-only. Livelihood is at stake, and a comparable niche app (NYC TLC exam prep) sells at $29.99 upfront with 2,687 ratings.

### Cited Findings

Which states offer Amharic or Tigrinya
- Washington DOL: knowledge test available in 12 languages: English, Spanish, Traditional Chinese, Korean, Russian, Vietnamese, Japanese, Arabic, Simplified Chinese, Punjabi, Tagalog, Ukrainian. No Amharic, Tigrinya or Somali. Online practice test only in English and Spanish. The page tells applicants to check that their driver training school offers the test in the language they need. — [WA DOL, Do I need to take a test?](https://dol.wa.gov/node/254)
- The WA DOL website itself is published in Amharic, Somali and Tigrinya versions, which shows the state recognises these as significant language communities even though the test is not offered in them. — [WA DOL Amharic site](https://dol.wa.gov/am/node/184)
- A Washington third-party driving school advertises the knowledge test "in several languages, including Amharic, with a translator" (unconfirmed by DOL). — [BeSafe Drivers Ed](https://sites.google.com/besafedriversed.org/besafe-drivers-ed/services/knowledge-test)
- Virginia DMV: driver, CDL and motorcycle knowledge exams offered in English, ASL, Amharic, Arabic, Chinese/Mandarin, Dari/Farsi, French, German, Haitian Creole, Italian, Korean, Mongolian, Nepali, Pashto, Punjabi, Russian, Spanish, Turkish, Urdu, Vietnamese. Tigrinya not listed. CDL HAZMAT is English only. — [Virginia DMV](https://transactions-t.dmv.virginia.gov/drivers/know_lang.asp)
- Maryland MVA: non-commercial learner's permit test expanded to 17 languages in 2024, including Amharic. — [Maryland MVA](https://mva.maryland.gov/news/maryland-learners-permit-exam-now-available-17-languages-including-american-sign-language); [MVA bulletin](https://mva.maryland.gov/your-mva-guide/businesses/bulletins-businesses/additional-languages-added-learners-permit-knowledge-test)
- DC DMV: non-commercial knowledge test in 15 languages including Amharic; online practice test also in Amharic (release undated). — [DC DMV](https://dmv.dc.gov/release/district-dmv-offers-driver-knowledge-test-15-languages)
- No source found showing any US state offering the knowledge test in Tigrinya. — [Virginia DMV list](https://transactions-t.dmv.virginia.gov/drivers/know_lang.asp); [WA DOL list](https://dol.wa.gov/node/254)

Federal English-proficiency (ELP) enforcement for commercial drivers
- FMCSA issued new enforcement instructions in May 2025; CVSA made ELP non-compliance an out-of-service condition effective 2025-06-25. The roadside check has two parts: conversational English and reading English highway signs. — [Transport Topics](https://www.ttnews.com/articles/english-proficiency-rule-2026); [HDT/Truckinginfo](https://www.truckinginfo.com/articles/when-language-stops-the-truck-the-return-of-elp-out-of-service-orders)
- DOT says more than 26,000 commercial drivers have been placed out of service for ELP since strict enforcement resumed (cumulative, as of about Aug 2026). — [FreightWaves](https://freightwaves.com/news/after-sidelining-26000-truck-drivers-fmcsa-seeks-to-lock-in-english-rules); [Washington Examiner](https://washingtonexaminer.com/policy/immigration/4678834/sean-duffy-codify-english-proficiency-truckers-transportation)
- An ATA vice president put the pace at about 2,000 drivers sidelined a month. — [Transport Topics](https://www.ttnews.com/articles/english-proficiency-rule-2026)
- Baseline: in 2024 there were about 10,000 ELP violations and no drivers placed out of service, per Secretary Duffy. — [HDT/Truckinginfo](https://www.truckinginfo.com/10241165/transportation-secretary-promises-to-go-after-bad-actors-in-trucking)
- On 2026-08-10 FMCSA published a proposed rule (91 FR 51422) to codify ELP as an out-of-service violation. — [J. J. Keller](https://jjkellercompliancenetwork.com/regsense/91-fr-51422-english-language-proficiency-out-of-service-criteria); [FMCSA newsroom](https://www.fmcsa.dot.gov/newsroom/trumps-transportation-secretary-sean-p-duffy-moves-codify-english-proficiency-requirements)
- A FreightWaves headline estimates the ELP rule "threatens 10% of truckers" (body not retrieved; treat as a headline claim). — [FreightWaves](https://www.freightwaves.com/news/elp-rule-threatens-10-of-truckers-risks-carrier-csa-scores)
- CDL tests moving to English only: on 2026-02-20 Secretary Duffy announced that all truck and bus drivers will be required to take CDL tests in English (federal rulemaking). — [Anchorage Daily News / wire](https://www.adn.com/nation-world/2026/02/20/all-truckers-and-bus-drivers-will-be-required-to-take-commercial-drivers-license-tests-in-english/)
- Texas DPS made all CDL and commercial learner permit knowledge exams English-only effective 2026-06-01, with interpreters prohibited. — [Texas DPS](https://www.dps.texas.gov/news/dps-announces-changes-cdl-knowledge-testing); [Texas Tribune](https://www.texastribune.org/2026/06/01/texas-commercial-drivers-license-testing-english-only/)
- Florida: from 2026-02-06 all driver licence knowledge and skills exams (not only CDL) are English-only, translation services not permitted (from search summary of trade press). — [CDLLife](https://cdllife.com/2026/texas-mandates-that-all-cdl-knowledge-testing-must-be-administered-in-english/)
- The Department of Labor has also moved to extend English-proficiency requirements to foreign commercial truck drivers. — [Safety+Health Magazine](https://www.safetyandhealthmagazine.com/dol-extends-english-proficiency-requirement-to-all-commercial-truck-drivers/)

Top iOS apps (iTunes API, 2026-11-13)
- Zutobi: Permit & Driving Prep: 239,138 ratings; EN, FR, DE, SV. — [App Store](https://apps.apple.com/us/app/id1394069110)
- DMV Genie: Permit Test 2026 (Elegant eLearning): 184,449 ratings, English only; claims 9 million drivers and a pass guarantee. — [App Store](https://apps.apple.com/us/app/id513850893)
- DMV WRITTEN TEST (Infinity Loop Capital): 138,168 ratings; EN, ES. — [App Store](https://apps.apple.com/us/app/id1497421016)
- DMV Practice Test 2026 myDMV (KAIN SUITE): 113,926 ratings; English, Spanish, Chinese, Vietnamese, Hindi. The broadest language set among large DMV apps; no African or Middle Eastern languages. — [App Store](https://apps.apple.com/us/app/id1625234008)
- CDL Test Prep 2026 Class A B (Hanh Le): 48,906 ratings, 4.9; EN, ES; "most-reviewed dedicated CDL prep app". — [App Store](https://apps.apple.com/us/app/id1527903479)
- CDL Exam Prep 2026 (Easy Pass): 27,621 ratings. CDL Permit 2027 (Mapola): 18,167. CDL Prep Test 2026 (Wei Zhang): 15,419. CDL Prep Genie: 14,535. — [Easy Pass](https://apps.apple.com/us/app/id1469003902); [Mapola](https://apps.apple.com/us/app/id1566343337); [Wei Zhang](https://apps.apple.com/us/app/id1464409838); [CDL Genie](https://apps.apple.com/us/app/id1447415467)
- CDL Help: CDL Prep Test 2026 (TruckDriver.help LLC): 5,413 ratings, 4.87; localised into AR, EN, KO, PT, RU, ZH, ES, TR, UK, UZ. This is the closest "immigrant-language CDL prep" competitor and proves the model; it has no Amharic, Tigrinya, Somali or Punjabi. — [App Store](https://apps.apple.com/us/app/id6444388755)
- Trucker-English apps are brand new and tiny: TruckSpeak: Trucker English (0 ratings, updated 2026-10-19), Trucker English by Interstate Logistics Services (1 rating, 2026-10-28), Lingo Truck: CDL English (7 ratings). — [TruckSpeak](https://apps.apple.com/us/app/id6822367936); [Trucker English](https://apps.apple.com/us/app/id6807656745); [Lingo Truck](https://apps.apple.com/us/app/id6756713641)
- Price benchmark for a livelihood licence niche: TLC Practice Exam 2.0 (NYC taxi/for-hire driver exam) is a $29.99 paid-upfront app with 2,687 ratings, 4.67, "study support in 8 languages" (UI in EN, ES, UR), launched 2023-05-26. — [App Store](https://apps.apple.com/us/app/id6447449111)
- App Store searches for "dmv permit test amharic", "amharic driving test" and "DMV test somali" returned no app with Amharic or Somali content. — [iTunes Search API, term "amharic driving test"](https://itunes.apple.com/search?term=amharic+driving+test&entity=software&country=us)

### Inferences
- Two distinct products sit here. (a) Regular driver's licence knowledge test with Amharic/Tigrinya explanations, most valuable in states that do NOT offer an Amharic test (Washington confirmed; Tigrinya appears unsupported everywhere). In WA the applicant must sit the test in English or one of 11 other languages, so bilingual prep (English question, native-language explanation, audio) is the precise need. (b) CDL permit prep plus "roadside English" drills (conversation with an inspector, reading signs), now forced into English by federal policy.
- The CDL/ELP segment has the clearest "hair on fire" signal in this file: a new enforcement regime, about 2,000 drivers a month losing the ability to work, tests switching to English-only, and incumbent English-practice apps with 0 to 7 ratings (all launched in the last few months). It is early, and nobody has won it.
- TLC Practice Exam's $29.99 upfront price with 2,687 ratings implies a floor of roughly $80K gross lifetime if every rater paid that price (ratings are a fraction of buyers; price history unknown). That is direct evidence drivers pay $30 for a licence-gating exam app with multilingual support.
- Plausible pricing for a solo developer: $14.99 to $29.99 one-time or about $9.99/month for CDL + roadside English; $7.99 to $14.99 one-time for the regular permit test. Truck drivers have income and an employer-driven deadline; teenagers and new arrivals taking the car test are more price sensitive and have free alternatives.
- Habesha fit is strong: trucking, rideshare and for-hire driving are common diaspora occupations (not sourced in this round; see Gaps), and the owner's Seattle base matches the state with the confirmed language hole.
- Risk: content must be state-specific and kept current; a pass guarantee creates refund exposure; ELP policy could be reversed by a future administration or court, which would deflate the CDL-English segment. No legal-advice exposure, and App Store risk is low (standard education category).
- Discovery: high-intent search terms exist ("DMV test Amharic", "CDL English test", "ELP test truck driver"), plus distribution through trucking schools, Habesha Facebook/Telegram trucker groups, and YouTube explainers in Amharic/Tigrinya.

### Gaps
- Minnesota, California, Colorado, Georgia and Texas non-commercial knowledge-test language lists: not confirmed in this round (searches returned no official pages). Needs direct checks of MN DVS, CA DMV, CO DMV, GA DDS, TX DPS.
- Whether Washington allows interpreters for the knowledge test officially: DOL page is silent; only a driving school claim was found.
- Number of Ethiopian/Eritrean-born commercial or rideshare drivers in the US, and how many of the 26,000 out-of-service drivers speak Amharic/Tigrinya/Somali: no data found. Trade coverage focuses on Spanish and Punjabi speakers.
- Knowledge-test failure rates by language in Washington: not found.
- Revenue estimates for DMV Genie, Zutobi, CDL Prep apps: not retrieved.
- Prices of in-person ELP/CDL English courses: search returned nothing usable.
- Official FMCSA monthly ELP out-of-service counts: only DOT cumulative claims and vendor-blog figures (for example 18,062 violations and 3,724 OOS in 2026, about 500 OOS in a three-day January 2026 operation, both from a vendor blog) were found. — [Oxmaint vendor blog](https://oxmaint.com/industries/fleet-management/fmcsa-elp-enforcement-2026-driver-roadside-inspections-oos-rule)

## 4. Immigration form help and case tracking (DV lottery, asylum, TPS, family petitions)

### Takeaway
Urgent and money is clearly spent here, but the category is dominated by venture-backed players with hundreds of thousands of ratings, and form preparation carries the heaviest unauthorised-practice-of-law exposure. Not a sensible solo-developer entry point except for narrow, low-liability utilities (for example DV entry guidance in Amharic), which are seasonal and low value.

### Cited Findings
- Case Tracker for USCIS & NVC (Immivision): 320,576 ratings, 4.82; EN, FR, HT, ES; "trusted by over 2 million users"; on the store since 2014. — [App Store](https://apps.apple.com/us/app/id921827126)
- MigraConnect Case Tracker (Tecso Solutions): about 202,000 ratings, 4.84, launched only 2024-08-13; adds immigration court (EOIR) tracking, asylum clock, FOIA status, judge asylum statistics. Shows a new entrant can still scale fast with a sharper feature set. — [App Store](https://apps.apple.com/us/app/id6596770726)
- Lawfully USCIS Case Tracker: 174,133 ratings, 4.81; "6M+ cases registered"; content in English, Spanish, French, Russian, Korean, Chinese. — [App Store](https://apps.apple.com/us/app/id1435063223)
- Lawfully in-app purchases range from $14.99 to $39.99 (10 IAPs listed). — [AppPricingLab](https://apppricinglab.com/app/apple/1435063223)
- Lawfully funding figures conflict: $2.5M seed (2022, Law360), $5.05M total (CB Insights). Company reports 6 million registered cases and 3 million downloads as of Sept 2025. — [Law360](https://law360.com/pulse/articles/1545873); [CB Insights](https://www.cbinsights.com/company/lawfully-1/financials); [Lawfully about page](https://www.lawfully.com/about/)
- Third-party estimate puts Lawfully's Android app at under $10K monthly revenue from IAP and ads; a lead-data site lists $3M annual revenue. Both unverified and mutually inconsistent. — [AppGoblin](https://appgoblin.info/apps/com.lawfully.lawfully_ai_tracker); [Prospeo](https://prospeo.io/c/lawfully)
- Inmigreat: USCIS Case Tracker: 13,049 ratings; EN, PT, ES. Case Tracker for USCIS Status (Kevin Horvath): 21,723 ratings. — [Inmigreat](https://apps.apple.com/us/app/id6450058436); [Horvath](https://apps.apple.com/us/app/id1585545181)
- Boundless pricing (from a competitor's comparison page, unverified): $899 Essential, $1,549 Premium for family-based adjustment. A pricing tracker shows monthly instalment plans from about $73/month and an approximately 8% instalment price increase in Sept 2026. — [Immiva](https://immiva.com/blog/boundless-alternatives); [PricingSaaS](https://pricingsaas.com/companies/boundless)
- CitizenPath pricing (same competitor page, unverified): $199 citizenship, $139 removal of conditions, $279 adjustment (I-864 separate). — [Immiva](https://immiva.com/blog/boundless-alternatives)
- DV lottery: a final rule published 2025-09-16 added a $1 non-refundable electronic registration fee per entry, on top of the $330 fee paid by selectees; no waivers. — [Mshale](https://mshale.com/2025/09/19/green-card-lottery-entry-no-longer-free-as-1-fee-goes-into-effect/); [Camp Legal](https://camplegal.com/understanding-the-dv-2027-lotterys-new-1-electronic-registration-fee/)
- DV passport rule: a State Department final rule effective 2026-04-10 requires entrants to provide valid passport information and upload scans of the biographic and signature pages, applying to DV-2027; State delayed the DV-2027 opening because of it. Sources conflict on timing (an earlier statement said the passport rule would not be implemented that year). — [JD Supra](https://www.jdsupra.com/legalnews/diversity-immigrant-visa-program-update-3587890/); [Ada Derana](https://www.adaderana.lk/news/113746/us-state-department-confirms-dv-2027-delay-and-new-1-registration-fee)
- DV photo/entry helper apps on iOS have negligible traction: Green Card Photo - DV Photo (14 ratings), DV Lottery 2027 Photo Editor (0), DV Photo Tool: 2027 Lottery (0; localised to AR, FA, RU, UZ, TR and others). — [SNAP FLOW](https://apps.apple.com/us/app/id6751569555); [DV Photo Tool](https://apps.apple.com/us/app/id6756299301)

### Inferences
- Case tracking is a solved, free, ad/IAP-supported commodity with three apps above 170K ratings; a Habesha-language tracker would add little because status strings are short and already machine-translatable.
- Form preparation is where the money is ($139 to $1,549 per application), but it requires legal review processes, attorney networks and UPL-safe design that a solo developer cannot credibly staff. In Washington and many states, non-lawyer "immigration assistant/notario" activity is specifically regulated (not sourced here; see Gaps).
- The DV lottery is culturally huge for Ethiopians and Eritreans, and the new passport-scan requirement raises entry friction, but DV entrants are mostly abroad (not US iOS users), entry is once a year, and the fee is $1. Diaspora members entering relatives is a real behaviour but a thin, seasonal monetisation base. Existing DV photo apps show almost no ratings.
- A defensible adjacent idea is content, not filing: Amharic/Tigrinya "what this USCIS status means" explainers bundled into the citizenship app as retention content.

### Gaps
- Boundless, CitizenPath and SimpleCitizen prices were not verified on the companies' own pricing pages; SimpleCitizen pricing was not found at all.
- No verified revenue for any of these companies.
- DV-2027 registration window dates and whether it has closed as of 2026-11-13: not established (one headline points to selection/registration activity on 2026-03-11, body not retrieved). — [National Law Review](https://natlawreview.com/article/diversity-visa-lottery-selection-opens-march-11-2026)
- Number of DV entrants and selectees from Ethiopia and Eritrea: not retrieved in this round.
- TPS/asylum populations for Ethiopia and Eritrea and current TPS status for Ethiopia: not researched.
- Notario fraud losses and typical notario fees: search returned nothing; FTC and state AG reports would be the source.
- State rules on non-lawyer immigration form assistance (for example Washington's immigration services fraud statute): not retrieved.

## 5. Professional licensing and job-entry exams (CNA, NCLEX for foreign-trained nurses, security guard, food handler, taxi/for-hire)

### Takeaway
Foreign-trained nurses failing NCLEX is a documented, expensive pain (about 47% first-time pass versus about 87% for US graduates) but the prep market is owned by well-funded incumbents; CNA, home-care aide, security guard and for-hire licence prep are lightly served on iOS and have real language-barrier evidence in Washington State, making them good second modules for a multilingual test-prep engine rather than a first product.

### Cited Findings
- NCLEX-RN 2025: first-time internationally educated candidates passed at about 47.3%; repeat internationally educated at about 30.5%; first-time US-educated at about 86.7% (167,272 of 192,916). Philippines-educated first-timers 45.8% (22,793 tested); India-educated 33.3% (4,866 tested). Secondary sites citing NCSBN; Kaplan lists 51.6% for first-time internationally educated, a conflict. — [NCSBN 2025 exam statistics](https://ncsbn.org/public-files/2025_NCLEXExamStats_Final.pdf); [GoodNurse summary](https://goodnurse.com/article/278/nclex-pass-rates-for-internationally-educated-nurses-2026-official-data-by-country); [Kaplan](https://www.kaptest.com/study/nclex/nclex-pass-rates-what-you-need-to-know/)
- NCLEX iOS incumbents: NCLEX RN Mastery (Higher Learning Technologies) 31,410 ratings; Archer Review NCLEX 22,805; Saunders Comprehensive Review 12,618; UWorld Nursing 2,112 (most usage is web). All English. — [NCLEX RN Mastery](https://apps.apple.com/us/app/id625614526); [Archer](https://apps.apple.com/us/app/id1492019618); [Saunders](https://apps.apple.com/us/app/id1328853613); [UWorld](https://apps.apple.com/us/app/id979446488)
- CNA prep on iOS is thin and English-only: CNA Practice Test 2026 Prep (Easy Pass) 2,265 ratings; CNA Practice Exam Genie 1,958; CNA Exam Practice Tests (Prepia) 1,132; others under 400. — [Easy Pass CNA](https://apps.apple.com/us/app/id1502053307); [CNA Genie](https://apps.apple.com/us/app/id1507143940); [Prepia](https://apps.apple.com/us/app/id6736650804)
- One nursing site states the CNA exam is offered only in English across the US; Washington is an exception for its Prometric-administered exam, which lists languages including Russian, Spanish, Ukrainian and Vietnamese, and notes a language barrier is not a disability for accommodation purposes. (The Washington detail appears to concern the home care aide exam.) — [Nurse.org](https://nurse.org/articles/certified-nursing-assistant-exam-spanish-chinese); [Prometric WA bulletin](https://prometric.com/media/3765/download)
- Washington home care aide exam, language-barrier evidence (dated 2018): Somali-language written pass rate was 78.9% in 2017 and 56.6% in 2018; Prometric rewrote the test in 2016 in response to low pass rates among non-English speakers; adding a translation for a new language was quoted at more than $50,000. — [Crosscut, Oct 2018](https://uat1.crosscut.com/2018/10/would-be-home-health-workers-claim-bias-states-qualifying-exam)
- Washington State Auditor found limited access to training and the exam, and language barriers for LEP applicants, were problems for home care aide certification; LEP pass rates improved after the exam was rewritten in simplified language. — [WA State Auditor report](https://www.sao.wa.gov/sites/default/files/audit_reports/ar1018059.pdf)
- Washington law requires annual evaluation of exam results for applicants testing in a language other than English, and a translation review when a language group fails disproportionately (home care aide chapter). — [RCW 18.88B.031](https://lawfilesext.leg.wa.gov/Law/RCWPDF/RCW%20%2018%20%20TITLE/RCW%20%2018%20.%2088B%20CHAPTER/RCW%20%2018%20.%2088B.031.pdf)
- Food handler/ServSafe prep: small and English/Spanish only: ServSafe Practice Test 2026 (EZ Test Prep) 1,948 ratings; ServSafe Practice Test Prep (Best Fun Games) 1,108; Easy Pass 652; dedicated "food handler" apps have 0 ratings. — [EZ Test Prep](https://apps.apple.com/us/app/id6742800006); [Best Fun Games](https://apps.apple.com/us/app/id6745693739); [Food Handler Test Prep 2026](https://apps.apple.com/us/app/id6782296881)
- Security guard licence prep: effectively empty on the US store; results were Canadian-province apps and one "Security Guard License Prep" with 0 ratings, plus an Illinois PERC card app with 0 ratings. — [Security Guard License Prep](https://apps.apple.com/us/app/id6790310508); [Illinois PERC Card](https://apps.apple.com/us/app/id6783681920)
- Taxi/for-hire: TLC Practice Exam 2.0 (NYC only) is $29.99 upfront with 2,687 ratings and multilingual support; no equivalent app surfaced for other cities. — [App Store](https://apps.apple.com/us/app/id6447449111)

### Inferences
- NCLEX for foreign-trained nurses is the most "burning" item in this group by failure rate and money at stake (candidates already pay for UWorld/Archer-class question banks), but the problem is clinical-reasoning English, the content bar is very high, and incumbents are entrenched. Ethiopian/Eritrean-trained nurse volumes are probably small relative to the Philippines and India. Not a solo first product.
- CNA and Washington home-care-aide prep with Amharic/Tigrinya/Somali explanations is a credible module: thin competition (top app about 2,300 ratings), documented LEP failure problem in Washington, and a workforce that Habesha and Somali women enter in large numbers (occupational share not sourced here). Price point likely $9.99 to $19.99 one-time, in line with the entry-level wage.
- Food handler cards are low-stakes (cheap, short, retake-friendly, often already multilingual at the county level); weak willingness to pay.
- Security guard licence prep is an empty shelf but requirements are state-by-state and many states test only after mandated in-person training; demand evidence is missing.
- The reusable asset across sections 1, 3 and 5 is one engine: English question bank + native-language explanation + audio + spoken mock. That supports the owner's "localise later" thesis better than any single test does.

### Gaps
- No current (2024 to 2026) CNA or home care aide pass rates by language were found; the Somali figures are from 2017 to 2018.
- Whether Washington's home care aide or CNA exam is offered in Amharic or Tigrinya: not confirmed.
- Annual number of CNA test-takers nationally and in Washington: not retrieved.
- Number of Ethiopian/Eritrean-educated NCLEX candidates per year: the NCSBN PDF has country tables but was not parsed.
- Seattle/King County for-hire driver licence exam requirements and whether a written test still exists: not researched.
- Prices of incumbent NCLEX subscriptions (UWorld, Archer) and CNA app IAPs: not retrieved in this round.
- Occupational concentration of Ethiopian/Eritrean immigrants (driving, home care, nursing, security, parking): asserted in the brief but not sourced here.

## Cross-cutting: ranking, pricing and distribution

### Takeaway
On the evidence gathered, the ranking for a solo developer with Habesha-community reach is: (1) driver/CDL test prep plus trucker roadside English in Amharic/Tigrinya (new federal pressure, confirmed Washington language gap, proven $30 price point, weak new competitors); (2) citizenship prep with native-language explanations (large and urgent, verified language gap, but price capped near $4/month or $20 one-time by strong incumbents); (3) CNA/home-care-aide prep as a follow-on module; with "explain this letter" as a free feature and immigration forms/tracking avoided.

### Cited Findings
- Verified price points in adjacent apps: Citizen Now $3.99/month or $19.99; Lawfully IAPs $14.99 to $39.99; TLC Practice Exam $29.99 upfront; Arabic citizenship app $12.99 upfront. — [AppPricingLab, Citizen Now](https://apppricinglab.com/app/apple/1492938869); [AppPricingLab, Lawfully](https://apppricinglab.com/app/apple/1435063223); [TLC Practice Exam](https://apps.apple.com/us/app/id6447449111); [Arabic US Citizenship Test](https://apps.apple.com/us/app/id1571047429)
- Multilingual competitors that prove the "immigrant-language test prep" model, and the languages they skip: Citizenry (20 languages, 13,619 ratings; no Amharic, Tigrinya, Somali, Dari); CDL Help (10 languages, 5,413 ratings; no Amharic, Tigrinya, Somali, Punjabi); myDMV (5 languages, 113,926 ratings). — [Citizenry](https://apps.apple.com/us/app/id6451455299); [CDL Help](https://apps.apple.com/us/app/id6444388755); [myDMV](https://apps.apple.com/us/app/id1625234008)
- Washington State does not offer the driver knowledge test in Amharic, Tigrinya or Somali but does publish its DOL website in all three. — [WA DOL test page](https://dol.wa.gov/node/254); [WA DOL Amharic site](https://dol.wa.gov/am/node/184)
- Free official substitutes exist for the core content: USCIS publishes the 2025 civics test study materials; state DOLs publish driver guides and (in WA) English/Spanish practice tests. — [Switchboard TA on USCIS 2025 test resources](https://www.switchboardta.org/2025-changes-to-the-naturalization-civics-test-what-service-providers-need-to-know/); [WA DOL](https://dol.wa.gov/node/254)

### Inferences
- "Already solved for free" applies in English and Spanish for every candidate here. It does not apply in Amharic or Tigrinya for any of them. The whole thesis rests on whether Habesha users will pay for native-language explanation and audio rather than struggle through free English tools; the Arabic, Uzbek/Russian (CDL Help) and Urdu (TLC) niches suggest some will, at $10 to $30.
- Realistic solo pricing: one-time unlocks of $9.99 to $29.99 per test (people study for weeks, then leave; subscriptions churn immediately after the exam). A "pass or refund" guarantee is common in the category (DMV Genie) and matters for trust.
- Distribution should not depend on App Store search, where incumbents hold the English keywords. High-intent native-language terms ("የዜግነት ፈተና", "DMV test Amharic", "CDL in Tigrinya") have no app results today, and the owner's existing Habesha audience, churches, Ethiopian/Eritrean community associations, driving schools and trucking Telegram/Facebook groups are the practical channels. YouTube/TikTok lessons in Amharic can serve as the top of the funnel.
- Legal and App Store risk is lowest for test prep (education), moderate for letter explanation (needs information-not-advice framing, AI labelling, disclaimers), and highest for form preparation.
- Policy dependence: both lead candidates are driven by 2025 to 2026 federal enforcement changes (harder civics test, ELP out-of-service rule, English-only CDL testing). These create urgency now, but could be reversed; the regular driver's licence test in a state with no Amharic option is the most durable part of the demand.

### Gaps
- No direct evidence yet (surveys, Reddit threads, community posts) of Habesha users saying they would pay for these; r/USCIS, r/Truckers and community-group checks were not done in this round.
- No revenue data for any competitor; all market-size statements for the Habesha segment are inference from stock figures (about 304K Ethiopia-born, about 45K Eritrea-born).
- Quality of current LLM output in Tigrinya (text and speech) is unverified and is a build risk for the "localise the engine" plan.
