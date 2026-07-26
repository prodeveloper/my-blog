+++
title = 'hugo tips'
date = 2025-01-21T13:05:53+01:00
draft = false
+++


This command does a commit. Run it from public folder.
```
bash push_to_live.sh   
```

The folder that gets published is just the public folder everything else I need to move manually

To solve the problem of localhost appearing in prod

1. ensure setup done on hugo.toml
2. run ``` ❯ hugo --environment production ```
3. Push changes to prod

Moving the project around:
- archived and uploaded to gdrive

