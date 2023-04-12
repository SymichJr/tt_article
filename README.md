# tt_article
Service to create/update/read articles

### Install
Clone the project to the local machine, install the virtual environment and run it

Install all dependencies from a file ```requirements.txt```
```sh
pip install -r requirements.txt
```
### API
A few examples of interaction with the API:

http://127.0.0.1:8000/v1/articles
Request method: ```GET```
Get list of articles only without subscrtiption

http://127.0.0.1:8000/v1/articles_sub
Request method: ```GET```
Get list of articles only /w subscrtiption

http://127.0.0.1:8000/v1/subscribers/
Request method: ```post```
Create a subscriber user to read sub_articles
