# Coffee Shop

Coffee Shop is an e-commerce website operating in the field for all coffee lovers. 

This fully responsive website was built using the Django framework in Python.

Find my live deployed site [here](https://coffeeshop91.herokuapp.com)

The payment system used is a service called Stripe. To test the payments on this site, dummy card details can be used. A list of these can be found [here](https://stripe.com/docs/testing#cards)

![Responsive](assets/mockup.png)

## Content 

[User experiences (UX)]()
* [user stories]

[Design](#design)

* color and inspiration

[Features](#features)

[Technologies](#technologies) 
*[Languages used](#languages-used)
[Libraries & programs used](#libraries-and-programs-used)


[Testing](#testing)


[Deployment](#deployment)
* [Github](#github)

[Credits](#credits)
* [Code](#code)
* [Media](#media)
* [Other](#other)

--------

## User experience (UX)

The visitors to Coffee Shop is most likely someone who enjoys making nice coffee at home. Who enjoys a nice espresso, or a pour over coffee from whole beans. A visitor to Coffee shop is also someone who most likely enjoys reading about coffee, and the different type of brews there are. 

### User stories 

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

The look for this project is partly inspired by Code Institutes "Boutique Ado" with some finishing touches and styles that i've seen doing research for this project.
I've contacted Gringo Coffee shop who is a roastery here in Sweden and i've gotten their permission to use images and copy their descriptions. You can find their website [here](https://www.gringonordic.se/)

### Color scheme 

I've decided to stick to a basic color scheme of black/white/grey with this project to really highlight the bags of beans, as i find them to have a really nice design - and i wanted them to really pop. 

### Images

- I've gotten my images from Gringo, which is also where i have gotten the inspiration for this website, and the information about their magical beans. 

### Wireframe

I took a lot of inspiration for this project from Code Institutes Boutique Ado, and also from Gringo's website as described above.
I did a start design on Figma to try and set up the main page and view for the products. 

* First mockup looked like this:

![Mockup](static/images/figmamockup.png)

* And for the product page like this: 

![Mockup](static/images/figmamockupproduct.png)

[Back to top ⇧](#coffee-shop)

-------

## Features 

### Home page 

 - ### Navigation bar 
    - The navbar is always visible from the top of the page, and will house links for products, about us, contact form and back to home page. There will also always be access to your account, the shoppingbag and to search the shop.
    - The option to view your account will only be visible when a user is logged in.
    - The option to add products and coupons is only visible to admin users.
    - The shopping bag is always accessible from the navbar, to always be able to check what you've added to your bag, to easily be able to remove and edit the items in your bag. 

------- 


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

### Business Model 

This project will have the business model of B2C (Business to Customer) as the business is selling products directly from their shop to the end user.

### Marketing 

This site represents a fairly new business, where the only current marketing stragety is a facebook page, and signing up for a newsletter.

- Links to social media sites can be found inside the footer

- The facebook link takes you to the Coffee Shop business page which can be found [here](https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2FCoffee-Shop-100440999619238%2Finsights%2F%3Freferrer%3Dpage_admin_insights_card)*.
<br>
<i>*Note, this page has unfortunately been deleted, due to facebooks regular deletion of inactive business pages.</i>

![Facebook](media/coffeeshopfacebook.png)

- The newsletter sign up form is to be found in the footer of the site. This is serviced by [Mailchimp](https://mailchimp.com/?currency=SEK)

![Newsletter]()

### Search Engine Optimisation

I've created both a robots.txt and sitemap.cml file to help search engines located to the site. To keep my users information safe, any pages that would include sensitive information has been disallowed in my robots.txt file.

My purpose of the "About us" pages was designed to give an opportinity to use some keywords to the user and help boost the site's ranking in search engine results. 

My inital keywords and phrases i came up with are:

#### Short tail keywords
- Espresso
- Coffeebeans
- Grounds
- Coffee pot
- Shot
- Bean
- Filter coffee
- Cappucino
- Flat white

#### Long tail keywords
- Milk drinks with coffee
- Espresso beans for home usage
- Make your own espresso
- Barista coffee at home
- espresso and pre-ground beans for home use

[Back to top⇧](#coffee-shop)

## Features

### Navbar

- #### Links
    - To help the user to navigate the website there's four links at the main nav bar at the top of every page.
    - Once the screen size becomes to small to fit all four links it turns into a hamburger bar to fit all the elements comfortably.
    - The link to the current page will be highlighted by an underline to help users understand what page they are on.
    - The Shop link and the about us drops down into a sub-menu where the user can navigate to all products or choose one of the two categories. In the about us section the user can choose to read the different articles, the main about us page, the coffee farm page or the flavour guide. 

    ![Navbar]( image here of the navbar )

- #### Search bar
    - The search bar is located in the middle of the navigation bar, and can be used to search for items on the site.
    - Using the search bar will search both the product's title and description for a match.
    - On smaller screens the bar collapses into a icon for searching that when clicking drops down into the full search bar.

    ![Nav-bar search ]( image here of the navbar search )

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

Testing and results can be found [here](TESTING.md)

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