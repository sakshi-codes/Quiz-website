# Quiz-website
This app is made using Django.It can be used to take Quizes.

# Specifications
<ul>
  <li>SQLite is used as a database.</li>
  <li>HTML,CSS,Javascript is used for frontend</li>
  <li>Python is used for backend.</li>
</ul>

## Screenshots:
![](https://github.com/sakshi-codes/Quiz-website/blob/main/screenshot/Capture.PNG)
![](https://github.com/sakshi-codes/Quiz-website/blob/main/screenshot/Capture1.PNG)
![](https://github.com/sakshi-codes/Quiz-website/blob/main/screenshot/Capture2.PNG)
![](https://github.com/sakshi-codes/Quiz-website/blob/main/screenshot/Capture3.PNG)
![](https://github.com/sakshi-codes/Quiz-website/blob/main/screenshot/Capture4.PNG)
## Functions:

## Admin:
- Create Admin account using command
```
py manage.py createsuperuser
```
- Can Add, View, Delete Quiz.
- Can Add Questions To Respective quiz With options and correct answer.
- Can also see result

## Student:

<ul>
  <li>Can Give Exam Any Time, There Is No Limit On Number Of Attempt.</li>
  <li>Can View Marks Of Each Attempt Of Each Exam.</li>
  <li>Question Pattern Is MCQ With 4 Options And 1 Correct Answer.</li>
</ul>

## HOW TO RUN THIS PROJECT

- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements. txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
