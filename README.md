# Photo App

This application enables users to upload and view uploaded pictures.

## Getting Started

Download the repository or use git clone to get a copy of the project on your system.
```
git clone https://github.com/shivani-nadkarni/photo_app.git
```
### Prerequisites

Run reqirements.txt to install python libraries.
```
pip install -r requirements.txt
```
Install postgreSQL.
```
apt-get install postgresql
```
Change the database URL accordingly. For postgreSQL, we have default user as 'postgres' and no default password. You can set password for the same. I have set 'postgres' as password 

You can then set environment variables for database URL and secret key as follows.
```
export DATABASE_URL="postgresql://postgres:postgres@localhost/photo_app"
export SECRET_KEY='1234sasdf//;;'
``` 
To create the database, open python interpretor.
```
python3
```
Then type the following the create the database.
```
from photo_app.routes import database
from photo_app.db import User, Photo, create_db

create_db()
```

### Installing

To start flask server, run the following command in the base folder.
```
python3 -m photo_app
```

### Demo

You can sign in the portal by using the below credentials:
username -- guest
password -- guest

Once logged in, upload pictures by browsing picture of you choice and then click on upload.
All uploaded pictures can be viewed through the thumbnails or by clicking the image links.

Once done, you can logout the portal by clicking 'Logout' on the top right corner. 

## Authors

Shivani Nadkarni - https://github.com/shivani-nadkarni


## Acknowledgments

Thanks to viren-nadkarni for guiding and inspiring to build this - https://github.com/viren-nadkarni

