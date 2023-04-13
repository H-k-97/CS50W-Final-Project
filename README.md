# CS50W Final Project

### Overview
- My Final Project on CS50's Web Programming with Python and JavaScript is about Patients Medical History that add and store data and informations for the Patients by the doctors , It can be used by Small and medium clinics with full basics and Histories .

- The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database.

- All webpages of the project are mobile-responsive.

#### Distinctiveness and Complexity

- This project can be very useful in terms of dealing with people who visit clinics or hospitals, the diagnosis is usually made anew every time, with a database and a patient history, it will be very easy for doctors and not to repeat mistakes or repeat the diagnosis

- Using built in Models (SQL Database) to store the Patient information making the things goes well .

- I used QR Codes (qrcodes) Module in this project for any Patients added and re-read the QR again for Seraching Patients and easily reach the patient .

- I used bootstrap 5 for styling the webpages .

- As a programming style i used notes and the experience that i learned from the course (CS50W) it was really helpful .

- I made the Doctors can upload photos for the Patients to make the things well.

- Using javascript vanilla is really hard way to make things but still just fine without javascript frameworks .

- It is possible to use the application for non-medical purposes with some modifications in the future



#### Installation
  - Install project dependencies by running `pip install -r requirements.txt`. Dependencies include Django and Pillow  and qrcode with pyzbar module that allows Django to work with images and create & read QR Codes.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser with `python manage.py createsuperuser`. This step is optional.
  - Run the development server by running `python manage.py runserver`.
  - Go to website address and register an account.

#### Files and directories
  - `hospital` - main application directory.
    - `static/hospital` contains all static content.
         - `index.js` - script that run in `post.html` template.
         - `style.css` - contains compiled CSS file and its map.
    - `templates/hospital` contains all application templates.
        - `layout.html` - base templates. All other tempalates extend it.
        - `index.html` - main templates that shows index .
        - `login.html` - template that shows a login page.
        - `register.html` - this template shows reqgister page.
        - `browse.html` - template shows the add and browse patients.
        - `add_patient.html` - this page add new patient.
        - `patients.html` - this page shows all the patients
		- `patient_detail.html` - this page shows patients details.
		- `read.html` - this page read QR codes 
    - `admin.py` - here I added some admin classes and re-registered User model.
    - `models.py` contains three models I used in the project. `UserExtended` model extends the standard User model, `Patient` model is for Patient, and `History` represents users Histories.
    - `urls.py` - all application URLs.
    - `views.py` respectively, contains all application views.
  - `final_project` - project directory.
  - `media` - this directory contains two folders .
       - `images` - folder that saves all Patient Photos .
	   - `qr_codes` - folder that saves QR Codes images that are created .

#### At the End 
-  I Would to say thanks and appreciation to Professor (David J. Malan) and Professor (Brian Yu) for the useful course. I wish you success with all my heart Thank you .