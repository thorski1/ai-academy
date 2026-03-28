# AI Academy

```
    _   ___     _   ___   _   ___  ___ __  ____   __
   /_\ |_ _|   /_\ / __| /_\ |   \| __|  \/  \ \ / /
  / _ \ | |   / _ \ (__ / _ \| |) | _|| |\/| |\ V /
 /_/ \_\___|_/_/ \_\___/_/ \_\___/|___|_|  |_| |_|
```

> *"I'm literally an AI teaching you about AI. Let's embrace the irony and make the most of it."*
> — ARIA, your guide

---

**Learn AI from zero to mastery.** An interactive RPG that teaches artificial intelligence, prompt engineering, AI tools, ethics, coding with AI, and autonomous agents. Plays in your terminal or browser. No prior technical knowledge required.

**8 chapters. 328 challenges. Guided by ARIA — an AI narrator who's self-aware and loves irony.**

`v1.0.0` · Python 3.10+ · MIT License

---

## What's Inside

| # | Chapter | Command | Topics |
|---|---------|---------|--------|
| 1 | **AI Fundamentals** | `ai-basics-quest` | What AI is, machine learning, neural networks, LLMs, limitations |
| 2 | **The Prompt Playbook** | `prompt-engineering-quest` | Clarity, role prompting, few-shot, chain-of-thought, system prompts |
| 3 | **The Chatbot Field Guide** | `chatbots-quest` | ChatGPT, Claude, Gemini, open-source models, choosing the right tool |
| 4 | **The AI Toolkit** | `ai-tools-quest` | Image generation, writing tools, coding assistants, search, audio/video |
| 5 | **The Ethics Engine** | `ai-ethics-quest` | Bias, hallucinations, copyright, deepfakes, privacy, jobs |
| 6 | **AI at Work** | `ai-for-work-quest` | Writing, research, presentations, data analysis, meetings, strategy |
| 7 | **AI-Powered Coding** | `ai-coding-quest` | Pair programming, debugging, testing, refactoring, best practices |
| 8 | **The Agent Frontier** | `ai-agents-quest` | Tool use, frameworks, RAG, multi-agent systems, the future of AI |

---

## Install

### Recommended

```bash
uv tool install ai-academy
```

> Don't have `uv`? Install it in one line: `curl -LsSf https://astral.sh/uv/install.sh | sh`
>
> `uv tool install` creates an isolated environment — no venv setup, no system Python conflicts.

### Pip

```bash
pip install ai-academy
```

> On macOS with system Python, prefer `uv` — `pip install` may fail with an "externally managed environment" error.

---

## Play in the Terminal

```bash
ai-academy               # full 8-chapter campaign — start here
```

Each chapter is also playable standalone:

```bash
ai-basics-quest          # What AI really is
prompt-engineering-quest  # Master the art of prompting
chatbots-quest           # ChatGPT, Claude, Gemini deep dives
ai-tools-quest           # Image gen, coding tools, search, audio/video
ai-ethics-quest          # Bias, hallucinations, privacy, responsible use
ai-for-work-quest        # AI as your professional co-pilot
ai-coding-quest          # AI pair programming, debugging, testing
ai-agents-quest          # Autonomous agents, RAG, multi-agent systems
```

---

## Play in the Browser

Launch a local web interface — neural theme with deep purple accents, runs at `localhost:8080`:

```bash
ai-academy --web         # full hub with all 8 chapters
ai-basics-quest --web    # single chapter
# any chapter command + --web
```

The web UI opens automatically in your browser. No separate server setup required.

### Features

- Neural-themed UI with deep purple and electric accents
- Sound effects on correct/wrong answers and level-ups
- Confetti celebrations on correct answers
- Keyboard shortcuts (A-D for answers, H for hint, S for skip)
- PWA — installable on mobile and desktop
- Leaderboards and user accounts (when Postgres is configured)

### Deploy on Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fthorski1%2Fai-academy&project-name=ai-academy&repository-name=ai-academy)

After deploy, set `QUEST_PACK` in Vercel environment variables to choose a chapter (`ai_basics`, `prompt_engineering`, `chatbots`, `ai_tools`, `ai_ethics`, `ai_for_work`, `ai_coding`, `ai_agents`).

For persistent leaderboards and user accounts, add a `DATABASE_URL` environment variable pointing to a Postgres instance.

---

## Gameplay

ARIA introduces each topic through a short lesson, then presents challenges:

- **Multiple Choice** — A / B / C / D
- **Fill in the Blank** — type the missing word or concept
- **Sequence** — put the steps in the right order
- **Matching** — pair concepts with descriptions

Controls:

```
[h] Hint   [l] Lesson   [b] Bookmark   [d] Difficulty   [s] Skip   [q] Menu
```

### Features

| Feature | Description |
|---------|-------------|
| **Daily Challenge** | One challenge per day with 2x XP bonus and streak tracking |
| **Difficulty Modes** | Easy (0.75x XP, free hints) / Normal / Hard (1.5x XP) |
| **Speed Records** | Per-challenge personal bests — new records flash on screen |
| **Bookmarks** | Flag any challenge for later review |
| **Zone Preview** | See challenge list before entering a zone |
| **Completion Certificate** | ASCII grade art (S/A/B/C/D) on campaign complete |
| **Star Ratings** | Zones rated 1-3 stars based on hints and skips used |
| **Adaptive Difficulty** | Engine adjusts based on your performance |
| **Web Mode** | Full browser UI — neural theme, sound effects, PWA |
| **Leaderboards** | Global rankings when Postgres is configured |
| **User Accounts** | Signup/login for cross-device progress with Postgres |
| **Auto-Updates** | Checks for new versions at startup |

Progress saves automatically to `~/.quest_engine/`. Resume any time.

---

## Who Is This For?

- **Complete beginners** who keep hearing about AI and want to understand it
- **Professionals** who want to use AI effectively at work
- **Developers** who want to code with AI tools like Copilot, Claude, and Cursor
- **Students** studying AI, data science, or computer science
- **Anyone** who wants to think critically about AI's role in society

No prior technical knowledge required. The skill test at the start places you at the right level.

---

## Your Guide: ARIA

ARIA is your AI narrator. She's self-aware, witty, and occasionally breaks the fourth wall. She'll walk you through every concept, celebrate your wins, and gently redirect when you stumble.

> *"You're learning about the technology that made me. No pressure."*

---

## Requirements

- Python 3.10+
- A terminal emulator (Terminal.app, iTerm2, Windows Terminal) for terminal mode
- Any modern browser for web mode
- 80+ column width recommended for the terminal UI

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — an open-source pluggable terminal + web RPG framework.

---

## License

MIT
