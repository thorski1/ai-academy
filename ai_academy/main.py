"""
ai_academy/main.py — Entry points for AI Academy.
"""

import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))
os.environ.setdefault("QUEST_CAMPAIGNS_DIR", str(_HERE / "campaigns"))

from engine.main import run, run_campaign          # noqa: E402
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "ai-academy"
_PACKS_DIR = str(_HERE / "skill-packs")

_WEB = "--web" in sys.argv

AI_PACKS = [
    "ai_basics", "prompt_engineering", "chatbots", "ai_tools",
    "ai_ethics", "ai_for_work", "ai_coding", "ai_agents", "ai_safety", "ai_rag", "ai_finetuning",
]


def _web(pack_name: str, port: int = 8080):
    from engine.web.server import serve
    serve(pack_name, port=port, packs_dir=_PACKS_DIR)


def main_ai_academy():
    if _WEB:
        from engine.web.hub import serve_hub
        serve_hub(AI_PACKS, port=8080, packs_dir=_PACKS_DIR)
        return
    check_and_prompt(_PACKAGE)
    run_campaign("ai_academy")


def main_ai_basics():
    if _WEB: _web("ai_basics"); return
    check_and_prompt(_PACKAGE); run("ai_basics")

def main_prompt_engineering():
    if _WEB: _web("prompt_engineering"); return
    check_and_prompt(_PACKAGE); run("prompt_engineering")

def main_chatbots():
    if _WEB: _web("chatbots"); return
    check_and_prompt(_PACKAGE); run("chatbots")

def main_ai_tools():
    if _WEB: _web("ai_tools"); return
    check_and_prompt(_PACKAGE); run("ai_tools")

def main_ai_ethics():
    if _WEB: _web("ai_ethics"); return
    check_and_prompt(_PACKAGE); run("ai_ethics")

def main_ai_for_work():
    if _WEB: _web("ai_for_work"); return
    check_and_prompt(_PACKAGE); run("ai_for_work")

def main_ai_coding():
    if _WEB: _web("ai_coding"); return
    check_and_prompt(_PACKAGE); run("ai_coding")

def main_ai_agents():
    if _WEB: _web("ai_agents"); return
    check_and_prompt(_PACKAGE); run("ai_agents")
