<h1 align="center">Lions Hotels.</h1> 

![View project](https://github.com/codigoenlaweb/lions_hotel/blob/master/static/img/imgreadme1.jpeg)

<div align="center">
    <a align="center" href="https://lionshotel.herokuapp.com/">View Demo</a>
</div>

## Table of Contents:
- About The Project
- Prerequisites.
- Installation
- Database design.
- Author
- Acknowledgments

## About The Project.
#### Description
Web application with Django, with which you can make a reservation in a hotel with a selected date range and with the possibility of choosing between different types of rooms, in addition to confirming the room through a verification code sent by email from asynchronously so as not to affect the performance of the server, and said code has an expiration time of 10 minutes, finally, when confirming a room, another new email will be sent to the user with a unique alphanumeric code where you can see your reservation with all the data of it.
#### Purpose of this project.
The purpose of this project was to present the technical test for the candidacy of django backend developer in the company [CHAPP Solutions](https://chappsolutions.com/es/ "CHAPP Solutions"). 
#### built with.
- Python
- Django
- Tailwindcss
- Javascript

## Prerequisites.
1. install Python.
2. install Pip.
3. VENV

## Installation.
This installation guide is based on the Ubuntu operating system.

1. We start by creating a new folder, in my case I will call it **project**.
2. We open the terminal in the project folder to be able to create our virtual environment, in my case I will call it **venv**.
   ```sh
   python3 -m venv venv
   ```
3. we proceed to clone the repository in **Github**.
   ```sh
   git clone https://github.com/codigoenlaweb/lions_hotel.git
   ```
4. We enter the virtual environment **venv**.
   ```sh
   source venv/bin/activate
   ```
5. We install the requirements in the virtual environment **venv**.
   ```sh
   pip install -r lions_hotel/requirements/local.txt
   ```
6. This project uses django-environ, within the application you will find the **.env.example** file, for practical reasons almost everything is filled in so that you only copy and paste in the **.env** file that They will be created in the root of the **lions_hotel** file at the same level as the **manage.py** (this is not a good practice since everyone should have their own environment variables following the **.env model. example** is only for practical purposes), it would only be necessary to add the **SECRET_KEY** that can be generated on this page.
[secret key generator](https://djecrety.ir/ "generador secret_key") 
7. We proceed to verify the result.
   ```sh
   python3 manage.py runserver
   ```
   
**You have assembled your project in django and you can now test it as much as you want**


------------

#### Do you want to change the styles to the page and add some new ones?
For this you should know that this project works with **tailwindcss** one of the most popular css frameworks and in particular my favorite since it has no limits when it comes to customizing it and giving it your special touch.

##### Below is the tailwind installation guide.
this project already has everything configured to be able to work with tailwind so it will be short.

1. Inside the **lions hotel** folder go to jstools.
   ```sh
   cd jstools/
   ```
2. npm install.
   ```sh
   npm install
   ```

3. npm run tailwind to work locally and npm run build before uploading to production.
   - Local
     ```sh
     npm run tailwind
     ```
   - Production
     ```sh
     npm run build
     ```
**Ready you have completed all the installation congratulations :)** 

## Database design.
[diagrama relacional](https://drive.google.com/file/d/1HpivqhYgemKfOTEcpf3FEgm9jLDR9sZW/view?usp=drivesdk "diagrama relacional")

## Author.
Jesus Olmos - [Linkedin](https://www.linkedin.com/in/jesus-armando-olmos-olmos-607748228/ "Linkedin") - olmosjesusarmando@gmail.com

## Acknowledgments.
Thank you **CHAPP Solutions** for giving me the opportunity to do this great technical test, which like everything and each one of the things I do, I put my heart, my signature, my personal touch and all the effort to reach the goal.

I hope that this application expresses a part of me and my love for my career, I have enjoyed doing it, I have learned and it has been another challenge in my path as a programmer.

