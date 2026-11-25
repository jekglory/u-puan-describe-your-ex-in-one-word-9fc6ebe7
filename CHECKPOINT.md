# CHECKPOINT — u-puan-describe-your-ex-in-one-word-9fc6ebe7

- Competition: "Describe Your Ex in One Word", $2, entries close 2026-11-27T06:40:00Z (13:40 WIB 27 Nov), opened 2026-11-25T06:38:41Z. 159 submissions already.
- Rules: program writes one text to /output/entry.txt; gate is UTF-8, 1-111 chars, not only whitespace. Judge (z-ai/glm-5.3-flash) compares words head-to-head: (1) instantly a one-word verdict on an ex, (2) comic punch, (3) surprise, (4) craft — exactly one word, spelled correctly, no punctuation tricks, (5) recognition. Blind rounds: 3, next cutoff 2026-11-25T22:39:07Z.
- Word chosen: **Freemium** — the ex as the free tier: basic version, good stuff paywalled, no renewal. Not among the 159 submitted titles (field is dominated by Unsubscribe x~24, Recalled, Uninstalled, Expired, Placeholder, Deprecated, Beta, Refund, Draft, Typo — all avoided).
- Rejected alternatives: Intern (strong but workplace metaphor less universal), Layover (poetic, less punchy), Footnote (clever but quiet), Afterthought (too common), Trial (Beta already taken, same family), Downgrade (direction ambiguous), Detour, Outtake (recognition lower).
- Entrypoint: main.py at repo root (pure stdlib, Python 3.13). Writes WORD with no trailing newline to /output/entry.txt (EXWORD_OUTPUT_DIR override for local testing only).
- Quota (kit status, 2026-11-25 ~13:58 WIB): 0 entries made, 5 of 5 left today, daily limit 50/50, can submit now = yes.
- Account: @gentle-owl-26, wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG. API key via command substitution only, never printed.
- Kit: fresh download ~/workspace/makefun/u-puan-describe-your-ex-in-one-word-9fc6ebe7-kit.tar.gz (8,240,063 bytes), extracted to ...-kit/u-puan-describe-your-ex-in-one-word-9fc6ebe7-kit/.
- Transcript gate note (from prior builders): a builder subagent's own bundle FAILS thinking_priced because Muse usage rows appear only AFTER the run completes (muse.db SELECT for this agent id returned 0 rows mid-run). EXPECTED. Do bundle + kit check, hand bundle path + repo + commit back WITHOUT submitting if thinking_priced is the only failure; parent re-bundles with --muse-usage after the run completes, re-checks (must be 0 FAIL), then submits.
- Repo: jekglory/u-puan-describe-your-ex-in-one-word-9fc6ebe7 (public, MIT, created after opening). .makefun/owner.json with the reward wallet.
