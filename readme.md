# Smart Budget

Welcome to the README for Smart Budget! :money-with-wings:

This document will provide you with a brief overview of the application and its functionalities, as well as instructions for installation and usage.

## Overview
This application is designed to have a handy simple way to maintain and manage a budget
### Its main features include:
1. viewing current budget
2. adding items to the budget
3. editing items in the budget
4. deleting items from the budget

## Installation
To install the application, follow these steps:
1. run the command in any folder you would like:
```git
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-III/budget-app
```
2. startup docker desktop
3. run the command:
```docker
docker-compose up
```
## Usage
To use the application, follow these steps:
1. enter http://localhost:8000/docs in your browser
2. various features of the app are:
    1. get("/budget_item/") to view the budget
    2. get("/budget_item/id") to view each item's id
    3. get("/budget_item/id/{item_id}") to view spesific items data
    4. get("/budget_item/tag") to view all item's tags
    5. get("/budget_item/tag/{item_tag}") to view all items with spesific tag
    6. post("/budget_item/") to add an item to the budget
    7. put("/budget_item/{item_id}") to edit an item with the specific id
    8. delete("/budget_item/{item_id}") to delet an item with the spesific id from the budget

## Support
If you encounter any issues with the application or have any questions, please contact email address orshaharr@gmail.com

## License
This application is licensed under Public domain.