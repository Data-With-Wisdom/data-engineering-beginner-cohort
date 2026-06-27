# Git & GitHub Basics for Beginners

## 1. What is Git?

Git is a **version control system**. It helps you track changes in your code or files over time.

### Why Git is useful:

* Keeps history of changes
* Lets you go back to previous versions
* Helps multiple people work on the same project
* Prevents overwriting each other’s work

---

## 2. What is GitHub?

GitHub is a **cloud platform** that stores Git repositories online.

### Why GitHub exists:

* Backup your code online
* Share projects with others
* Collaborate with teams
* Showcase your projects (portfolio)

Think of it like:

* Git = tool on your computer
* GitHub = online storage for Git projects

---

## 3. Installing Git on Windows

### Step 1: Download Git

Go to:
[https://git-scm.com/downloads](https://git-scm.com/downloads)

### Step 2: Install

* Run the installer
* Keep default settings (recommended)
* Finish installation

### Step 3: Verify installation

Open **Command Prompt** or **Git Bash** and run:

```
git --version
```

If it shows a version number, Git is installed.

---

## 4. Basic Git Setup (First Time Only)

Set your username and email:

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check config:

```
git config --list
```

---

## 5. Creating a Git Repository (Local)

Inside your project folder:

```
git init
```

This initializes Git in the folder.

---

## 6. Connecting to GitHub (Remote Repo)

First create a repository on GitHub:

* Go to [https://github.com](https://github.com)
* Click **New Repository**
* Give it a name
* Click Create

---

## 7. Common Git Workflow

### 1. Check status

```
git status
```

### 2. Add files to staging

```
git add .
```

### 3. Commit changes

```
git commit -m "first commit"
```

### 4. Connect to GitHub repo

```
git remote add origin https://github.com/username/repo-name.git
```

### 5. Push code to GitHub

```
git push -u origin main
```

---

## 8. Cloning a Repository (Download from GitHub)

```
git clone https://github.com/username/repo-name.git
```

This downloads the project to your local machine.

---

## 9. Pulling Updates from GitHub

If changes were made online:

```
git pull origin main
```

---

## 10. Basic Git Commands Summary

| Command             | Meaning               |
| ------------------- | --------------------- |
| git init            | Start a repo          |
| git status          | Check file status     |
| git add .           | Stage changes         |
| git commit -m "msg" | Save changes          |
| git push            | Upload to GitHub      |
| git pull            | Download updates      |
| git clone           | Copy repo from GitHub |

---

## 11. Simple Mental Model

* You work on files locally
* You track changes with Git
* You save snapshots (commit)
* You upload to GitHub (push)
* You download updates (pull)

---

## 12. Common Beginner Mistakes

* Forgetting to commit before pushing
* Not adding files before commit
* Wrong branch name (main vs master)
* Not setting remote origin

---

## 13. Practice Task for Students

1. Create a folder called `my-first-repo`
2. Initialize Git
3. Create a simple text file
4. Add and commit the file
5. Create a GitHub repo
6. Push your code
7. Clone it into another folder
8. Make a change and push again

---

## End