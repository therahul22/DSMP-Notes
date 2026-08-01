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
```

Tagging creates explicit reference pointers to specific points in Git history, primarily used to mark release versions.

### Semantic Versioning Syntax: `X.Y.Z`
* **X (Major Version):** Incompatible API changes or breaking updates.
* **Y (Minor Version):** New functionality added in a backward-compatible manner.
* **Z (Patch Version):** Backward-compatible bug fixes and patch adjustments.

```bash
# Tag the current HEAD commit with an annotated version tag
git tag -a v1.0.0 -m "Initial Production Release"

# Tag a past commit using its SHA-1 hash
git tag -a v0.9.0 <SHA_HASH> -m "Beta Testing Release"

# List all tags
git tag

# Delete a tag
git tag -d v0.9.0
```

---

## 6. Branching Mechanics & HEAD Pointer Mechanics

A **branch** in Git is simply a lightweight, movable pointer to a commit snapshot.

### The `HEAD` Pointer
The **`HEAD`** pointer is a dynamic reference pointing to the currently active branch or commit in your working directory. Moving `HEAD` changes the state of files in your working space.

```
                  HEAD
                   │
                   ▼
               [main]
                   │
                   ▼
[Commit C1] ◄── [Commit C2] ◄── [Commit C3]
```

### Branching Commands
```bash
# Create a new branch pointing to the current HEAD
git branch feature-auth

# Create a new branch originating from a historical commit SHA
git branch bugfix-login <SHA_HASH>

# List all local branches (* indicates current active branch where HEAD points)
git branch

# Switch HEAD to another existing branch
git checkout feature-auth

# Shortcut: Create AND switch to a new branch simultaneously
git checkout -b feature-dashboard

# View all branches visually across full history graphs
git log --oneline --graph --all

# Deleting branches
git branch -d feature-auth    # Safe delete (fails if branch has unmerged changes)
git branch -D feature-auth    # Force delete unmerged branch
```

---

## 7. Merging Strategies & Conflict Resolution 💡 *(Interview Topic)*

Merging combines the histories of independent execution branches. **Merging always occurs on the currently checked-out branch.**

```bash
git checkout main
git merge feature-auth
```

### 1. Fast-Forward Merge
Occurs when the target branch (`main`) has **no intermediate commits** since the source branch (`feature-auth`) diverged. Git simply moves the `main` pointer forward to match the tip of `feature-auth`. No merge commit is generated.

```
Before Fast-Forward:
main:     C1 ──► C2 (HEAD)
feature:          └──► C3 ──► C4

After 'git merge feature':
main, feature: C1 ──► C2 ──► C3 ──► C4 (HEAD)
```

### 2. Recursive Three-Way Merge (Divergent Branches)
Occurs when both branches have diverged with independent commits. Git identifies a common ancestor commit (three-way comparison) and creates a dedicated **Merge Commit** with two parent commits.

```
Divergent Graph:
main:     C1 ──► C2 ───────► C5 (HEAD / Merge Commit)
                  └──► C3 ──► C4 (feature)
```

### 3. Resolving Merge Conflicts
A conflict occurs when changes are made to the **same line(s) of the same file** in different ways across merging branches.

#### Conflict Block Markers
When a conflict occurs, Git halts the merge and inserts conflict markers directly into affected files:

```text
<<<<<<< HEAD
# Code present on your currently checked-out active branch
print("System status: Active")
=======
# Code present on the incoming branch being merged
print("System status: Active & Authenticated")
>>>>>>> heading-update
```

#### Conflict Resolution Steps:
1. Open conflicted files and manually select desired code combinations.
2. Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Save file, stage resolved files via `git add <file>`.
4. Run `git commit` to finalize the merge snapshot.

---

## 8. Remote Workflows: Collaborating with GitHub

Remote repositories hosted on GitHub serve as centralized reference hubs for distributed team synchronization.

```bash
# Connect local repo to a remote hosting repository short-named 'origin'
git remote add origin [https://github.com/user/repo.git](https://github.com/user/repo.git)

# View configured remote tracking aliases
git remote -v

# Push local commits to remote branch
git push origin main

# Set default upstream tracking branch (-u flag)
git push -u origin main
```

### Fetch vs. Pull
* **`git fetch origin main`:** Downloads new commits from remote without merging them into working branch files.
* **`git pull origin main`:** Downloads remote commits and **immediately executes a `git merge`** into the local branch (`git pull = git fetch + git merge`).

---

## 9. Undoing Changes & History Rewriting

### Modifying the Last Commit (`--amend`)
If you made a typo in the previous commit message or forgot to include staged files:

```bash
# Add forgotten file
git add forgotten_file.py

# Amend previous commit snapshot without modifying its commit message
git commit --amend --no-edit

# Amend previous commit message
git commit --amend -m "Updated commit message description"
```

### Reverting vs. Resetting 💡 *(Interview Topic)*

| Command | Action | Use Case |
| :--- | :--- | :--- |
| **`git revert <SHA>`** | Generates a **new commit** that completely inverses/undoes changes made in the target SHA. | **Safe for Public Repositories** (preserves continuous commit history without rewriting timeline). |
| **`git reset`** | Moves `HEAD` pointer backward to a historical SHA, altering commit history. | **Private/Local Repositories** (Rewrites history). |

```bash
# Safely undo specific past commit by recording inverse commit
git revert <SHA_HASH>

# Soft Reset: Moves HEAD back, leaves working directory and staged index untouched
git reset --soft <SHA_HASH>

# Mixed Reset (Default): Moves HEAD back, un-stages changes, keeps working directory files
git reset --mixed <SHA_HASH>

# Hard Reset: DESTRUCTIVE! Discards ALL local changes and resets files to target commit state
git reset --hard <SHA_HASH>
```
