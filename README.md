Scrapy Spider for www.productindetail.com
This README file provides instructions on how to run the Scrapy spider for scraping phone data from the website www.producinndetail.com and storing the collected data in a MongoDB database running on your localhost.

Prerequisites
Before you can run the Scrapy spider and set up the MongoDB database, make sure you have the following prerequisites installed on your machine:

Python (3.6 or higher)
Scrapy
MongoDB
pymongo (Python library for MongoDB)
You can install Scrapy and pymongo using pip:

bash
Copy code
pip install scrapy pymongo
Setting Up MongoDB
Install MongoDB: If you haven't already installed MongoDB, please follow the installation instructions for your specific operating system from the official MongoDB website: https://docs.mongodb.com/manual/installation/

Run MongoDB: Start the MongoDB server on your machine. You can usually do this by running the mongod command in your terminal.

Create a Database: Use the MongoDB shell or a GUI tool like MongoDB Compass to create a new database named "phone_data" and a collection named "phones" within it.

Running the Scrapy Spider
Follow these steps to run the Scrapy spider:

Clone the Repository: If you haven't already, clone the repository containing the Scrapy spider code.

Navigate to the Spider Directory: Open a terminal and navigate to the directory where the Scrapy spider code is located.

Configure the Spider: In the phones/phones/spiders/phones_spider.py file, make sure to set the MONGO_URI and MONGO_DATABASE variables to match your MongoDB configuration.

python
Copy code
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'phone_data'
Run the Spider: Run the Scrapy spider using the following command:
bash
Copy code
scrapy crawl phones
The spider will start scraping phone data from www.producinndetail.com. It will crawl multiple pages if pagination is available on the website.

Check MongoDB: After the spider completes its job, you can check your MongoDB database to see the collected phone data in the "phones" collection.
Important Notes
The Scrapy spider is named "phones" and targets the main page of www.productindetail.com.

The spider extracts data for each phone, including product name, brand, description, operating system, display technology, and image URL.

Please respect the website's terms of service and scraping policies while running this spider. Make sure your scraping activity is in compliance with the website's rules.

The spider may require adjustments if the website's structure changes in the future.

Ensure that your MongoDB server is running before running the spider, and double-check the MongoDB configuration in the spider script.

By following these instructions, you can scrape phone data from www.productindetail.com and store it in a MongoDB database on your localhost.
