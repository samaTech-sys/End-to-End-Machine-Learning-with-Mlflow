import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="2.9.2"

REPO_NAME = "End-to-End-MAchine-Learning-with-MLflow"
AUTHOR_USER_NAME = "colline"
SRC_REPO = "test_mlflow" #here back
AUTHOR_EMAIL = "collinetazuba@gmail.com"

setuptools.setup(
    name=SRC_REPO,  # ✅ Avoid conflict with the real mlflow package
    version=__version__,  # ✅ Add a version to your project
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python project for ML app", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", 
    }, 
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
