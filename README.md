# schedule-python-script-using-Google-Cloud
**Use Case**: Automates live Chicago traffic data and flows it into BigQuery for interactive real-time analysis

**Technical Concept**: Schedules a simple Python script to append data into BigQuery using Google Cloud's App Engine with a cron job.

**Reference**: http://zablo.net/blog/post/python-apache-beam-google-dataflow-cron

Shout out to Mylin Ackerman for all his help. Saved me weeks of research with his personal touch.
https://www.linkedin.com/in/mylin-ackermann-25a00445/

**Order of Operations**:
1. Develop scripts with Google cloud shell or SDK
2. Deploy on appengine
3. Deploy cron job
4. Check BigQuery
5. Connect with dataviz tool such as Tableau

**Setup Prerequisites**:
1. Signup for Google Cloud account and enable billing
2. Enable BigQuery API, Stackdriver API, Google Cloud Deployment Manager V2 API, Google Compute Engine API, 

**Development Instructions**:
1. Copy github repository into SDK or Google cloud shell(thankfully it has persistent storage, so you don't have to recopy the folder structure)
2. 

**Deploy Instructions**:
1. Install all required packages into local lib folder: pip install -r requirements.txt -t lib
2. To deploy App Engine app, run: gcloud app deploy app.yaml
3. To deploy App Engine CRON, run: gcloud app deploy cron.yaml

**Document Context**:
appengine_config.py adds dependencies to locally installed packages (from lib folder)

app.yaml - definition of Google App Engine application

cron.yaml - definition of Google App Engine CRON job

main.py - entry point for the web application and calls the function contained within "append_data.py"

append_data.py - call the Chicago live traffic API and appends it into BigQuery

requirements.txt - file for pip package manager, which contains list of all required packages to run the application and the pipeline

lib - local folder with all pip-installed packages from requirements.txt file
