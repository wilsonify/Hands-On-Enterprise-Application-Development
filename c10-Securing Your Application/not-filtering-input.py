

username = request.args.get('username')
email = request.args.get('email')
password = request.args.get('password')
user_record = User(username=username, email=email, password=password)
# Let's create an object to store in database
# Let's store the object into the database
db.session.add(user_record)
db.session.commit()
