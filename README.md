# rss-feed-open-ai
## Introduction
This project is a simple RSS Feed Database that allows users to add, parse, view all, read, find feeds in a specific website, delete, and classify feeds with OpenAI Completion API. The project has the following files: main.py, command.py, handler.py, database.py, and findfeed.py. The database is SQLite.

## Prerequisites
To use the project, you will need to have the following installed:

- Python 3
- feedparser
- openai

## Usage
The project is run using the main.py file. The user can use the following commands to interact with the database:

- **add**: Adds an RSS feed to the database
- **parse**: Parses an RSS feed and adds its items to the database
- **view_all**: Views all the added RSS feeds in the database
- **read**: Reads the added RSS feed items from the database
- **findfeed**: Finds an RSS feed on a website and adds it to the database if exists
- **delete**: Deletes an RSS feed from the database
- **classify**: Classifies the entries of an RSS feed with OpenAI Completion API. Add your OpenAI API key in handler.py to make that work. Currently only prints the completion result.

To run the project, navigate to the project directory in the terminal and run the following commands:

```python main.py parse https://www.yourfeed.com/xml```
    
```python main.py view_all```
    
```python main.py read https://www.yourfeed.com/xml```
    
```python main.py findfeed https://www.yoursite.com```
    
```python main.py delete https://www.yourfeed.com/xml```
    
```python main.py classify ttps://www.yourfeed.com/xml```


## Contributing
If you would like to contribute to the project, you can submit a pull request.

## License
The project is licensed under the MIT License.
