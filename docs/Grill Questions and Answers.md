Read memory [](file:///Users/edhwang/Library/Application%20Support/Code/User/workspaceStorage/0afc851e0c02d42e7151d95b98d75837/GitHub.copilot-chat/memory-tool/memories/repo/discovery-workspace-conventions.md)

Read memory [](file:///Users/edhwang/Library/Application%20Support/Code/User/workspaceStorage/0afc851e0c02d42e7151d95b98d75837/GitHub.copilot-chat/memory-tool/memories/repo/credential-recovery.md)

Now let me gather context about the website project — existing WPs, the current site, and any relevant memory files.   

Searched for files matching `**/memory/**website*`, 3 matches

Searched for files matching `**/Memory/**`, 20 matches

Ran terminal command:  source ~/.ste-secrets/.env && AUTH=$(echo -n "apikey:$OPENPROJECTS_COPILOT_API_KEY" | base64) && curl -s "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/projects/6/work_packages?filters=%5B%7B%22status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%5D" -H "Authorization: Basic $AUTH" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for wp in data.get('_embedded',{}).get('elements',[]):
    print(f'OP#{wp["id"]}  [{wp.get("_links",{}).get("status",{}).get("title","")}]  {wp["subject"]}')
"

Read [](file:///Users/edhwang/Discovery/Memory/STE%20-%202026-07-14%20-%20Website%20Design%20Direction.md)

Read [](file:///Users/edhwang/Discovery/Memory/STE%20-%202026-07-14%20-%20Website%20Copy%20Strategy.md)

Read [](file:///Users/edhwang/Discovery/Memory/STE%20-%202026-07-06%20-%20Website%20and%20Tooling%20Issues.md)

Read [](file:///Users/edhwang/Discovery/Memory/STE%20-%202026-07-06%20-%20Content%20Strategy%20and%20Brand%20Positioning.md)

Ran terminal command:  source ~/.ste-secrets/.env && AUTH=$(echo -n "apikey:$OPENPROJECTS_COPILOT_API_KEY" | base64) && curl -s "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/331" -H "Authorization: Basic $AUTH" | python3 -c "
import sys, json
wp = json.load(sys.stdin)
print('Subject:', wp.get('subject',''))
print('Status:', wp.get('_links',{}).get('status',{}).get('title',''))
print('Description:')
print(wp.get('description',{}).get('raw',''))
"

Searched for files matching `**/projects/**website*`, 1 match

Ran terminal command:  source ~/.ste-secrets/.env && AUTH=$(echo -n "apikey:$OPENPROJECTS_COPILOT_API_KEY" | base64) && curl -s "https://ste-business-server.tailebe6d3.ts.net:8080/api/v3/work_packages/274" -H "Authorization: Basic $AUTH" | python3 -c "
import sys, json
wp = json.load(sys.stdin)
print('Subject:', wp.get('subject',''))
print('Description:')
print(wp.get('description',{}).get('raw',''))
"

Read [](file:///Users/edhwang/Discovery/docs/projects/STE-website-community.md#1-1), lines 1 to 120

Read [](file:///Users/edhwang/Discovery/docs/projects/STE-website-community.md#120-120), lines 120 to 180

Good — I have a solid picture of the existing state. Now let me look at the current live site and check the git repo location. 

Ran terminal command:  find ~ -name "*.json" -path "*/smoking*" 2>/dev/null | head -5; find ~ -maxdepth 4 -name "*.json" -path "*firebase*" 2>/dev/null | head -5; ls ~/Documents/ 2>/dev/null | grep -i smoking; ls ~/Developer/ 2>/dev/null | grep -i smoking; ls ~/Sites/ 2>/dev/null | grep -i smoking; ls ~/ 2>/dev/null | grep -i smoking

Ran terminal command:  cd ~/smokingtigers-web && git remote -v && git log --oneline -5 && ls

Good. I now have full context. Let me also check the recent daily notes for any website-relevant context from the July 20-22 sessions.  

Read [](file:///Users/edhwang/Discovery/2026-07-21.md#1-1), lines 1 to 60

Read [](file:///Users/edhwang/Discovery/2026-07-22.md#1-1), lines 1 to 60

I now have a comprehensive picture. Before I proceed to create OP work packages, I need to grill you on the key questions from each roadmap section to get the missing context. Here we go:

---

## 🔍 Grill Questions — Website Roadmap Planning

I've reviewed all the memory, existing WPs, PRD, meeting notes, and the repo. Here's what I need to fill the gaps before creating properly-scoped WPs:

---

### Section 1 — Why & Who (PRD)

The existing PRD at STE-website-community.md is actually **solid** — it's not wrong, it's just out of date and incomplete. But I need to confirm a few things:

1. **Primary Goal / Single CTA:** Right now the PRD implies "join the community" as the primary CTA. Is the goal still *community sign-up*, or has it shifted to *booking a discovery call* (your July 22 notes mention paid discovery calls as a model)?
2. **Target Audience priority:** Four segments are listed (solopreneurs, SMBs, nonprofits, impact ventures). Which is **#1 right now** for the first launch — who is the site primarily speaking to?
3. **KPIs:** No KPIs are defined anywhere. What does success look like in 30/60/90 days? (Examples: X email sign-ups, X discovery call bookings, X community members?)

---

### Section 2 — Sitemap & IA

4. The current site at `smokingtigers.enterprises` was vibe-coded. Have you looked at it recently? I can open it — do you want me to do an audit and generate a sitemap from what exists, or do you have a list of pages you want to keep / cut?
5. The PRD mentions a `/contribute` page (OP#335) is already planned. Are there any other pages you know you need that aren't on the site yet? (Your July 22 notes mention a video links/playlist page and a calendar/events page.)

---

### Section 3 — Content Audit

6. The site was AI-generated. Do you have **any** high-res photos, real brand assets, or professional copy ready — or is everything placeholder text right now?
7. The Solaris-style 60-second hero video — has this been produced yet, or is it still planned?

---

### Section 4 — Wireframing

8. Christine owns design. Is she actively iterating right now, or is this paused pending the value props being drafted (OP#265)? Should the wireframe task go to her or to a Copilot-assisted spec doc?

---

### Section 5 — Tech Stack

9. The site is on Firebase + custom vibe-coded HTML/CSS. You said you want to switch to **spec coding using OP as the work surface** — does that mean you want to *rebuild* the site from scratch with a proper stack, or *refactor* what exists spec-by-spec?
10. **Gemini integration** — is this for content generation on the site (like a chatbot), for the development workflow itself, or both?

---

### Section 6 — Pre-Launch / Domain / Analytics

11. Domain confirmed: `smokingtigers.enterprises` (Firebase hosting, GCP project `smoking-tigers-agents`). Is **`smokingtigers.media`** or **`smokingtigers.org`** being used for anything right now or planned for redirection?
12. **Analytics:** Is anything tracking the current site (GA4, PostHog, etc.)? If not, do you want that added to the roadmap?
13. **SEO:** Any target keywords identified, or is that still TBD?

---

Take these one section at a time or fire all answers at once — either works. Once I have your answers, I'll draft the WPs for confirmation before posting to OP.