"""
Vercel entrypoint for AI Academy — serves all 8 chapters via the hub.

    /                       → Chapter chooser (hub landing page)
    /ai_basics/             → AI Fundamentals
    /prompt_engineering/    → The Prompt Playbook
    /chatbots/              → The Chatbot Field Guide
    ... and so on for all 8 chapters.

Set QUEST_PACK env var for single-chapter mode. Leave unset for the full hub.
"""

import os
import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

import ai_academy as _pkg  # noqa: E402
_PACKS_DIR = str(Path(_pkg.__file__).parent / "skill-packs")
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", _PACKS_DIR)

from engine.skill_pack import load_skill_pack  # noqa: E402

_AI_PACKS = [
    "ai_basics", "prompt_engineering", "chatbots", "ai_tools",
    "ai_ethics", "ai_for_work", "ai_coding", "ai_agents",
]


def _make_app():
    _single_pack = os.environ.get("QUEST_PACK", "")
    if _single_pack:
        from engine.web.server import create_app
        return create_app(load_skill_pack(_single_pack, packs_dir=_PACKS_DIR))
    from engine.web.hub import create_hub_app
    _packs = [load_skill_pack(p, packs_dir=_PACKS_DIR) for p in _AI_PACKS]
    return create_hub_app(_packs)


app = _make_app()
