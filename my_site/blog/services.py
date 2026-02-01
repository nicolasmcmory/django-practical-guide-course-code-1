class Posts:

    def __init__(self):
        self.posts = {
            "first-post": {
                "title": "My First Post",
                "content": "This is my first blog post.",
            },
            "second-post": {
                "title": "Another Post",
                "content": "Here's some more content in another post.",
            },
            "third-post": {
                "title": "Yet Another Post",
                "content": "This is yet another blog post for demonstration.",
            },
        }

    def get_post(self, post_slug):
        return self.posts.get(post_slug)

    def get_posts(self):
        return self.posts
