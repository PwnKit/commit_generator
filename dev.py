import os
import random
from datetime import datetime, timedelta

total_day = 458  # Total days back
repo_link = "https://github.com/PwnKit/commit_generator.git"

now = datetime.now()
ctr = 1
pointer = 0

# Initialize commit file
f = open("commit.txt", "w")
f.close()

# Set up Git configurations
os.system("git config user.name 'YourUsername'")
os.system("git config user.email 'youremail@example.com'")
os.system("git init")

while pointer < total_day:
    # Calculate the date for this iteration
    current_day = now - timedelta(days=pointer)
    
    # Randomly decide whether to make commits or skip the day
    skip_day = random.choice([True, False])  # Randomly choose to skip or not
    
    if skip_day:
        print(f"Skipping day {current_day.strftime('%Y-%m-%d')} with no commits.")
        pointer += 1
        continue
    
    # Random commit frequency per day (between 1 and 10 commits per day)
    commit_frequency = random.randint(1, 10)
    
    for _ in range(commit_frequency):
        # Prepare the commit date and message
        formatdate = current_day.strftime("%Y-%m-%d")
        with open("commit.txt", "a+") as f:
            f.write(f"Commit {ctr}: {formatdate}\n")
        
        # Git commit actions
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"Commit {ctr}\"")
        print(f"Commit {ctr}: {formatdate}")
        ctr += 1
    
    pointer += 1

# Push to remote repository
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
