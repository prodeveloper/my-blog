#!/bin/bash
# Check em-dash count in a markdown file
# Usage: ./check-em-dashes.sh <file.md>
# Returns: count, and exits 0 if <= 5, 1 if > 5

FILE="$1"
if [ -z "$FILE" ]; then
  echo "Usage: $0 <file.md>"
  exit 2
fi

COUNT=$(grep -o '—' "$FILE" | wc -l | tr -d ' ')
echo "$COUNT em-dashes in $FILE"

if [ "$COUNT" -gt 2 ]; then
  echo "⚠️  Over limit ($COUNT > 2) — needs rework"
  exit 1
else
  echo "✅ Within limit"
  exit 0
fi
