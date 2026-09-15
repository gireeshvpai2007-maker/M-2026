# 🚗 FellaRide — Product, Research & Testing Notes

**Prepared by:** Deepthi Dongre (Product, Research & Testing Lead)
**Project:** M#2026 Hackathon — Community Activation Platform (FellaFlywheel Engine)

---

## 🆚 Why FellaRide Isn't "Uber for Carpooling"

Before diving into testing, it's worth being clear about what we're actually building — because it's easy to assume FellaRide works like Ola or Uber. It doesn't.

| | Uber / Ola | FellaRide |
|---|---|---|
| Who's driving | Professional/gig driver, paid to drive | A regular commuter already driving that route |
| Relationship | Strangers | People from the same community (colleagues, classmates, neighbors) |
| Why they drive | Income | Splitting cost, company, convenience |
| How you find a ride | Instant request, any driver nearby | Recurring carpool with people you'd already trust |
| Trust | Built via ratings/reviews of strangers | Already exists because you know (or share a community with) them |

**In short:** Uber solves "get me a ride right now." FellaRide solves "help the coworkers/classmates who are already driving the same way find each other." That difference is the whole point of the product — and it's why the early activation strategy (finding the right first few people) matters more here than it would for a typical ride-hailing app.

---

## 🎯 The Core Problem We're Solving

A carpooling app is useless with zero users — no drivers means no rides, no rides means no reason to open the app. FellaRide's bet: instead of chasing mass signups, find the right first few people inside an existing community and help them create the first few real rides. If that works, trust and referrals should carry the growth from there.

My job as Product/Research/Testing lead is to make sure this actually holds up with real people — that the community we pick makes sense, that the AI's suggestions feel helpful rather than invasive, and that what we ship for the hackathon demo actually proves the concept.

---

## 🏫 1. Picking Our First Community

We need one real community to pilot on for the demo — I'd recommend our own college/campus, since we already have access, existing trust, and know the commute patterns firsthand.

| Option | Why it could work | Why it's harder |
|---|---|---|
| Our college campus | We already have access + trust; fastest to test | Smaller scale, may not fully reflect "real" traffic patterns |
| A corporate office | Realistic, recurring commutes | We don't have access or existing relationships there |
| A residential area | Groups (like WhatsApp communities) already exist | Mobility patterns are less predictable, harder to map |

**Recommendation:** Start with campus. It matches the "East Bengaluru → Campus" demo scenario already in the docs, and we can identify real connectors (people in our own friend groups with reach) instead of guessing.

---

## 🚘 2. Making Sure "Driver" Means the Right Thing

As clarified above — in FellaRide, a "Driver" is a regular commuter already making that trip, not a professional or gig driver. This needs to be reflected clearly in the UI copy and onboarding, or people will expect an Uber-style experience and be confused when it's not that.

| Role | What I'll verify during testing |
|---|---|
| Driver | Has a car and already makes this commute — does the "create a recurring ride" prompt feel natural to them, or presumptuous? |
| Passenger | Has a predictable commute — does "request a seat" feel low-friction? |
| Connector | Actually has real reach in the community, not just a big friend list |
| Early Adopter | Genuinely responsive, not just statistically present |

I'll pick 5–10 people I know personally and compare what the system predicts about their role against what I already know to be true — a quick sanity check before we trust the AI's classification more broadly.

---

## 🤖 3. Testing the Activation Score & Messaging

The Activation Score (Community Reach, Route Fit, Role Potential, Responsiveness, Trust) decides who gets targeted first — so it needs to feel *right*, not just mathematically correct. My plan:

- **Sanity-check the score** — compare it against what a human would guess for a few known people
- **Check the "Why?" explanation** — can someone without a technical background actually understand why they were suggested?
- **Stress-test the messaging** — a line like *"3 people in your office commute toward Whitefield"* can land as either genuinely helpful or a little unsettling, depending on tone. I'll draft a few phrasing variants per role and get quick reactions from classmates before we lock in the copy.

---

## 📊 4. What "Working" Looks Like

FellaRide already defines its own success metrics — my job is to actually track them during the pilot:

| Metric | What it tells us |
|---|---|
| Time to First Ride | How fast someone goes from discovery to an actual completed ride |
| Ride Cluster Density | How many rides happen per active community/corridor |
| Repeat Rate | Whether people come back and ride again within a week |
| Referral Propagation | Whether activated users bring in others |

---

## 🔐 5. Keeping It Responsible

FellaRide's own principle is "public signals should create relevance, never surveillance" — so as I test, I'll be watching for:

- Every intervention message has a clear way to opt out
- Messages don't expose more personal detail than necessary to make the point
- Nothing crosses from "helpful suggestion" into "this feels like profiling"

---

## 💬 Open Items for the Team

A couple of things I still need input on before finalizing the test plan:
- Confirming campus as our pilot community (or if there's a better option I'm missing)
- What signals we can realistically access in our timeframe — real data, or a simulated dataset for the demo
- What "done" looks like for the hackathon: a working prototype, or the AI logic plus a strong demo narrative

---
*Living document — I'll update this as FellaFlywheel gets built and we start testing for real.*