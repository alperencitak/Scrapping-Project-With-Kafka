### **Web Scrapping App**
It is a docker + kafka + flask project that pulls the first page data from the site and then saves it to a file. In the application, data is transmitted as a message to the head at 1 second intervals. When the data transmitted on the first page is finished, the messages are written to a file called products.json. api/products endpoint provides access to the data in this file.

## Technology Stack
Docker + Kafka
Flask Framework

## ENDPOINTS
-/api/products GET

![Image](https://github.com/user-attachments/assets/cb3f01f6-94fd-4861-be8c-16e1e62dd0c4)

## CONTAINERS

![Image](https://github.com/user-attachments/assets/7cd97d73-d431-4f78-ade1-e413b1607447)
