# Ethereum-Block-Updater
A Flask App that shows last 3 blocks mined and pending transactions in the current block.
This is just something I created to learn my way around infura. And also practice using Flask with Ethereum.
web3.py is the file where all the data is obtained from the Infura URL.
server.py is where the Flask app runs.
Ignore the main.css file. I was having trouble applying css styles via linking it to the html file. The table just wouldn't change. So I added all the css in the html file.
Later I will figure how to apply css from main.css.
The page refreshes every 20 seconds to load new pending transactions and the latest block.
Only "last 3 blocks" are displayed but this could be modified to display as many blocks as one wants, without maxing out on the infura limit.
I have displayed only few relevant details of the blocks and transactions. Many other parameters can be displayed, however it will make the table columns unsightly and 
long for the UI.

