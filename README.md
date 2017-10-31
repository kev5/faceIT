# Face Recognition // Boston Hacks 2017

## Members

* Keval Khara
* Devin Dyson
* Brian Pham
* Amandeep Singh
* Amit Mangotra

## Inspiration

The National Health Care Anti-Fraud Association estimates that health care fraud costs the United States about $68 billion annually. Roughly 3% of the nation's $2.26 trillion annual health care expenditure.

The following data represents Blue Cross Blue Shield of Michigan's fraud investigation unit activity from July 1980 to March 2017.

Cases opened: 51,322 Cases closed: 50,324 Referred for recovery/cost savings: $402,716,325.25

According to these statistics there is a huge opportunity to implement a more substantial identity-verification process in Hospitals and Clinics for point of care service.

## What It Does

1. Create user (PatientID)
2. Train PatientID using OpenCV
3. Admin captures an image of the patient
4. OpenCV maps a PatientID to the image of patient
5. Displays stored patient information

## How we Built it

1. Create a virtual environment
2. Install the packages pip install -r req.txt
3. Python manage.py migrate python mange.py runserver and you're good to go on at localhost:8000

## Challenges Faced

Up until the near end of our project, we had split ourselves into two teams, one working on the facial recognition, the other working on the front and back-end. When it came time to combine our efforts, we had some problems integrating the facial recognition in a way that works well with the front and back-end developers. Also, the android application could not be completed in the given time as our planned minimum viable product was web application.

