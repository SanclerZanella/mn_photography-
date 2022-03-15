import os


os.environ["DJANGO_SECRET"] = "Your Django Secret"
os.environ["INSTA_USER"] = "Your Instagram User"
os.environ["INSTA_PASSWORD"] = "Your Instagram Password"

# This variable should not be added in production
os.environ["DEVELOPMENT"] = "true"
