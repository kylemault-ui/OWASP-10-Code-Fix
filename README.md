# OWASP-10-Code-Fix
Okay for this assignment I put all the fixed codes in 1 .py file so all 10 are together but you can take each one and use them where every you need to they have everything that is need to run separate I just did not want to make like 10 different files also in this read me has all of what is wrong and how to fix and why does this help. This is the main source is used for this 2 https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html but I also used this two just not as much https://zetcode.com/terms-testing/owasp-testing/ and https://owasp.org/projects/web-security-testing-guide

1. Broken Access Control

What is wrong? The original code lets a user access a profile by using a user ID. It does not check if they are allowed to see that profile. This could let someone see another user's information. How did I fix it? I added a check that compares the logged-in user's ID with the profile ID. Why does this help? The user can only access the profile if the IDs match. This helps stop users from accessing other people's information.

2. Broken Access Control

What is wrong? This code has the same type of problem. It gets an account without checking if the user is allowed to access it. Someone could change the account ID and try to see another account. How did I fix it? I added a check to make sure the current user owns the account. Why does this help? If the IDs do not match, access is denied. This helps protect other users' account information.

3. Cryptographic Failures

What is wrong? The original code uses MD5 for passwords. MD5 is old and is not safe for storing passwords. How did I fix it? I changed the code to use bcrypt. Why does this help? Bcrypt is made for password storage and is much safer than MD5.

4. Cryptographic Failures

What is wrong? The original code uses SHA-1 for a password. SHA-1 is old and should not be used for password storage. How did I fix it? I changed it to use bcrypt. Why does this help? Bcrypt is made for passwords and makes them harder to crack.

5. Injection

What is wrong? The original code puts the username directly into a SQL query. An attacker could enter SQL commands instead of a normal username. How did I fix it? I used a parameter in the SQL query instead of putting the username directly into it. Why does this help? The database treats the username as data instead of a SQL command. This helps stop SQL injection.

6. Injection

What is wrong? The original code trusts the username given by the user. An attacker could send unexpected information to try to change how the database search works. How did I fix it? I checked that the username is a string and that it is not too long. Why does this help? This makes sure the program gets the type of information it expects.

7. Insecure Design

What is wrong? The original password reset code only uses an email and a new password. Someone could try to reset another person's password without proving they own the account. How did I fix it? I added a reset token that must be correct before the password can be changed. Why does this help? The reset token gives the program another way to check that the password reset is allowed.

8. Software and Data Integrity Failures
  
What is wrong? The original code loads a JavaScript file without checking if it has been changed. If the file was changed, the website could run the changed code. How did I fix it?
I added a file hash check. Why does this help? The hash can be used to check if the file is still the same. If the hash does not match, the file was changed.

9. Server-Side Request Forgery What is wrong?
  
The original code lets the user enter any URL and makes the server connect to it. This could let someone make the server connect to places it should not. How did I fix it? I check that the URL uses HTTP or HTTPS and added a timeout. Why does this help? This adds a check before the request is made and stops the request from taking too long. A real application should also use a list of trusted websites and block internal addresses.

10. Identification and Authentication Failures

What is wrong? The original code compares the entered password to the stored password. If passwords are stored normally, someone who gets the database could see the passwords. How did I fix it? I used bcrypt to store the password as a hash and then check the entered password against the hash. Why does this help? The real password does not need to be stored. This helps protect passwords if the database gets stolen.
