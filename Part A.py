import heapq
from datetime import datetime


class SocialMediaManager:
    def __init__(self):
        """
        Initialize the SocialMediaManager with an empty list of posts.
        """
        self.posts = []  # List to store posts as tuples (datetime, post_content, poster)

    def add_post(self, post_content, poster, datetime_value):
        """
        Add a new post to the social media manager.

        Args:
            post_content (str): The content of the post.
            poster (str): The person who posted the content.
            datetime_value (datetime): The datetime value of the post.
        """
        post_entry = (datetime_value, post_content, poster)
        heapq.heappush(self.posts, post_entry)

    def find_post_by_datetime(self, datetime_value):
        """
        Find a post by its unique datetime value.

        Args:
            datetime_value (datetime): The datetime value of the post to find.

        Returns:
            tuple or None: The post entry (datetime, post_content, poster) if found, else None.
        """
        for post in self.posts:
            if post[0] == datetime_value:
                return post
        return None

    def find_posts_in_time_range(self, start_datetime, end_datetime):
        """
        Find posts within a specific time range.

        Args:
            start_datetime (datetime): The start datetime of the time range.
            end_datetime (datetime): The end datetime of the time range.

        Returns:
            list: List of post entries (datetime, post_content, poster) within the specified time range.
        """
        posts_in_range = []
        for post in self.posts:
            if start_datetime <= post[0] <= end_datetime:
                posts_in_range.append(post)
        return posts_in_range

    def prioritize_by_views(self):
        """
        Prioritize social media posts by the number of views.

        Returns:
            tuple or None: The post with the highest views (based on post_content and poster) if any, else None.
        """
        if not self.posts:
            return None
        # Sort posts by views (number of characters in post_content)
        most_viewed_post = max(self.posts, key=lambda x: len(x[1]))
        return most_viewed_post


# Test Cases
social_media = SocialMediaManager()

# Adding posts with datetime values
social_media.add_post("Exciting news!", "Aysha", datetime(2024, 4, 21, 10, 30))
social_media.add_post("New recipe!", "Amal", datetime(2024, 4, 20, 15, 45))
social_media.add_post("Travel adventure!", "Afra", datetime(2024, 4, 22, 8, 0))

# Finding posts by datetime
found_post = social_media.find_post_by_datetime(datetime(2024, 4, 20, 15, 45))
print("Found post by datetime:", found_post)

# Finding posts in a time range
posts_in_range = social_media.find_posts_in_time_range(datetime(2024, 4, 20), datetime(2024, 4, 21))
print("Posts in time range:", posts_in_range)

# Prioritizing posts by views
most_viewed_post = social_media.prioritize_by_views()
print("Most viewed post:", most_viewed_post)