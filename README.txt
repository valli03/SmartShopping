# README

SMARTSHOPPING

When a customer goes to a shopping mall, he/she would like to know the best deals available for the product that they wish to buy. Once they get to know the price of the product in each store, they would compare it with the price of the product in Amazon. This comparison will help them in deciding as to where they should buy this product. Therefore, the objective is to help customers in providing information about better deals available for a particular product in a shopping mall and also the deals available online at the click of a button.

LANGUAGES USED:

* Ruby on Rails
* PHP
* Python

INTERNET PROTOCOLS:
* HTTP
* TCP

CAPTIVE PORTAL SETUP:
1. Download pfsense iso-image from official website of pfsense
2. Load the image in one setup (virtual machine)  and run the configuration as FreeBSD
3. Set the Network Interface as Internal Network and Bridged Adapter
4. Once the installation is complete, set the LAN and WAN IPs in the pfsense environment
5. Access web-configurator of the pfsense using https://<LAN_IP>/
6. Go to services-> Captive Portal and configure LAN interface and populate the redirection URL field pointing to our shopping website URL.
7. On another system (VM) with Internal network interface same as that of pfsense, open the browser where you are greeted with the captive portal login page.
8. Enter email id and click on continue, then you are redirected to the shopping website.


WEBSITE SETUP:

1. Use two systems (two virtual machines - one for server and one for client)
2. In the client, clone the github repository: https://github.ncsu.edu/vannama/SmartShopping.git or copy the contents of the client directory
3. Install Ruby and Rails in the client virtual machine
4. Go to the SmartShopping directory and run "#bundle install"
5. Start the rails server by executing the command "#rails s"
6. Rails server runs in port 3000. So start the php server in another terminal in port 3001, using the following command:
   #php -S localhost:3001
7. In the second virtual machine, install mysql database server
8. Put the server.py file from the server directory in the second virtual machine
9. The client.py file will be called by the php script whenever a search is made in the website
10. When the client file gets executed, the search query is taken as input and passed to the server running in the second virtual machine
11. The server queries its local mysql database and returns the data to the client
12. The client sends the data to the PHP script which outputs the content to the HTML page.   

HOW TO RUN THE APPLICATION:

1. Connect to the network and open browser.
2. In the login page enter email id and click continue.
In VM1:
1. Open terminal where the application is installed and run "rails s"
2. Open terminal and run "php -S localhost:3001"
In VM2:
3. Go to the location where server.py file is saved and run "python server.py"
In VM1:
4. Go to browser and hit: 127.0.0.1:3000
5. In the search text box, type a product name and hit Search
6. Search.html page will be rendered with data from local sqlite3 db and remote mysql db