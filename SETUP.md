
# Instructions for applying the API

Basically, you need some IDE such as PyCharm with appropriate libs installed.
If you aren`t sure about having them, you can check their versions in a way like this:

`pip --version`

`django-admin --version`

or using the window in your IDE which contains the libs list that are in use.

In case of need to install libs, do this:

`pip install django`

`pip install djangorestframework`

`pip install django-rest-knox`

After this open the project, shift to root folder and start the server:

`python manage.py runserver`

If server is on air, you may open your localhost address in browser or app such as Postman.
Now you can work with database.

Supported urls:

	- GET /drivers/driver/ 				list of drivers
	- GET /drivers/driver/<driver_id>/		info by ID
	- POST /drivers/driver/ 			new driver
	- UPDATE /drivers/driver/<driver_id>/    	changing driver info by ID
	- DELETE /drivers/driver/<driver_id>/		delete by ID
	- GET /vehicles/vehicle/ 			list of vehicles
	- GET /vehicles/vehicle/<vehicle_id>/ 		info by ID
	- POST /vehicles/vehicle/ 			new vehicle
	- UPDATE /vehicles/vehicle/<vehicle_id>/ 	changing vehicle info by ID
	- DELETE /vehicles/vehicle/<vehicle_id>/ 	delete by ID

The urls for sorting the driver list considering date may be added soon.

File *db.sqlite3* contains some examples of models. 
Admin panel can be accessed through username/password *"admin"/"12345"*
