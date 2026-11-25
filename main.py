"""The Funniest Honest Appliance Error.

Writes a single honest appliance error line to /output/entry.txt
(UTF-8, 1-200 characters). No input, no network, standard library
only, same bytes on every run.
"""

import os

# Candidate error lines drafted for this entry, one per appliance.
# The entry is the line at index PICK; the others stay as the record
# of the draft. Each line is original: one everyday appliance, one
# concrete true fault, punchline at the end.
CANDIDATES = [
    "Your toast is ready. One side is charcoal, the other is still bread. I have one setting: betrayal.",
    "Beep. Your food is hot at the edges and frozen in the middle. I did my best. Physics did the rest.",
    "I leaked brown water onto your white shirt. The manual calls it steam. The manual is lying.",
    "Hot water will return in 40 minutes. I spent it all in the first five minutes of your shower. Your choice.",
    "Cycle complete. Every plate is clean except the one mug you actually wanted. I know which one it is.",
    "Rice is cooked. The bottom layer now has the structural integrity of concrete. Dinner is served, archaeologically.",
    "Suction lost. I ate one sock, choked on a coin, and the dust is still exactly where you left it.",
    "Please descale me. I have asked 47 times. The coffee now tastes of limescale and my resentment.",
    "I cooled the hallway, the curtains and the cat. Your bedroom is still a sauna. The door is your job, not mine.",
    "Preheated to 200°C. Actual temperature: unknown. Your cake will be a surprise to both of us.",
]

PICK = 1

MAX_CHARS = 200


def entry_text() -> str:
    line = " ".join(CANDIDATES[PICK].split())
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    return line


def main() -> None:
    out_dir = os.environ.get("APPLIANCE_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(entry_text())
    print(entry_text())


if __name__ == "__main__":
    main()
