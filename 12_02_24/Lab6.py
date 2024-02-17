from unittest import case

browser = input("Enter the browser name\n")
browser = browser.lower()
match browser:
         case "chrome":
             print("chrome code executed")
         case "firefox":
            print("firefox code")
         case _ :
            print("invalid")

