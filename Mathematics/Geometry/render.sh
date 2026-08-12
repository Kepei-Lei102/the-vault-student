#!/usr/bin/env bash
# Render the heptadecagon Manim animation.
# Default: 4K committed render. Pass "draft" for 720p iteration, "review" for 1080p.
#
# Usage:
#     bash render.sh           # -qk (2160p60, ~30-60 min on M-series) → committed final
#     bash render.sh review    # -qh (1080p60)                          → review pass
#     bash render.sh draft     # -qm  (720p30, ~3-5 min)                 → fast iteration
#
# Output is copied to ./heptadecagon.mp4 so the vault note's `![[heptadecagon.mp4]]` resolves.

set -euo pipefail
cd "$(dirname "$0")"

case "${1:-final}" in
  draft)   FLAG="-qm"; OUT_DIR="720p30"  ;;
  review)  FLAG="-qh"; OUT_DIR="1080p60" ;;
  final|*) FLAG="-qk"; OUT_DIR="2160p60" ;;
esac

echo "Rendering heptadecagon at $OUT_DIR ($FLAG)..."
manim "$FLAG" heptadecagon.py Heptadecagon

cp "media/videos/heptadecagon/$OUT_DIR/Heptadecagon.mp4" ./heptadecagon.mp4
echo "Done. Vault MP4 at: $(pwd)/heptadecagon.mp4"
