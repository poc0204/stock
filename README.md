# 上市個股資金流向
### TWSE Listed Company Stock Price
#### Website Url : https://pocworks.store/
#### Test Account
* ID:123@yahoo.com
* Password:1231231
# Main Features
* Show TWSE Listed Company Stock Price and TWSE funds ratio
* Member can add following stock to stock table 
# System Architecture
![流程圖](https://user-images.githubusercontent.com/93992949/174734841-491acab0-78f4-4980-b382-008c555b9d76.png)
# Member Login
![會員登入](https://user-images.githubusercontent.com/93992949/174734893-3489de2a-bf1f-4900-92ce-df598d92252e.png)
# Backend
* AWS EC2 for Server
* Docker for deploy website
* Python Flask for environment
* SSl and Https for secure website
* Nginx for reverse proxy
* AWS RDS Mysql for Database 
* BeautifulSoup4 and FinMind to get data 
* Python APScheduler auto send request to Server mon-fir to update date
* RESTfulAPI get and post data from Database
* Member login statement with JWT
* MVC design 
# Frontend
* HTML
* CSS
* Javascript
# Contact
* poc0204@yahoo.com.tw
