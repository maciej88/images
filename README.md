# images
Recruitment task

django rest view for management small database (data is storage in local database - sqlite3) views:
- rest/ - rendered list with button for create new record in database 
(values viewed: id, album id, link (only for local storage),width and height of image)
- rest/id - details with possibility of update, and delete record
- rest/create - for new record
- possibility of filling database from JSON link:
https://jsonplaceholder.typicode.com/photos by command from folder "python db_fill.py"
- unfortunately not done: calculating HEX dominant color, save correct photo patch from external link in to local db.
- secret key in .env