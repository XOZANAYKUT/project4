# Culinary Academy

 [Culinary Academy](https://8000-xozanaykut-project4-cimyq6mphm4.ws-eu110.gitpod.io/)

Culinary Academy, is a culinary school and chef academy website. This project aims to offer users various cooking courses and chef training programs. By providing a wide range of culinary education opportunities, the website aims to help users enhance their cooking skills and pursue careers as professional chefs. Culinary Academy stands out with its high-quality educational programs, experienced instructors, and modern teaching methods, providing students with a creative and innovative learning environment.
____

![mockup](docs/images/mock.png)
____

## Existing Features
 
### Navigation Bar
- The fully responsive navigation bar on all pages contains links to the Home Page, About Us, search button, register, login pages and is located on each page to allow easy navigation.

- This section will allow the user to easily navigate from page to page on all devices without having to go back to the previous page via the 'back' button.

![nav](docs/images/nav.png)
____
## The Landing Page Image
- The homepage of Culinary Academy features basic course information along with images highlighting the company's areas of expertise. When a user clicks on a course URL, they are directed to a page providing detailed information about the course. Additionally, on this page, users can add and delete comments about the course, allowing for interactive engagement. 
- The visual elements effectively emphasize the firm's specialization areas, creating an engaging and informative experience for visitors.

![workspaces](docs/images/home.png)


### ABOUT 
- About Us section provides comprehensive details about the culinary courses and services offered by Culinary Academy. Each course is elaborated with further information to help clients understand the curriculum better. Moreover, visitors can explore the profiles of the academy's instructors, learning about their expertise and backgrounds. 
- For those seeking additional information, a contact form is available at the bottom of the page to facilitate further inquiries.
![aboutus](docs/images/about1.png)
____
![aboutus](docs/images/about2.png)
____
![aboutus](docs/images/about3.png)
____
 ### The Footer
 - The footer section of Culinary Academy's website features links to its relevant social media platforms, allowing users to easily connect and stay updated. These links are designed to open in a new tab, ensuring seamless navigation for the users. 
 - Additionally, the footer provides essential information such as the academy's working hours, enabling visitors to plan their interactions accordingly. 
 - Alongside the working hours, social media icons are prominently displayed, encouraging users to engage with the academy's content across various platforms.

![footer](docs/images/footer.png)
____
### Search
- "Search Section": On the Culinary Academy website, there is a search button in the header that allows users to easily find the content or courses they are looking for by entering keywords. Users can input keywords to perform a search. If search results are found, users can quickly access the results. However, if no results are found, users are notified with a message indicating that no results were found. This ensures a user-friendly experience.
![Search](docs/images/search1.png)
____
![Search](docs/images/search2.png)
____
![Search](docs/images/search3.png)

____
### Register
- Registering for Culinary Academy is quite easy! Here, they can take advantage of many benefits by creating a personalized account. All they need to do is choose a username, provide an email address, and select a strong password. Then, they can create their account and embark on an adventure filled with the world's most delicious dishes. After signing up, they can join various courses, receive special tips from chefs, and explore much more

![Register](docs/images/register.png)

___
### Login
- After logging in, users can browse through comments, leave their own feedback, and explore additional features on the site.

![Login](docs/images/login.png)
____

## Features Left to Implement
- To integrate a calendar for booking calls
- An application form for the internship programme
- Applying online for the course
- 

____

## Performance For Mobile

### Home page performance

![home](docs/images/mobil1.png)
____

### Courses  page performance
![Courses](docs/images/courses.png)
____
### About  page performance

![About](docs/images/about.png)
____

### Search page performance

![Search](docs/images/search.png)
____
![Search](docs/images/src.png)
____

### Register page performance

![Register](docs/images/rgr.png)
____
### Login page performance

![Login](docs/images/lgn.png)
____
### Logout page performance

![Logout](docs/images/sgn.png)
____


## Performance For Desktop

### Home page performance

![home](docs/images/desk.png)
____
### Courses  page performance
![Aboutus](docs/images/desk3.png)
____

### About  page performance
![Courses](docs/images/desk2.png)

____

### Search page performance

![Search](docs/images/desk5.png)
____
![Search](docs/images/desk4.png)
____

### Register page performance

![Register](docs/images/desk6.png)
____

### Login page performance

![Login](docs/images/desk7.png)
____
### Logout page performance

![Logout](docs/images/desk8.png)
____

## Data Model

- The Django model definitions provided down create models for a course and comments. The "Course" model represents a course created by a user, while the "Comment" model represents comments made on courses.

### The Course model has the following fields:

- title: The title of the course.
- slug: A unique URL tag for the course.
- author: A foreign key representing the author of the course. When a user is deleted, their associated courses are  automatically deleted.
- featured_image: The featured image for the course.
- content: The content of the course.
- date: The date of the course.
- duration: The duration of the course, which can be short-term or long-term.
- created_on: The date when the course was created.
- status: The status of the course, which can be draft or published.
- excerpt: A summary of the course.
- updated_on: The date when the course information was last updated.
____
## The Comment model has the following fields:

- course: A foreign key representing the course to which the comment is attached. When a course is deleted, associated comments are automatically deleted.
- author: A foreign key representing the author of the comment. When a user is deleted, their associated comments are automatically deleted.
- body: The content of the comment.
- approved: The approval status of the comment. By default, comments are set as unapproved.
- created_on: The date when the comment was create

## The About  model has the following fields:

- title: A CharField representing the title of the about section.
- updated_on: A DateTimeField automatically updated with the current date and time whenever the model is saved.
- profile_image: A CloudinaryField representing the image associated with the about section. It has a default value of 'placeholder'.
- content: A TextField containing the detailed content or description.
## model has the following fields:

- name: A CharField representing the name of the person making the collaboration request.
- email: An EmailField representing the email address of the person making the collaboration request.
- message: A TextField containing the message or details of the collaboration request.
- read: A BooleanField indicating whether the collaboration request has been read or not. It has a default value of False.
____
![data](docs/images/data.png) 
____
## Validator Testing
- HTML: No errors were found when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fprojectfour-1535055a6d4c.herokuapp.com%2F)
 - CSS: No errors found when passing through the official [(Jigsaw) validator
Deployment](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fprojectfour-1535055a6d4c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
____
## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:

- Log in to [Heroku](https://id.heroku.com/) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create 
- New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:
-  In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
-  Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file 
 storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

###
Add the following Config Vars in Heroku:

- SECRET_KEY value
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1
- DATABASE_URL 

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy - Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.
- The site is now live and operational.

    + [Local Deployment](#local-deployment)
    + [Heroku Deployment](#heroku-deployment)-
    + [django-aullauth Setup](#django-aullauth-setup)
    + [cloudinary Setup](#cloudinary-Setup)
    + [ElephantSQL Setup](#ElephantSQL-Setup)

- The live link for Heroku can be found here - https://projectfour-1535055a6d4c.herokuapp.com/
   
____
## Credits

### Content
-  Instructions on how to apply form verification on the Register page are taken from 
[Btkakademi](https://www.btkakademi.gov.tr)
[Bootstrap](https://getbootstrap.com/)
[w3schools](https://www.w3schools.com/)

### Media
- Images used on homepage and registration page are taken from [instagram](https://www.instagram.com/)

- The image used for the About Us page was taken from[instagram](https://www.instagram.com/)
  
- The image used for the return page was taken from the website [instagram](https://www.instagram.com/)

- Favicon was downloaded at [Icons8](https://icons8.com/icons/set/book)

- Icons in the Login taken from
[Font Awesome](https://fontawesome.com)

- Icons in the footer taken from
[Font Awesome](https://fontawesome.com)