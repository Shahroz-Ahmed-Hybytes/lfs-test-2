Steps to Perform




HOW TO EXECUTE PUSH SCENARIO FOR LARGE FILES
File : pre_commit_hook.py

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

<---------------------------------------------------------------------->


HOW TO EXECUTE PULL SCENARIO FOR LARGE FILES
File : git_pull.py

If you performed above steps of push scenario
then you only need to run command "pyton3 git_pull.py"

S3 Bucket content will be pulled and placed in the same directory where it should be or overwrite the content. 
 
