"""Render the diagrams for the three MIT AGAI Medium write-ups.

Style matches the IBM capstone write-ups: navy/blue rounded boxes on white.
Run from anywhere:  python writeups/make_figures.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
BLUE, NAVY, GRAY, LIGHT, INK = "#2b6cb8", "#17335c", "#9aa5b1", "#e8eef6", "#17335c"
plt.rcParams["font.family"] = "DejaVu Sans"


def canvas(w=19, h=5.2):
    fig, ax = plt.subplots(figsize=(w, h), dpi=100)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, title, sub="", color=BLUE, tsize=22, ssize=15, tcolor="white"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.22",
                                fc=color, ec="none"))
    if sub:
        ax.text(x + w / 2, y + h * 0.66, title, ha="center", va="center",
                fontsize=tsize, weight="bold", color=tcolor)
        ax.text(x + w / 2, y + h * 0.30, sub, ha="center", va="center",
                fontsize=ssize, color=tcolor, linespacing=1.3)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                fontsize=tsize, weight="bold", color=tcolor)


def arrow(ax, x0, x1, y, color=NAVY):
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.7",
                                lw=3, color=color))


def save(fig, rel):
    out = HERE / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", pad_inches=0.35, facecolor="white")
    plt.close(fig)
    print("wrote", out)


# Week 1: reactive vs. proactive -------------------------------------------
def reactive_vs_proactive():
    fig, ax = canvas(19, 7.2)
    ax.text(9.5, 6.75, "From responding to pursuing a goal", ha="center",
            fontsize=28, weight="bold", color=INK)
    # reactive row
    ax.text(0.6, 5.05, "Reactive (generative AI)", fontsize=17, weight="bold", color=GRAY)
    box(ax, 0.6, 3.35, 3.0, 1.4, "Prompt", color=GRAY, tsize=20)
    arrow(ax, 3.65, 4.6, 4.05, GRAY)
    box(ax, 4.65, 3.35, 3.0, 1.4, "Response", color=GRAY, tsize=20)
    ax.text(8.1, 4.05, "one input, one output, no goal of its own", va="center",
            fontsize=16, color=GRAY, style="italic")
    # proactive row
    ax.text(0.6, 2.45, "Proactive (agentic AI)", fontsize=17, weight="bold", color=NAVY)
    steps = [("Goal", "the objective"), ("Plan", "decompose\ninto steps"),
             ("Act", "call tools,\nquery systems"), ("Check", "evaluate\nits own work"),
             ("Adapt", "revise, or\nescalate to a human")]
    w, gap, x = 3.0, 0.62, 0.6
    for i, (t, s) in enumerate(steps):
        box(ax, x, 0.35, w, 1.85, t, s, color=NAVY if i % 2 else BLUE, tsize=21, ssize=13.5)
        if i < len(steps) - 1:
            arrow(ax, x + w + 0.04, x + w + gap - 0.04, 1.27)
        x += w + gap
    save(fig, "01-what-is-an-agent/reactive_vs_proactive.png")


# Week 2: five building blocks + threshold map --------------------------------
def five_decisions():
    fig, ax = canvas(19, 5.6)
    ax.text(9.5, 5.05, "Five decisions every agent design makes", ha="center",
            fontsize=28, weight="bold", color=INK)
    blocks = [("Perception", "what it can see,\nand what it can't"),
              ("Action", "which tools it can call,\nwith what side effects"),
              ("Planning", "how it breaks down\nthe goal"),
              ("Memory", "what it keeps\nbetween runs"),
              ("Safety", "what it may never do\nwithout a human")]
    w, gap, x = 3.36, 0.3, 0.6
    for i, (t, s) in enumerate(blocks):
        box(ax, x, 0.9, w, 3.2, t, s, color=NAVY if i % 2 else BLUE, tsize=22, ssize=14)
        x += w + gap
    ax.text(9.5, 0.35, "Same five questions whether you build, buy, or stack.",
            ha="center", fontsize=16, color=GRAY, style="italic")
    save(fig, "02-every-agent-needs-a-manager/five_decisions.png")


def threshold_map():
    fig, ax = canvas(19, 6.4)
    ax.text(9.5, 5.85, "Human-in-the-loop is a threshold map, not a switch", ha="center",
            fontsize=27, weight="bold", color=INK)
    rows = [("Low stakes, reversible", "agent acts alone, logged", BLUE, 0.92),
            ("Medium stakes", "agent acts, human samples & reviews", "#3f5f8f", 0.62),
            ("High stakes or irreversible", "human approves before it happens", NAVY, 0.32)]
    y = 3.85
    for label, rule, c, frac in rows:
        ax.text(0.6, y + 0.55, label, fontsize=18, weight="bold", color=INK, va="center")
        ax.add_patch(FancyBboxPatch((7.2, y + 0.12), 11.2, 0.86,
                                    boxstyle="round,pad=0,rounding_size=0.2", fc=LIGHT, ec="none"))
        ax.add_patch(FancyBboxPatch((7.2, y + 0.12), 11.2 * frac, 0.86,
                                    boxstyle="round,pad=0,rounding_size=0.2", fc=c, ec="none"))
        if frac >= 0.5:
            ax.text(7.5, y + 0.55, rule, fontsize=16, color="white", va="center", weight="bold")
        else:
            ax.text(7.2 + 11.2 * frac + 0.3, y + 0.55, rule, fontsize=16, color=INK, va="center", weight="bold")
        y -= 1.45
    ax.text(7.2, 0.2, "bar = how much the agent does on its own", fontsize=14,
            color=GRAY, style="italic")
    save(fig, "02-every-agent-needs-a-manager/threshold_map.png")


# Week 3: autonomy dial + four safeguard layers ------------------------------
def safeguard_layers():
    fig, ax = canvas(19, 8.4)
    ax.text(9.5, 7.85, "Four safeguard layers, four owners", ha="center",
            fontsize=28, weight="bold", color=INK)
    layers = [("Hardcoded constraints", "rules that run outside the model; it can't reason past them", "Legal"),
              ("Output verification", "a second check before any result triggers an action", "Operations"),
              ("Reversibility by design", "no irreversible move faster than you can catch a mistake", "Finance"),
              ("Escalation architecture", "a staffed, funded path to a human at the edge of competence", "People")]
    y, h = 5.75, 1.45
    for i, (t, s, owner) in enumerate(layers):
        c = BLUE if i % 2 == 0 else NAVY
        ax.add_patch(FancyBboxPatch((0.6, y), 14.6, h, boxstyle="round,pad=0,rounding_size=0.22",
                                    fc=c, ec="none"))
        ax.text(1.0, y + h * 0.66, t, fontsize=21, weight="bold", color="white", va="center")
        ax.text(1.0, y + h * 0.28, s, fontsize=15, color="white", va="center")
        ax.add_patch(FancyBboxPatch((15.5, y), 2.9, h, boxstyle="round,pad=0,rounding_size=0.22",
                                    fc=LIGHT, ec="none"))
        ax.text(16.95, y + h / 2, owner, fontsize=19, weight="bold", color=INK,
                ha="center", va="center")
        y -= h + 0.3
    ax.text(16.95, 7.3, "owner", fontsize=14, color=GRAY, ha="center", style="italic")
    ax.set_ylim(-0.6, 8.4)
    ax.text(0.6, -0.25, "Defense in depth: any single layer can fail without the whole system failing.",
            fontsize=15, color=GRAY, style="italic")
    save(fig, "03-seduction-of-the-demo/safeguard_layers.png")


def autonomy_dial():
    fig, ax = canvas(19, 4.6)
    ax.text(9.5, 4.05, "Autonomy is a dial, set task by task", ha="center",
            fontsize=28, weight="bold", color=INK)
    n = 60
    for i in range(n):
        t = i / (n - 1)
        r = int(0x2b + (0x17 - 0x2b) * t); g = int(0x6c + (0x33 - 0x6c) * t); b = int(0xb8 + (0x5c - 0xb8) * t)
        ax.add_patch(plt.Rectangle((0.6 + 17.8 * i / n, 1.75), 17.8 / n + 0.02, 0.9,
                                   fc=f"#{r:02x}{g:02x}{b:02x}", ec="none"))
    ax.text(0.6, 1.25, "Fully constrained", fontsize=18, weight="bold", color=BLUE)
    ax.text(0.6, 0.7, "only pre-verified answers: safe, limited", fontsize=15, color=GRAY)
    ax.text(18.4, 1.25, "Fully autonomous", fontsize=18, weight="bold", color=NAVY, ha="right")
    ax.text(18.4, 0.7, "powerful: every output carries uncertainty", fontsize=15, color=GRAY, ha="right")
    for x, lbl in [(4.2, "answer FAQs"), (9.5, "draft supplier\nassessments"), (14.2, "approve\npayments?")]:
        ax.plot([x, x], [1.62, 2.78], color="white", lw=4)
        ax.text(x, 3.05, lbl, ha="center", va="bottom", fontsize=14, color=INK, linespacing=1.15)
    save(fig, "03-seduction-of-the-demo/autonomy_dial.png")


if __name__ == "__main__":
    reactive_vs_proactive()
    five_decisions()
    threshold_map()
    safeguard_layers()
    autonomy_dial()
