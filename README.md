Steps to Perform






1. Configure AWS with AWS Configure command
2. Create AWS S3 Bucket
3. git init
4. install python 3
5. give permissions to pre_commit_hook.py as "chmod +x pre_commit_hook.py"
6. Create Soft link with git hook pre-commit. "ln -s ../../pre_commit_hook.py .git/hooks/pre-commit"
7. Change Bucket name in the script :  S3_BUCKET = "s3testpush"
8. git add.
9. git commit -m "first commit for push"

 Script will execute
 
