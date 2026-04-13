from .. import models


class UserInterface:
    # get user by id
    def get_user_by_id(self, user_id):
        user = models.User.objects.get(id=user_id)
        return user

    # get user by email
    def get_user_by_email(self, email):
        user = models.User.objects.get(email=email)
        return user

    # Get user by first name and last name
    def get_user_by_name(self, first_name, last_name):
        user = models.User.objects.get(first_name=first_name, last_name=last_name)
        return user

    # Get all users
    def get_all_users(self):
        users = models.User.objects.all()
        return users

    # Create a new user from form
    def create_user(self, first_name, last_name, email, image=None):
        user = models.User.objects.create(
            first_name=first_name, last_name=last_name, email=email, image=image
        )
        return user


class PostInterface:
    # Get post by id
    def get_post_by_id(self, post_id):
        post = models.Posts.objects.get(id=post_id)
        return post

    # Get all posts
    def get_all_posts(self):
        posts = models.Posts.objects.all()
        return posts

    # Create a new post from form
    def create_post(self, title, content, author):
        post = models.Posts.objects.create(title=title, content=content, author=author)
        return post

    # Get all posts by Author/User
    def get_posts_by_author(self, author):
        posts = models.Posts.objects.filter(author=author)
        return posts
