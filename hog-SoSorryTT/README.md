## Hog Application

This repository contains code for the [Hog Project][hog]
from the UC Berkeley CS61a course.

### What to Do

1. Complete the code for [The Game of Hog][hog] as described at the link.

2. [Test your code](#test-your-code) frequently.

3. [Save and submit your work](#save-and-submit-your-work-using-git) regularly using Git -- do this everytime you work on something, not just when you finish the assignment.

### Test Your Code

`hog.py` contains doctests in comments that you can run using:
```
python3 -m doctest hog.py
```
Any failures (expected result not same as actual result) are shown on the console.

Use the `ok` program included with the code to better test your
program, as described in the [Hog assignment][hog].


### Save and Submit Your Work Using Git

Use Git to regularly add work to your local repository and then send it to Github.  This is a good software development practice and protects you from losing work.

The commands are:

1. Check what files you have changed:
   ```
   git status

   Modified files:
      hog.py
      .ok_history
   ```
2. Use `git add` to tell git you want to save the modified files or add new files:
   ```
   git add hog.py .ok_history
   ```
3. Commit the files to your local repository:
   ```
   git commit -m "write a message describing what work you did"
   ```
   Or, combine step 2 and step 3 into one command:
   ```
   git commit -am "write a message describing what work you did"
   ```
4. Copy your local repository updates to Github:
   ```
   git push
   ```
5. Visit your repository on Github to verify your new work is there!

### What to Submit

You should "push" (upload) your code to Github.

You can "push" your code many times until the project deadline.

### Git

You need the "git" client program on your computer
and added to your environment's PATH.

Get Git from <https://git-scm.com/downloads>.


[hog]: https://cs61a.org/proj/hog/
