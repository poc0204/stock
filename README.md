# 上市個股資金流向
### TWSE Listed Company Funds Ratio
#### Website Url : https://pocworks.store/
#### Test Account
* ID:123@yahoo.com
* Password:1231231
# Main Features
* Show TWSE Listed Company Funds Ratio and Stock Price
* Member can add following stock to stock table 
# System Architecture
![流程圖](https://user-images.githubusercontent.com/93992949/174955708-ec1e1e33-b828-4dff-a7b7-0d10d2687e23.png)
# Backend
* AWS EC2 for Server
* Docker for deploy website
* Python Flask for environment
* SSL and Https for secure website
* Nginx for reverse proxy
* AWS RDS MySQL for Database 
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
* 張郡驛 Joe
* Email:poc0204@yahoo.com.tw
