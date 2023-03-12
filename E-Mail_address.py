#Program to identify the USERNAME & DOMAIN of E-mail Address

E_mail_id = input ( " Enter the E-Mail ID :" )
user_name, domain_name = E_mail_id.split('@')
print( " User name is : ", user_name )
print( " Domain_name is : ", domain_name )