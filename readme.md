#  Performance Metrics API

## About
This API exposes a sample dataset through a single generic HTTP API endpoint, which is capable of filtering,
 grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a
  given date, advertising channel, country and operating system.
  
 This API is built using Django and Pyhton3.The sample dataset which has to be exposed using this API has been added to
 the project and it will populate the sqlite db in the time of migration.
  

 
## How to make this API running


* First clone this project
* Go to the root directory of the project
* Create a new virtual environment 
* Activate the virtual environment
* Install the required dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
* Now to migrate the database and populate the database with sample data-set run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```
* Now as the database is ready we can jump start the API. Run the following command to do so:
```bash
python manage.py runserver
``` 
* This will start the api in the following url:
```bash
http://127.0.0.1:8000/api/performance_metric/
```
 
## Use cases:

* Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and
 country, sorted by clicks in descending order.
 
 
 
```bash
    GET /api/performance_metric/?before_date=2017-06-01&group_by=channel,country&sort_by_clicks=desc
```



      
* Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending 
order.
 
 
 
```bash
    GET /api/performance_metric/?os=ios&after_date=2017-04-30&before_date=2017-06-1&group_by=date&sort_by_date=asc
```



* Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
 
 
 ```bash
    GET /api/performance_metric/?date=2017-06-01&group_by=os&country=us&sort_by_revenue=desc
```

    


* Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
 
 
 ```bash
    GET /api/performance_metric/?country=ca&group_by=channel,cpi&sort_by_cpi=desc
```
 




  