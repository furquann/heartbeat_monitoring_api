# heartbeat_monitoring_api
A Django REST Framework-based API for monitoring patients' heart rates.  This system provides endpoints for user authentication, patient management, and heart rate data tracking.




# **Features:**

* Custom User Authentication using Email
* RESTful API Endpoints
* Patient Management
* Heart Rate Monitoring
* Secure Password Handling
* Timestamp Tracking for Data



# **Installation**

Run these commands one by one:

**1. Clone the Repository:**
* git clone https://github.com/username/heartbeat_monitoring_api.git
* cd heartbeat_monitoring_api

**2. Create and Activate Virtual Environment:**
* python -m venv venv
* source venv/bin/activate  # On Windows use: venv\Scripts\activate

**3. Install Dependencies:**
* pip install -r requirements.txt

**4. Apply Migrations:**
* python manage.py migrate

**5. Create a Superuser (Optional, for Admin Panel):**
* python manage.py createsuperuser

**6. Run the Development Server:**
* python manage.py runserver



# **API Endpoints**

**1. Register a new user:**  
* POST /api/auth/register/  

**2. User Login:**  
* POST /api/auth/login/  

**3. Patients Management:**  
* GET /api/patients/ (List all patients)  
* POST /api/patients/ (Create new patient)  
* GET /api/patients/{id}/ (Get patient details)  
* PUT /api/patients/{id}/ (Update patient details)  
* PATCH /api/patients/{id}/ (Partially update patient details)  
* DELETE /api/patients/{id}/ (Delete patient)  

**4. Heart Rate Records:**  
* GET /api/heart-rates/ (List all records)  
* POST /api/heart-rates/ (Create new record)  
* GET /api/heart-rates/?patient_id={id} (Get patient's records)  
* GET /api/heart-rates/{id}/ (Get specific record details)  
* PUT /api/heart-rates/{id}/ (Update heart rate record)  
* PATCH /api/heart-rates/{id}/ (Partially update heart rate record)  
* DELETE /api/heart-rates/{id}/ (Delete heart rate record)  























