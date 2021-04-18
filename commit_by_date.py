from datetime import datetime
import os

# target format: git commit -m "Add date <date> to README" --date="<date>"

with open("datestowrite.cvs") as infile:
    for x in infile:
        my_date = datetime.strptime(str.rstrip(x), '%Y-%m-%d')
        print(my_date)
        readmeFile = open('README.md', 'a')
        readmeFile.write(str(my_date) + '\n')
        readmeFile.close()
        os.system("git add README.md")
        commitMessage = f"""git commit -m "Add date {my_date} to README" --date="{my_date}" """
        os.system(commitMessage)
    os.system("git push")

