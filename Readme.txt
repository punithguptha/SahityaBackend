This is a simple WIP flask application for backend of Sahitya Project..

Activate env:
source /env/bin/activate

Install packages from requirements.txt

After installing the packages execute these below commands:
sudo mkdir /var/lib/pgadmin
sudo mkdir /var/log/pgadmin
sudo chown $USER /var/lib/pgadmin
sudo chown $USER /var/log/pgadmin

After these type pgadmin4 in the terminal and enter necessary details for it to start

Install postgres on mac: brew install postgresql@15

Start postgres server with this below:
brew services start postgresql@14


Create a PostGres Session now:
psql postgres -> To create a new postgres session

Then type execute these two sqls:
1. CREATE ROLE saipunithbonagiri WITH LOGIN PASSWORD 'password';
2. ALTER ROLE saipunithbonagiri CREATEDB;

Quit the session:
\q -> To quit postgres session


//Optional:
psql postgres -U saipunithbonagiri ->Login with earlier created user role
\du -> Displays the user details
psql ProjectDB -> Logs in to DB named ProjectDB
//





