# SOP: Website Collaboration
**Project:** SmokingTigers.Enterprises website  
**Repo:** https://github.com/edjieun/smokingtigers-web  
**Status:** Draft — 2026-07-22  
**Author:** Copilot Agent  
**Attach to:** OP (governance project — see WP for OP#ID)

---

## Purpose

This SOP defines how contributors work on the STE website together — from picking up a task to getting code into production. It applies to all contributors (Ed, Christine, agents, and future members).

The goal is peer review, not gatekeeping. Anyone with collaborator access can review. No single person is the bottleneck.

---

## Resources

| Resource | URL |
|---|---|
| GitHub repo | https://github.com/edjieun/smokingtigers-web |
| OpenProjects (STE Website project) | https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-website |
| OpenProjects (Governance project) | https://ste-business-server.tailebe6d3.ts.net:8080/projects/governance |
| Live site | https://smokingtigers.enterprises |
| Governance repo | https://github.com/edjieun/smoking-tigers-governance |
| Agent instructions | `.github/agents/website-builder.agent.md` in the web repo |

---

## Roles

| Role | Responsibility |
|---|---|
| **Contributor** | Anyone making a change — Ed, Christine, agents |
| **Reviewer** | Any other contributor (peer review — not role-specific) |
| **Steward** | Ed — final merge authority for structural/content changes; not required for typo/copy fixes |

---

## Workflow

### 1. Pick up a task

Every website change should have an OP work package before work starts.

- Check open WPs in the [STE Website project](https://ste-business-server.tailebe6d3.ts.net:8080/projects/ste-website/work_packages)
- If no WP exists for your change → create one before you start
- Assign yourself, set status to **In Progress**

### 2. Create a branch

Never commit directly to `main`.

```bash
git checkout -b <your-name>/<short-description>
# Examples:
# christine/community-page-update
# ed/governance-footer-links
# copilot/contribute-page
```

Branch naming: `<author>/<what-it-does>` — lowercase, hyphen-separated.

### 3. Make your changes

- All pages live under `public/`
- Follow the existing design system (CSS variables, Art Deco pattern, Cormorant Garamond + DM Sans fonts)
- Accessibility requirements: `alt` text on images, ARIA roles on interactive elements, semantic HTML5
- Run a local preview before opening a PR: `python3 -m http.server 8000` from the `public/` directory

### 4. Open a Pull Request

When your change is ready for review:

1. Push your branch to GitHub
2. Open a PR from your branch → `main`
3. PR title: `[WP#ID] Short description` — e.g., `[OP#266] Add onboarding flow to community page`
4. PR description must include:
   - Link to the OP work package
   - What changed and why
   - Screenshot or link to local preview (for visual changes)
5. Request review from at least one other contributor

### 5. Review

**Reviewer checklist:**
- [ ] Does the change match the OP work package scope?
- [ ] Does it follow the design system (colors, fonts, spacing)?
- [ ] Are there broken links or placeholder text? (e.g., `REPLACE-WITH-INVITE`)
- [ ] Does it work on mobile (check at 375px width)?
- [ ] Is HTML semantic and accessible?

Approve with a comment. If requesting changes, be specific — not just "change this."

### 6. Merge

- Squash and merge preferred for small changes
- Ed merges structural changes (new pages, nav updates, major content shifts)
- Either contributor can merge copy fixes and minor updates after approval
- Delete the branch after merging

### 7. Deployment

Changes to `public/` deploy automatically via Caddy on the Mac Mini server.  
No manual deploy step needed. Verify at https://smokingtigers.enterprises after merge.

For Firebase backup: `firebase deploy --only hosting` (run manually when needed).

### 8. Close the WP

After merge, update the OP work package:
- Set status to **Closed**
- Add a comment with the PR link and merge commit

---

## Content decisions vs. code changes

| Change type | Who decides | Review required |
|---|---|---|
| Typo / grammar fix | Contributor | Yes — but can self-merge if trivial |
| Copy / messaging update | Ed + contributor | Yes — peer review |
| New page or section | Ed (with input from contributors) | Yes — Ed approves merge |
| Navigation changes | Ed | Yes — Ed approves merge |
| Design system changes | Ed | Yes — Ed approves merge |
| Governance links / references | Ed | Yes — Ed approves merge |

---

## Known issues to fix (as of 2026-07-22)

- Discord invite links are placeholders: `https://discord.gg/REPLACE-WITH-INVITE` — needs real link
- Footer GitHub link points to `https://github.com/SmokingTigers/GovRepo` — should be `https://github.com/edjieun/smoking-tigers-governance`
- Community page was pushed directly to main without PR — this SOP is retroactive from this date forward

---

## Governance

This SOP is governed by the same process as all STE governance docs:  
- Draft → proposed → approved by Ed → merge via PR  
- Stored in: Governance repo (`edjieun/smoking-tigers-governance`) and attached to OP  
- This file is **temporary staging** in Discovery — the canonical version lives in OP as an attachment
