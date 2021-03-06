# Order_delivery
A simple order delivery API app using Python, Django, Django Rest Framework

## Features
- [x] Order Calculator
- [ ] List items
- [ ] Add to cart feature
- [ ] Save orders to database
- [ ] Order Tracking

## Demo
This Django application is hosted on aws ec2 instance in <b>DEBUG</b> mode and it can be accessed [here](http://ec2-15-207-115-148.ap-south-1.compute.amazonaws.com/api/calculate-order/). It is hosted using Nginx, Supervisor, Gunicorn.

## Usage
1. Clone this repository
```
git clone https://github.com/ShreehariVaasishta/order_delivery
```
2. Go to the root directory of this project
```
cd order_delivery
```
3. Install the dependencies using `pip`. Activate [virtual environment](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html) if you use one.
```
pip3 install -r requirements.txt
```
3. Create a `.env` file and make sure the following variables are set
```
DJANGO_SECRET_KEY=
DEBUG=
```
4. Start the django server 
```
./manage.py runserver
```
OR
```
python3 manage.py runserver
```
Now you should be able to access the Django app running [locally](http://127.0.0.1:8000/) at port 8000. Additionally you can specifiy the port for the django app to run in local
```
./manage.py runserver 0.0.0.0:8080
```
Now the Django app will be accessible at port 8080
## Testing
Few basic test cases are already included for the existing order calculation API which inherits Django's `TestCase` class. <br />
To run those test cases, run the following command
```
./manage.py test 
```
OR
```
python3 manage.py test
```
Test case results will be displayed in the terminal.

# Tech Stack (Programming Language, Framework(s))
* Python
* Django
* Django Rest Framework

# Technical Decisions
1. Added type annotations and comments everywhere which improves code readability
2. Used DjangoRestFramework's serializers to validate the request body. Which keeps code readable, modularised and also maintainable.
3. Used python dictionaries to store distance range and price allotted to the respective distance.
4. Moved utility functions to utility folder. This should keep them easily accessible instead of searching the whole file.
5. Constants have a dedicated file in the app which might not change frequently.

# Screenshots
1. With FLAT offer
![Flat](./demo-images/order-1.png)
2. With DELIVERY offer
![Delivery](./demo-images/order-2.png)
3. Without OFFER
![No offer](./demo-images/order-3.png)
4. Order 4
![Order 4](./demo-images/order-4.png)
5. Order 5
![Order 5](./demo-images/order-5.png)
6. Order 6
![Order 6](./demo-images/order-6.png)
