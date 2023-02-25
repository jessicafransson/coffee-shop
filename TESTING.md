# Coffee Shop - testing

[Visit the live website here](https://coffeeshop91.herokuapp.com/)

---

## Content

[Validators](#validation-testing)
* [HTML](#html)
* [CSS](#css)
* [JavaScript](#jshint)
* [Python](#python)
* [Lighthouse](#lighthouse)

[User Story Testing](user-story-testing)
* [Testing User Stories](#testing-user-stories)
* [Full Testing](#full-testing)

* [Bugs](#bugs)
* [Solved Bugs](#solved-bugs)
* [Known Bugs](#known-bugs)

[Back to top ⇧](#coffee-shop---testing)

Testing has been ongoing throughout building this site, making sure the mobile view is working as it should, and that styles do as expected. 

I've used Chromes devtools to troubleshoot errors and made sure it's responsive on different sizes and devices. 

---

## Validation Testing 

### HTML

- All pages has been tested with the official [W3C Validator](https://validator.w3.org/).

#### Home Page Validation
![home-w3](assets/testing/validation/html/html_mainpage.png)
#### About us Validation
![about-w3](assets/testing/validation/html/html_about.png)
#### Product Page Validation
![products-w3](assets/testing/validation/html/html_products.png)
#### Product Detail Page Validation
![productdetail-w3](assets/testing/validation/html/html_productdetail.png)
#### Add Product Page Validation
![addproducts-w3](assets/testing/validation/html/html_addproduct.png)
#### Edit Product Page Validation
![editproducts-w3](assets/testing/validation/html/html_editproduct.png)
- The add and edit product page shows two errors. These are because the image upload widget and changing this code breaks the field.
#### Coffee Farm Page Validation
![farm-w3](assets/testing/validation/html/html_coffeefarm.png)
#### Flavour Guide Page Validation
![flavour-w3](assets/testing/validation/html/html_flavour.png)
#### Profile Page Validation
![profile-w3](assets/testing/validation/html/html_profile.png)
#### Coupon Page Validation
![coupon-w3](assets/testing/validation/html/html_coupon.png)
#### Coupon error Page Validation
![couponerror-w3](assets/testing/validation/html/html_couponerror.png)
#### Edit Coupon error Page Validation
![couponerror-w3](assets/testing/validation/html/html_editcoupon.png)
#### Coupon error Page Validation
![editcouponerror-w3](assets/testing/validation/html/html_editcouponerror.png)
- The add and edit coupon page shows eight errors. These are because of the datetimepicker widget so it cannot be changed.

[Back to top ⇧](#coffee-shop---testing)

### CSS

- All CSS was checked with official [Jigsaw validator](https://jigsaw.w3.org/css-validator/).

#### Base CSS
![base-css-jigsaw](assets/testing/validation/css/cssvalidator.png)
#### Bag CSS
![bag-css-jigsaw](assets/testing/validation/css/cssbag.png)
#### Profile CSS
![profile-css-jigsaw](assets/testing/validation/css/cssprofile.png)

[Back to top ⇧](#coffee-shop---testing)

### JSHINT

- All JavaScript was passed thru [Jshint](https://jshint.com/).

### Base
![jshint-base](assets/testing/validation/javascript/base.png)
### Products
![jshint-products](assets/testing/validation/javascript/productsjs.png)
### Profile
![jshint-profile](assets/testing/validation/javascript/profilejs.png)
### Bag
![jshint-bag](assets/testing/validation/javascript/bagjs.png)
### Edit Review
![jshint-edit-review](assets/testing/validation/javascript/editreviewjs.png)
### Checkout
![jshint-checkout](assets/testing/validation/javascript/checkoutjs.png)

[Back to top ⇧](#coffee-shop---testing)

### PEP8

- PEP8 only shows things that can be ignored

![pylint]()

### Lighthouse

- Lighthouse score shows..

[Back to top ⇧](#coffee-shop---testing)

## User Story Testing

### EPIC | Navigation
*As a user I can easily navigate the website to see what to purchase*
- The navigation bar is located at the top of every page. Users can access all pages from here.

![Navbar](assets/testing/validation/epic/navbar.png)

- On smaller screens the navbar is located in a hamburger menu that displays when clicked.

![Navbar-mobile](assets/testing/validation/epic/navbarmobile.png)

*As a user i can easily see a list of items to purchase*

![Products](assets/testing/validation/epic/categories.png)

*As a user i can easily see a list of items to purchase*

![Navbar-full](assets/testing/validation/epic/allproducts.png)

*As a user i can click an item to read more about it*

![Product detail](assets/testing/validation/epic/productdetail.png)


### EPIC | Accounts

*As a user i can easily create account to use all the features*
- Users can click the 'Sign in' account icon located in the header, and there choose to sign up. 
- Once on the registration page, the user fills out the form to create an account.

![Sign-up-form](assets/testing/validation/epic/signupform.png)

*As a user i can confirm my email address to create my account*
- When filling out the form, an email will be sent with a link the user can click to confirm the email address.

![Email-confirmation](assets/testing/validation/epic/emailconfirmation.png)

*As a user i can access my account*
- When the link has been clicked and the account is active the user can log in and log out easily from the buttons in the navbar.

![Email-confirmed](assets/testing/validation/epic/emailconfirmed.png)

*As a user i can log in to my account*

![log-in](assets/testing/validation/epic/signinmenu.png)

![log-in](assets/testing/validation/epic/signinform.png)

![log-in](assets/testing/validation/epic/loginsuccess.png)

*As a user i can access my profile*
- As a user i can access and edit my profile information.
- As a user i can see my previous purchases in my account.
- If no purchases has been made there's a link taking you to the products.

![log-in-menu](assets/testing/validation/epic/userprofileview.png)


[Back to top ⇧](#coffee-shop---testing)

### EPIC | Admin
*As an admin, i can access my account from the page*
- Admin users can navigate to the "Product management" under the accounts menu.
- Admin users can also navigate to the "Coupon management" under the accounts menu.

![Admin-menu](assets/testing/validation/epic/adminmenu.png)

- On this page, the admin user can add a new product by filling out this form:

![Add-product](assets/testing/validation/epic/adminaddproduct.png)

*As an admin i can update the information about my products to keep them up to date*

![product-edit](assets/testing/validation/epic/adminupdateproduct.png)

*As an admin i can delete products from the product view*

![Admin-delete](assets/testing/validation/epic/admindelete.png)

*As an admin i can add coupons to give a discount to my customers*

- All the admin have to do is fill out this form to activate a discount.

![Admin-add-coupon](assets/testing/validation/epic/adminaddcoupon.png)

- When added successfully this pop-up will be displayed that the coupon was added successfully!

![Admin-add-coupon](assets/testing/validation/epic/admincouponsuccess.png)

- The admin user can also check what coupons are active and valid at the moment, and choose to edit and delete them.

![Admin-add-coupon](assets/testing/validation/epic/adminactivecoupon.png)

### EPIC | Purchasing

*As a shopper i can add items to my bag*
- The shopper can in any product detail view add items to the bag, and choose the qty of items.


![Add-bag](assets/testing/validation/epic/addbag.png)

*As a shopper i can view my bag to see the items in there, and the amount in my bag.*
- The items will remain in the bag until the shopper is ready to purchase them.
- In this view the shopper can also choose to update the amount and delete an item
- The shopper can also always follow the amount total in the bag, and see the total cost with shipping.
- If the shopper has items for less than $ which is the amount for free shipping, there will be a calculator for how much more to spend for free shipping.
- If the user has a coupon code, this is the place to add it to the total amount.

![view-bag](assets/testing/validation/epic/viewbag.png)

*As a shopper i can easily make a purchase without being logged in*

- Any shopper can add items to the bag, and make a purchase without being logged in.
- The users will be displayed with a form to fill out information, and card details.
- There's a box to tick, if you would like to save your information for the future.

![view-bag](assets/testing/validation/epic/checkout.png)

*As a user i can easily pay for my order*

- When the user has pressed to secure checkout, and filled in the payment information it will display a loading view, informing the user that the payment is ongoing.

![payment-loading](assets/testing/validation/epic/paymentloading.png)

*As a shopper i get a confirmation after made purchase*

- The user will be displayed with a purchase successful page, where all the information will be displayed

![checkout-success](assets/testing/validation/epic/checkoutsuccess.png)

*As a user i get a confirmation email after successful purchase*

- The user will get sent an email confirmation after a successful purchase, with all the information about the items.
- The email also contains a discount code for the next purchase, and contact information to the shop.

![email-confirmation](assets/testing/validation/epic/emailconfirmation.png)

### EPIC | Interaction

*As a user i can leave reviews on products to share tips with others*
- To write a review is located on the right side at the end of the product detail page.
- Once the review has been left it will be visible on the left side, with the amount of stars filled in.
- If a user has already left a review, the box on the left will be gone, with a text that a review has already been written.

![review](assets/testing/validation/epic/addreview.png)

- If the user isn't logged in they see this view, redirecting to log in to leave a review

![leave-review-user-not-loggedin](assets/testing/validation/epic/addreviewloginrequired.png)

- When the review has been successfully left, it will be displayed like this:
- currently there's a bug for the user to edit their review. It is under construction.

![review-confirmation](assets/testing/validation/epic/addedreview.png)

*As a user i can contact the shop owner with questions*

- The contact us form contains a form the user can fill out to leave a message to the company with ideas or complaints.
- If the user doesn't want to send a message there's a button displayed which re-directs the user back to previous page.

![contact-us](assets/testing/validation/epic/contactform.png)

*As a user i can sign up for a newsletter*

- The user can at the footer of every page sign up for a newsletter for the shop.

![newsletter](assets/testing/validation/epic/newsletter.png)

- When the form has been filled out correctly a message pops up saying "thank you for subscribing".

![newsletter-success](assets/testing/validation/epic/newslettersuccess.png)

*As a user i can find information about the shop, and how to contact them*

- The user can find the information about the shop in the footer of each page with address, email and phone number
- There's also a link here directly to the contact form

![contact-info](assets/testing/validation/epic/contactinfo.png)

*As a user i can read more about the shop and founders*

- As a user i can read more information about coffee shop as a company
- As a user i can also go directly to the beans from this page via the shop link
- As a user i can also go directly to contact us via a link on this page.

![about-coffee-shop](assets/testing/validation/epic/aboutus.png)

*As a user i can read more about the farm they own*

- As a user i can read more about the work they do on their farm, and their purpose
- As a user i can also go directly to the beans from this page via the shop link
- As a user i can also go directly to contact us via a link on this page.

![about-coffee-farm](assets/testing/validation/epic/coffeefarm.png)

*As a user i can get more information about different type of beans and flavours*

- As a user i can learn more about different type of beans, and how the roast affects the flavour.
- As a user i can also go directly to the beans from this page via the shop link
- As a user i can also go directly to contact us via a link on this page.

![about-coffee-flavours](assets/testing/validation/epic/flavourguide.png)


[Back to top ⇧](#coffee-shop---testing)

## Feature testing

### Nav Bar

- #### Links

    Checked that:

    - The links change colour when hovered over.
    - The Shop link drops down into a sub-menu displaying all products and the different categories.
    - The links collapse into a hamburger menu once the screen size becomes too small. 

    ![navbar](assets/testing/validation/epic/navbar.png)

- #### Search Bar
    Checked that:
    - The search bar will search both products title and description.
    - On smaller screens, the search bar collapses into a search icon that when clicked dropps into the full search bar

    ![search-bar](assets/testing/validation/epic/searchbar.png)

- #### Account
    Checked that:
    - Hovering over the account icon changes its colour.
    - When clicking the account a dropdown opens up for the user with options to register or log in.
    - When a user is logged in the dropdown options change to 'My Account' and 'Sign out'.
    - When a user is logged in the icons text changes from 'Sign in' to 'My Account'.
    - When a user is signed in as a super user then a third option of 'Product Management' is available.
    - When a user is signed in as a super user then a fourth option of 'Coupon Management' is available.

    ![user-menu](assets/testing/validation/epic/userlogin.png)
    ![admin-menu](assets/testing/validation/epic/adminmenu.png)
    
- #### Bag Icon
    Checked that:
    - Underneath the bag icon there's a total cost of all the items in the bag.
    - After an item has been added a pop-up shows with the qty of items, and total lost, located at the top right corner.


    ![add-to-shopping-bag](assets/testing/validation/epic/addtobag.png)

    - When bag icon is clicked, user get's navigated to the shopping bag where user can see what items are in the bag.

    ![shopping-bag](assets/testing/validation/epic/viewbag.png)

### Home Page 



[Back to top ⇧](#coffee-shop---testing)

[Back to top ⇧](#coffee-shop---testing)