#!/usr/bin/python3
# Full Featured Web App Part 4 Database With Flask Sqlalchemy

"""
>>>> SQL Alchemy
        It is a popular ORM used for different databases.
        pip install flask-sqlalchemy
>>>> ORM
        Object Relational Mapper.
        Access the database in a object oriented way.
        You can use different databases without changing python code.
>>>> To create db.
        Open python shell in the current project.
        from flaskblog import app, db
        app.app_context().push()
        db.create_all()

        # Adding the user from the shell.
        from flaskblog import User, Post
        user_1 = User(username='Corey', email='C@demo.com', password='password')
        db.session.add(user_1)
        user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
        db.session.add(user_2)

        # Committing all changes.
        db.session.commit()

        # Querying the result.
        User.query.all()

        # Get the first user.
        User.query.first()

        # Filter the result.
        User.query.filter_by(username='Corey').all()
        user = User.query.filter_by(username='Corey').first()
        user.id

        # Getting the result with id.
        user = User.query.get(1)

        # Create a post.
        post_1 = Post(title="Blog 1", content="First Post Content!", user_id=user.id)
        post_2 = Post(title="Blog 2", content="Second Post Content!", user_id=user.id)
        db.session.add(post_1)
        db.session.add(post_2)
        db.session.commit()
        user.posts

        # Printing all post of the user.
        for post in user.posts:
            print(post.title)

        # Getting the first post.
        post = Post.query.first()
        post.user_id
        post.author

        # Delete everything from database.
        db.drop_all()
>>>>
"""
