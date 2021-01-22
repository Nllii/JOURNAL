# How to use this script!


1. Find your webdriver online and set it to the path!  
I have added a chromedriver for mac, if you need another driver, google it.

```JS
example: if your driver is at  downloads: get the path and modify the code to the path 
driver = webdriver.Chrome('/Users/admin/newrow_login/chromedriver ')

````
2. edit the script 
    1. open terminal cd to path where the script is
    2. vi, add your username and login to the script 

```JS
full_name = driver.find_element_by_id('txtFullName').send_keys("Mr.Lyon_raawwww")
email = driver.find_element_by_id('txtNewEmail').send_keys("W@student.hccs.edu")

````


3. Next you want to set up a cron task.
 https://en.wikipedia.org/wiki/Cron
https://man7.org/linux/man-pages/man1/crontab.1.html


1. open terminal 
2. crontab -e 
3. Add this : 

 