# Social Bookmark
Testing Django. Simple social app. It uses Redis to count views.

## Features

* User registration
* Login / logout
* Login with Facebook
* Forget password (send confirmation email, token)
* Change password (after logged in)
* Edit profile and set image profile
* It's possible to add a bookmark clicking on any page and select an image to bookmark
* View all images bookmarked, with infinite scroll paginator
* Like and unlike photos from users
* View all users
* View user profile and all bookmarks related
* Follow and unfollow users
* Users have own timeline, showing all the following users actions (bookmarked, liked, created account, follow/unfollow)
* Top Viewed Images, using redis to count the views
