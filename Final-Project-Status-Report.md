# Master Status Report


## Project Overview

**Team:** Autumn, Adam, Britt, Steve

**Scribe** Amelia


## Sprint Goals
**Sprint 1: Setup and Core Features**
>Goal: Establish basic infrastructure and develop core features of the rewards program
>
***Tasks***
* Set up project repository and development environment
* Create UML Class Diagram




**Sprint 2: Points Accumulation System and Reward Redemption Functionality**
>Goal 1: Implement points accumulation system based on customer spending
>
***Tasks***
* Design and develop points calculation logic based on agreed spending amount
* Ensure functionality of auto update of points balance after each purpose
* Design and implement user registration form with email and password authentication
* Create user interface in which user can view profile page that displays current point balance and transaction history

>Goal 2: Develop reward redemption features
>
***Tasks***
* Design rewards catalog with different redemption options
* Integrate points redemption process and enable ability to redeem points for rewards
* Develop feedback for successful or failed redemption attempts



**Sprint 3: Admin Interface for Accounts and Points Management**
>Goal: Create interface for adjusting points and managing user accounts
>
***Tasks***
* Design an admin dashboard with functions to view and manage accounts
* Develop features to add, subtract, and adjust points for user accounts
* Develop reporting tools to monitor reward program performance and user activity



**Sprint 4: Testing and Bug Fixes**
>Goal: Conduct extensive testing and fix any identified bugs
>
***Tasks***
* Perform meticulous testing of all app features to identify and resolve any issues or bugs.
* Ensure compatability for different web browsers
* Address and revise any app performance issues to enhance speed and efficiency



**Sprint 5: Final Review**
>Goal: Complete final reviews and deployment tasks to ensure app is ready for launch 
>
***Tasks***
* Comprehensive review of all features and functionality
* Create deployment documentation
* Move app from development to production environment
* Verify that app works correctly in production environment and all systems function as expected. Resolve any deployment issues.

# Team Meetings

**Upcoming Meeting: TBD**


# Progress Summary

## ***Complete Tasks***
* Autumn created Discord for team communication
* Adam created Github Repository and sent invite to all team members
* Steve created and completed Class UML
* Amelia created ad formatted a status report and will continue to add updates throughout the project
* Sprint 1: Setup and Core Features Tasks Completed
* Sprint 2: Points Accumulation System and Reward Redemption Functionality
* Sprint 3: Admin Interface for Accounts and Points Management

## ***In-Progress Tasks***

*September 10, 2024*
* Autumn started developing the class tkinter codes for the program

*September 15, 2024*
* Britt began drafting rewards system in which she created the opening screen of the app, which includes interactive buttons that highlights as yellow when clicked and takes user to a new window. Interactive buttons will open windows that will do the following:
  *  New Member: Begin the process of obtaining customer info, point balance, and redeeming points.
  *  Existing Member: Login authentication which then will show user profile, point balance, and transaction history
  *  Exit: Close out the program

* Britt began developing code for the new member registration window, which asks for user first and last name
* Britt began developing code for Existing Member Login window, which shows reward balance, past purchases, item to purchase and the points earned if purchased, and rewards that can be redeemed along with how many points needed to redeem them. She also coded feedback messages for successful and failed reward redemptions.

![Rewards System Windows](https://media.discordapp.net/attachments/1280868273541615639/1284922854781223012/Screenshot_2024-09-15_125913.png?ex=66f399e9&is=66f24869&hm=74ba1e6b09f8a93b4891d5d1980ccfc34bdae0ab180c3c3e33b75af6a35f8a5c&=&format=webp&quality=lossless&width=1243&height=686)
![Rewards System Windows 2](https://media.discordapp.net/attachments/1280868273541615639/1284922855087276154/Screenshot_2024-09-15_125955.png?ex=66e86529&is=66e713a9&hm=3452e7309ae80831bb55b909dc85e34a45b62e9cff3b701554b55e2667d23b66&=&format=webp&quality=lossless&width=1012&height=918)

![Rewards System Windows 3]![image](https://github.com/user-attachments/assets/f7ac2ada-3237-4dd2-a297-74e3a87d0cbf)

![Rewards System Windows 4]![image](https://github.com/user-attachments/assets/87dd912c-78a2-4e97-bbf4-f0f3b0ad64a2)

![Rewards System Windows 5]![image](https://github.com/user-attachments/assets/a3adecd6-562c-4765-bc6c-263c23481509)


*September 24, 2024*
* Amelia added Sprint Tasks on Kaban board for others to edit and adjust
* Autumn got permission from owner to use Blue Moose Coffee Lounge logo for our project


*September 25, 2024*
* Steve updated the menu screen design and made it so that the forms will open in the center of the menu screen. He also made it so the menu screen buttons are disabled until the pop up window is closed. 
![Rewards System Windows](https://cdn.discordapp.com/attachments/1280868273541615639/1288682674797543465/image.png?ex=66f6bb84&is=66f56a04&hm=ecc99d86621abf27df4d14416816b2547d9f4be1ccd8b90fc5968c61b4c4e721&)


*September 27, 2024*
* Adam fixed the file pathing and windows for the redemption points. He also edited the other windows backgrounds so that they would match the background Steve put on the main screen.


*September 28, 2024*
* Amelia began converting the Python Tkinter code to Django and then editing and designing the main window


*October 1, 2024*
* Amelia finished designing and editing the main page of the webapp


*October 3, 2024*
* Amelia coded all pages(login page, customer profile page, registration page, and thank you for registering page) of webapp to have the same background and style as the main page
* Amelia fixed login redirect errors so that it will successfully redirect the user to their profile
* Amelia created a logout feature
* Amelia added redirect features on login and registration pages, so that if user does not have a profile, they can be redirected to registeration page or vice versa
* Amelia created an admin user profile to manage customer data

* October 4, 2024*
* Amelia extended member_data function to include logic for redeemable and purchasable items, as well as the ability to redeem or purchase items.

* October 7, 2024*
* Steve fixed issues with purchase and redeem
