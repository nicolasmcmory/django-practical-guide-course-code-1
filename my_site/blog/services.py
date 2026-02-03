from django.shortcuts import render
from django.urls import reverse
from datetime import date


class Posts:

    def __init__(self):
        self.posts = {
            "first-post": {
                "title": "My First Post",
                "published_date": date(2021, 10, 1),
                "content": "This is my first blog post.",
                "image": "first_post.jpeg",
            },
            "second-post": {
                "title": "Another Post",
                "published_date": date(2024, 10, 1),
                "content": "Here's some more content in another post.",
                "image": "second_post.jpeg",
            },
            "third-post": {
                "title": "Yet Another Post",
                "published_date": date(2026, 10, 1),
                "content": "This is yet another blog post for demonstration.",
                "image": "third_post.jpeg",
            },
            "fourth-post": {
                "title": "The Fourth Post",
                "published_date": date(2022, 10, 1),
                "content": "Continuing the series with a fourth post.",
                "image": "fourth_post.jpeg",
            },
        }

    def get_post(self, post_slug):
        return self.posts.get(post_slug)

    def get_posts(self):
        return self.posts

    # Get recent posts with a default count of 3
    def get_recent_posts(self, count: int = 3) -> dict:
        return dict(
            sorted(self.posts.items(), key=lambda item: item[1]["published_date"], reverse=True)[
                :count
            ]
        )
