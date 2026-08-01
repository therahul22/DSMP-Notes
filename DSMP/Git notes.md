# Git & Version Control — Fundamentals, Commits & Semantic Versioning

---

## 1. Version Control Systems (VCS) Architecture 💡 *(Interview Topic)*

A **Version Control System** tracks changes to files over time so you can recall specific versions later, collaborate non-linearly, and safely rollback buggy releases.

### Centralized vs. Distributed VCS
* **Centralized VCS (e.g., SVN, Perforce):** A single central server stores the full commit history. Developers check out files locally, but server failure halts collaboration and commit capability.
* **Distributed VCS (e.g., Git, Mercurial):** Every developer's local machine clone acts as a full-fledged repository containing the complete commit history. Work can happen completely offline.

---

## 2. The Three States of Git Mechanics

Git tracks files through three primary local lifecycle areas:

```
┌────────────────────────┐    git add     ┌────────────────────────┐   git commit   ┌────────────────────────┐
│   Working Directory    │ ─────────────> │     Staging Area       │ ─────────────> │    Local Repository    │
│  (Unstaged/Modified)   │                │        (Index)         │                │     (Committed)        │
└────────────────────────┘                └────────────────────────┘                └────────────────────────┘
```

1. **Working Directory:** The local filesystem directory where files are actively edited and modified.
2. **Staging Area (Index):** A draft file containing tracked snapshot changes prepared to go into the next commit.
3. **Local Repository (`.git`):** The local database storing committed snapshot metadata, blobs, trees, and commit objects.

---

## 3. Core Initialization & Staging Commands

### Repositories Setup
```bash
# Initialize a new, empty Git repository in current folder
git init

# Clone an existing remote repository locally
git clone [https://github.com/user/repository.git](https://github.com/user/repository.git)

# Check working tree status (untracked, modified, or staged files)
git status
```

### Staging Changes & Using `.gitignore`
```bash
# Stage a specific file
git add filename.py

# Stage all tracked/untracked changes across the current directory
git add .
```

#### The `.gitignore` File
Create a `.gitignore` text file in the root directory to specify untracked files or patterns that Git should ignore (e.g., virtual environments, credentials, build output).

```gitignore
# Ignore python cache files and byte-compiled files
__pycache__/
*.pyc

# Ignore environment variables / secrets
.env

# Ignore dependency directories
node_modules/
venv/
```

### Recording Snapshots (Committing)
```bash
# Record staged changes into the local repository with a clear message
git commit -m "feat: implement user authentication flow"
```

---

## 4. History Inspection & Diffing Tools 💡 *(Interview Favorite)*

Every Git commit is identified by a unique **SHA-1 hash** (a 40-character hexadecimal string representing the contents and metadata).

```bash
# 1. Full Commit History Log
git log

# 2. Compact View (Displays 7-character short SHA-1 hashes and commit messages)
git log --oneline

# 3. File Statistics Log (Shows number of insertion/deletion lines per file)
git log --stat

# 4. Patch View (Shows full line-by-line detailed diffs for every commit in history)
git log -p

# 5. Inspecting Specific Commits (Inspects changes introduced by a given commit SHA)
git show 7a1b2c3

# 6. Uncommitted Diffs (Shows unstaged differences in working directory against index)
git diff
```

---

## 5. Semantic Versioning & Release Tagging (`git tag`)

Software releases use **Semantic Versioning (SemVer)** represented as `X.Y.Z` (e.g., `v2.4.1`):

```
       vX.Y.Z
        │ │ │
        │ │ └─── Z: Patch Version  -> Bug fixes, hotfixes (Backwards compatible)
        │ └───── Y: Minor Version  -> New functionality added (Backwards compatible)
        └─────── X: Major Version  -> Breaking API changes (NOT backwards compatible)
