# Coffee Shop

Find my live deployed site [here](https://coffeeshop91.herokuapp.com)

-------

### Coffee Shop is the one stop coffee shop for all coffee drinkers out there. We serve the purpose of being able to deliver your favourite beans right to your door. We also serve a purpose of giving you the information you need about the different type of roasts. 

This project is built as a Full Stack Framework for e-commerce. 

The payment system used is a service called Stripe. To test the payments on this site, dummy card details can be used. A list of these can be found [here](https://stripe.com/docs/testing#cards)

## Content 

[User experiences (UX)]()
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

This is a list of my user stories, and it can also be found [here](https://github.com/users/jessicafransson/projects/8)

#### EPIC | Admin
- As an admin, i can access the products thru the admin site
- As an admin, i can add products to the site
- As an admin, i can add coupons for the site
- As an admin, i can edit/delete the products and coupons for the site
- As an admin, i can view the people signed up for my site

### EPIC | Navigation 
- As a user i can easily navigate around the site to view the different products and sections
- As a user i can view a list of products to select what to order
- As a user i can easily click a product to see more information
- As a user i can easily find out what previous buyers think

### EPIC | Customer
- As a user i want to be able to sign up for an account
- As a user i want to be able to edit my contact information
- As a user i want to add an item to the shopping cart
- As a user i want to be able to update the amount of products in my cart
- As a user i want to be able to delete an item from my cart
- As a user i want to be able to sign up for a newsletter
- As a user i want to be able to see privacy information
- As a user i want to be able to log in/log out easily
- As a user i want to be able to se product information 

### EPIC | Purchase
- As a user i want to view my shopping cart to see the total cost
- As a user i want to easily edit my cart to buy more/less
- As a user i want to see a summary of my products added
- As a user i want to be able to easily enter my payment information to complete a purchase
- As a user i want to easily make an order without having to sign up
- As a user i want to view a confirmation of my order and recieve an email confirmation


[Back to top ⇧](#coffee-shop)
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


[Back to top ⇧](#coffee-shop)
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
    16. Inside the Procfile you need to add following: web: guincorn coffee_shop.wsgi.
    17. After adding these files, commit and push these changes to GitHub.
    18. In Heroku, go to the deployment tab and deploy this branch manually. This will lead to Heroku building this app for you, and you will be able to follow the build process in the window. 
    19. When successful, you will be displayed with following: "Your app was successfully deployed".

[Back to top ⇧](#coffee-shop)

------

## Credits 

### Code
- Inspiration from both the Walkthru project, former student Delboy and Kera.
- [GringoCoffee](https://www.gringonordic.se/) for images, inspiration with information and the coffee that kept me coding! 

### Media
- As mentioned above most images are from the [Gringo](https://www.gringonordic.se/) website. 
Others from pixabay

### Other
- The [Djangodocs](https://docs.djangoproject.com/en/4.0/) was a big help for troubleshooting
- [Stackoverflow](https://stackoverflow.com) for trying to find bugs, sollutions and inspiration.
- Creating a sitemap file [here](https://www.xml-sitemaps.com/)

------

## Acknowledgements 

- The big support network on slack, alumnis and current students for always beeing there and helping, troubleshooting or rubber-ducking. No one mentioned and no-one therefor forgotten!
- Tutor support for putting up with my brain-fog silly questions


[Back to top ⇧](#coffee-shop)