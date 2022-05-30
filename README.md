# Github-repo-commit-art
This repository lets you use your GitHub commit views as a pixel canvas. Simply click on the puttons / dates you want 
to draw on. If you are finished click on push (Bottom left).

## What? Why?!
Did you know that you can specify the commit dates in Git?
I did not!
Seeing that i did not commit anything in a long time on the commit statistics i hatched a plan.
These commit statistics look like a dotmatrix dont they?
![There is something missing here!](doc/img/empty_commit_statistics.PNG?raw=true "Empty statistics")
Let us draw on them!

## How Do I Use This?
This code is tested with **python 3.9.1**. Other versions might work but i can not guarentee this.

### Fork This Repository
Fork this repository by clicking the fork button on GitHub.
After that clone your forked repository.

### Install Dependencies
Simply install the dependencies by typing
`pip install -r requirements.txt`

### Define Current Date in Source
Update the date defined for `my_date` in the source file **commit_using_ui.py**.
As for now, you need to define the date shown on your statistics in the top left.

**Failing to define this date properly will cause the graphic to be shown on GitHub at the wrong place**

### Run the Code
Type 
`python commit_using_ui.py`

The following UI will show up:
![There is something missing here!](doc/img/Empty_ui.PNG?raw=true "Empty UI")

Klick on the buttons representing the days you want to commit on.
*Take a look at the terminal, you will see which date you have selected here!*

After you are done selecting the days you want to commit on simply click push.
*This is the button on the bottom left of the screen.*

![There is something missing here!](doc/img/Testing_ui.PNG?raw=true "Testing written in UI")

The selected dates will be committed and pushed.
*This might take a few moments, you can see the progress in your terminal.*

Take a look at your profile and enjoy.

![There is something missing here!](doc/img/Github_test.PNG?raw=true "Testing as commits on GitHub")

##### Following are the dates used for testing so far.
2021-03-15 00:00:00
2021-03-16 00:00:00
2021-03-17 00:00:00
2021-03-18 00:00:00
2021-03-19 00:00:00
2021-03-22 00:00:00
2021-03-29 00:00:00
2021-04-05 00:00:00
2021-03-24 00:00:00
2021-03-31 00:00:00
2021-03-26 00:00:00
2021-04-02 00:00:00
2021-04-09 00:00:00
2021-04-20 00:00:00
2021-04-21 00:00:00
2021-04-23 00:00:00
2021-04-26 00:00:00
2021-04-28 00:00:00
2021-04-30 00:00:00
2021-05-03 00:00:00
2021-05-06 00:00:00
2021-05-07 00:00:00
2021-05-17 00:00:00
2021-05-24 00:00:00
2021-05-31 00:00:00
2021-06-01 00:00:00
2021-06-02 00:00:00
2021-06-03 00:00:00
2021-06-04 00:00:00
2021-06-07 00:00:00
2021-06-14 00:00:00
2021-04-19 00:00:00
2021-05-05 00:00:00
2021-06-28 00:00:00
2021-07-05 00:00:00
2021-07-12 00:00:00
2021-07-06 00:00:00
2021-07-07 00:00:00
2021-07-08 00:00:00
2021-07-02 00:00:00
2021-07-09 00:00:00
2021-07-16 00:00:00
2021-07-26 00:00:00
2021-07-27 00:00:00
2021-07-28 00:00:00
2021-07-29 00:00:00
2021-07-30 00:00:00
2021-08-03 00:00:00
2021-08-11 00:00:00
2021-08-19 00:00:00
2021-08-27 00:00:00
2021-08-26 00:00:00
2021-08-25 00:00:00
2021-08-24 00:00:00
2021-08-23 00:00:00
2021-09-07 00:00:00
2021-09-08 00:00:00
2021-09-09 00:00:00
2021-09-13 00:00:00
2021-09-16 00:00:00
2021-09-17 00:00:00
2021-09-20 00:00:00
2021-09-24 00:00:00
2021-09-27 00:00:00
2021-09-29 00:00:00
2021-10-01 00:00:00
2021-10-04 00:00:00
2021-10-06 00:00:00
2021-10-07 00:00:00
2021-10-08 00:00:00
2021-10-18 00:00:00
2021-10-19 00:00:00
2021-10-20 00:00:00
2021-10-22 00:00:00
2021-12-20 00:00:00
2021-12-21 00:00:00
2021-12-22 00:00:00
2021-12-23 00:00:00
2021-12-24 00:00:00
2021-12-29 00:00:00
2022-01-05 00:00:00
2022-01-10 00:00:00
2022-01-11 00:00:00
2022-01-12 00:00:00
2022-01-13 00:00:00
2022-01-14 00:00:00
2022-01-24 00:00:00
2022-01-25 00:00:00
2022-01-26 00:00:00
2022-01-27 00:00:00
2022-01-28 00:00:00
2022-01-31 00:00:00
2022-02-02 00:00:00
2022-02-04 00:00:00
2022-02-07 00:00:00
2022-02-11 00:00:00
2022-02-21 00:00:00
2022-02-22 00:00:00
2022-02-23 00:00:00
2022-02-24 00:00:00
2022-02-25 00:00:00
2022-03-04 00:00:00
2022-03-11 00:00:00
2022-03-21 00:00:00
2022-03-22 00:00:00
2022-03-23 00:00:00
2022-03-24 00:00:00
2022-03-25 00:00:00
2022-04-01 00:00:00
2022-04-08 00:00:00
2022-04-19 00:00:00
2022-04-20 00:00:00
2022-04-21 00:00:00
2022-04-25 00:00:00
2022-04-29 00:00:00
2022-05-02 00:00:00
2022-05-06 00:00:00
2022-05-10 00:00:00
2022-05-11 00:00:00
2022-05-12 00:00:00
2022-05-31 00:00:00
