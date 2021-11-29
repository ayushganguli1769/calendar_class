# Eduvation: My Microsoft Engage Ace Hackathon Project
Eduvation is an online education forum. This forum helps in task management and task planning.
This education forum allows teachers to upload tasks,assignemnts and students to submit task.
## Important Links

<table>
<tr>
<th> Live URL</th>
<td><a href="http://eduvatemeeducation.pythonanywhere.com/"> Website Link</a> </td>
</tr>
<tr>
<th> Demo Video</th>
<td> <a href="https://www.youtube.com/watch?v=epG3aRdHjBs">Video Link </a></td>
</tr>
</table>

## How to test the live url?

You can login using the faculty username cse_faculty1 and password 1234. For testing the student model use username cse_student1 and password 1234. Previously uploaded media files during development won't work for now. While uploading media files please use small txt files.

## Problems it Solves:

### Respeated Need for Class Codes
Online Learning Platform repeatedly needs class codes. For a course like engineering with 70+ classes including practical,
joining classes again and again is not a good idea. I have categorized classes into batches. For instance NIT Raipur IT 2022 can be a batch and classes can be DBMS class, OS class, OOPs class, etc

### Poorly Planned Tasks
Teachers aren't aware schedule of other classes. Often assignment/task submissions are concentrated in a few days. 
I have helped teachers distribute load using a calendar based interactive ui.
It considers stress from same day, previous days and next days for a particular day. It helps faculties decide the submission date by task stress management

## Tech Stacks Used

<table>
<tr>
<th> Backend</th>
<td>  Python Django </td>
</tr>
<tr>
<th> Frontend</th>
<td> JavaScript(fetch api), Jquery,Bootstrap 5, CSS, HTML </td>
</tr>
 <tr>
<th> Backend</th>
<td> PostgreSQl(sqlite locally), Firebase </td>
</tr>
</table>

## Feature List

<table>
<tr>
<th> User Models</th>
<td> I have created two user models faculties and students with seperate functionalities</td>
</tr>
<tr>
<th>Join/ Create</th>
<td> Teachers can join batch. On being part of batch they have view only access i.e they can view tasks created by other faculties and submissions by students.
On joining a class, faculties can create tasks and grade submissions for that class. Students can either join batch to join all classes in it or join a class anonymously to 
not be a part of other classes in that batch.
</td>
</tr>
<tr>
<th> Plan Tasks</th>
<td>
This feature is for faculties only. If faculties want to choose deadline for task within a range, they can consider stress due to other tasks from other classes. On a particular day 
we consider stress due to tasks on same day, days preceding it and days after it as specified. It generates a coloured heat map with red meaning not a good day and green meaning good day.Optimal 
day is also calculated.
</td>
</tr>
<tr>
<th> Create Tasks</th>
<td>
Fully built in editor to create tasks for a class. Multiple files can be uploaded. Teachers of a class can create task.
</td>
</tr>
<tr>
<th> View Tasks</th>
<td> Teachers and students can view tasks created </td>
</tr>
<tr>
<th>Submit Tasks</th>
<td>
Students can submit their work as multiple files.
</td>
</tr>
<tr>
<th>View Submissions</th>
<td> Teachers of the same batch as that as class of task can view submissions submitted by students</td>
</tr>
<tr>
<th>Grade Tasks</th>
<td> Only teacher with same class as that of task can grade submissions to tasks</td>
</tr>
<tr>
<th> Hierarchial Navigator</th>
<td> Data Table based navigator with search and sort filters to navigate between batch, class, tasks, submissions.
</tr>
</table>

## Screenshots

### Home Page
![image](https://user-images.githubusercontent.com/53971272/143778966-b194876d-20ab-4068-a139-917ee0fae6bb.png)

### Join Create View
![image](https://user-images.githubusercontent.com/53971272/143778993-481a990f-0d51-47d3-811f-f054e49eee63.png)

### Interactive Calendar Based Task Planner
![image](https://user-images.githubusercontent.com/53971272/143780400-b033e083-e453-45a6-850a-f3e0fe40232c.png)

### Task Creator
![image](https://user-images.githubusercontent.com/53971272/143779059-2910b2ae-8194-4536-915d-b2d6fe7d7d29.png)

### Hierarchial Views
![image](https://user-images.githubusercontent.com/53971272/143779102-52b7a7aa-0ec0-4c7d-b420-c3d9eeff85ee.png)

## How to run this project?
```bash
  pip install virtualenv
  virtualenv .
  .\scripts\activate
  git clone https://github.com/ayushganguli1769/calendar_class.git
  cd calendar_class
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
 ```

</br> Type the following url in your web browser to run it locally http://127.0.0.1:8000/  </br>



