# Coffee Shop

Here's a link to the live project ()

-------

### Coffee Shop is the one stop coffee shop for all coffee drinkers out there. We serve the purpose of being able to deliver your favourite beans right to your door. We also serve a purpose of giving you the information you need about the different type of roasts. 

This project is built as a Full Stack Framework for e-commerce. 

## Content 

- User experiences 
* user stories 

- design 
* color and inspiration

- Features

- Technologies 
* libraries and languages

- testing (#testing.md)

- Deployment

- Credits 

--------

## User experience (UX)

-------

## User stories 

This is a list of my user stories, and it can also be found here (https://github.com/users/jessicafransson/projects/6)

### EPIC 
### EPIC
### EPIC
### EPIC 

----- 

## Design

### Color scheme 

### Images

- I've gotten my images from Gringo, which is also where i have gotten the inspiration for this website, and the information about their magical beans. 

### Wireframe

-------

## Features 

### Home page 
 navbar
 heroimage
 product view
 account
 about us
 the farm
 flavours 
 reviews
 shopping cart 


- #### Interactivity 

this is what the visitor can do on my site: 

------- 

- #### Footer information 

------

### Accounts 

- user registration

- user login 

- user logout

- user account information 

------

## Admin 

### Add products
### Add coupons 
### Edit products/coupons
### Delete products/coupons 

-----

## Technologies 

### languages used:

- HTML5
- CSS
- Python
- JavaScript 

### Libraries and programs used:

- Git, for version control.
- GitHub, for storing code and deploying site.
- Gitpod, Used to build project and editing the code.
- Django, a python based framework to develop this project
- Bootstrap, for HTML design templates.
- Cloudinary, to store images. 
- Figma, to mockup the design.
- ElephantSQL, database through Heroku.
- W3C for validation of HTML and CSS.
- Pep8CI for validation of Python.
- Summernote, for usage in the admin panel.
- Heroku, for deploying the project. 
- Convertion, for converting JPG to AVIF. 

## Testing 

Testing and results can be found [here] (testing.md)

## Creating repository

The project is deployed to Heroku from GitHub.
It is created in GitHub following these steps: 

    1. Log in to GitHub.
    2. Click the 'repositories' section.
    3. Pressed the 'new' button, this will create a new repository page.
    4. Choose the CodeInstitute template from the dropdown menu. 
    5. I choose a title for my project and pressed 'create repository'.
    6. Once this is created i opened the repository and pressed the green 'GitPod' button to create my workspace. 

## Deployment

### To deploy this project through Heroku i did following steps:

    1. Log in to [Heroku](https://www.heroku.com/)
    2. From the main Heroku dashboard select 'new', and 'create new app'
    3. Name your project, and select a suitable region. After this press 'create app'. (The name you choose must be unique)
    4. Previous step creates the app in Heroku and will bring you to the deploy tab. From the menu at the top you want to navigate to the resources tab. 
    5. After this you want to add the database to the app, you do this by going to the add-ons section and search for 'Heroku Postgres', select the package that appears and add it to the database. 
    6. Navigat3e to the settings, inside config vars you want to add the DATABASE_URL to the clipboard for the Django config. 
    7. Create a new file in GitPod called env.py and inside set your environment table for the DATABASE_URL and paste in the copied address from Heroku. 
    8. I created a secret key by adding SECRET_KEY in my env.py file, and in heroku. To get the secret key i typed 'openssl rand -base64 16' in my terminal. One time for a secret key to Heroku and a second time for a secret key to add in GitPod. 
    9. Create an account in Cloudinary, or log in if you already have an account. The url is found on your dashboard in your account. Copy this and add to your env.py file. 
    10. Paste it also into your Heroku config vars. 
    11. You now need to add 'KEY - DISABLE_COLLECTSTATIC' with the value of 1 to the config vars in Heroku, this line must be removed before final deployment of the project. 
    12. In GitPod you now have to add the cloudinary libraries to the list of installed apps in the settings file. The order here is important, 'cloudinary_storage' must go above 'django.contrib.staticfiles' and then 'cloudinary' goes below. 
    13. For your settings.py file you must also add the STATIC files, the url, storage path, directory path, root path, media url and the default file storage path. 
    14. You link this to the templates directory in Heroku with 'TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')'
    15. You also need to add new folders in GitPod. Create media, static and template folders and a file at the top level namned Procfile (the P has to be capital - important!)
    16. Inside the Procfile you need to add following: web: guincorn bakemeacake.wsgi.
    17. After adding these files, commit and push these changes to GitHub.
    18. In Heroku, go to the deployment tab and deploy this branch manually. This will lead to Heroku building this app for you, and you will be able to follow the build process in the window. 
    19. When successful, you will be displayed with following: "Your app was successfully deployed".

[Back to top (arrow)] ()

------

## Credits 

------

## Acknowledgements 