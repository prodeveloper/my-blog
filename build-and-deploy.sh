#!/bin/bash
set -e

# Blog build + deploy script
# Usage: ./build-and-deploy.sh [commit-message]

SOURCE_DIR="$HOME/ChenchaApplications/Blog/hugo_blog"
DEPLOY_DIR="$HOME/ChenchaRepos/my-blog"
MSG="${1:-Latest blog posts}"

echo "→ Building site..."
cd "$SOURCE_DIR"
hugo --gc

echo "→ Copying to deploy repo..."
cd "$DEPLOY_DIR"
rm -rf .github 2>/dev/null
cp -r "$SOURCE_DIR/public/"* .
git restore .github/workflows/static.yml 2>/dev/null || true

echo "→ Committing..."
git add -A
git commit -m "$MSG"

echo "→ Pushing..."
git push

echo "✓ Done — site will deploy via GitHub Actions in ~1-2 min"
