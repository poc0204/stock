# 上市個股資金流向
### TWSE(Taiwan Stock Exchange) Listed Company Funds Ratio
#### Website Url : https://pocworks.store/
#### Test Account
* ID: 123@yahoo.com
* Password: 1231231
# Main Features
* Show TWSE Listed Company Funds Ratio and Stock Price
* Member can add following stock to stock table 
# System Architecture
![流程圖](https://user-images.githubusercontent.com/93992949/174955708-ec1e1e33-b828-4dff-a7b7-0d10d2687e23.png)
# Backend
* Python
  * Flask for environment
  * BeautifulSoup4 and FinMind to get data
  * APScheduler auto send request to Server mon-fir to update date
* AWS 
  * EC2 for Server
  * RDS MySQL for Database 
* Docker
  * Deploy website
* Nginx
  * SSL and Https for secure website
  * Reverse proxy
* Others
  * RESTfulAPI interface FrontEnd and BackEnd
  * Member login statement with JWT
  * MVC design 
# Frontend
* HTML
* CSS
* Javascript
# Demo
![stock_k](https://user-images.githubusercontent.com/93992949/175454754-f5437da4-f559-44ea-9fd3-3f49d2d6950c.png)
![stock](https://user-images.githubusercontent.com/93992949/175454761-a0d8d6c2-0438-455b-9ee9-b2fa4dc7cbab.png)

# Contact
* 張郡驛 Joe
* Email: poc0204@yahoo.com.tw
