#currency.py
#作者：化学与分子工程学院18级 崔若瑶
#学号：1800011755
#网络号：162.105.129.65
#邮箱：1800011755@pku.edu.cn


"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

from urllib.request import urlopen
import sys
import re

def before_space(s):
	"""break up a JSON string and seperate the currency amount from the currency name
	Returns: Substring of s before the first space

	Parameter s: the string to slice
	Precondition: s has at least one space in it"""
	aa=s.lstrip()
	qq=aa.find(" ")
	ww=aa[:qq]
	return ww

def after_space(d):
	"""Returns: Substring of s after the first space
	   Parameter d: the string to slice
	   Precondition: s has at least one space in it"""
	ee=d.lstrip()
	rr=ee.find(" ")
	tt=ee[rr:]
	yy=tt.rstrip()
	return yy.lstrip()


def get_from(JSON):
	"""Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	Returns: The FROM value in the response to a currency query."""
	dd=JSON.split(":")
	ff=dd[1]
	gg=ff.find(",")
	ggg=ff[2:gg-1]
	return ggg

def get_to(JSON1):
	"""Given a JSON response to a currency query, this returns the string inside double quotes (") immediately following the keyword "to".
	Returns: The TO value in the response to a currency query.
	Parameter JSON1: a json string to parse
	Precondition: JSON1 is the response to a currency query"""
	hh=JSON1.split(":")
	jj=hh[2]
	kk=jj.find(",")
	ll=jj[2:kk-1]
	return ll

def has_error(JSON2):
	"""Given a JSON response to a currency query, this returns the opposite of the value following the keyword "success". 
	Returns: True if the query has an error; False otherwise.
	Parameter JSON2: a json string to parse
	Precondition: JSON2 is the response to a currency query"""
	if JSON2.find("false")!= -1:
		return True
	else:
		return False

def currency_response(currency_from, currency_to, amount_from):
	"""Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "success" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
	parameter="from="+currency_from+"&to="+currency_to+"&amt="+amount_from
	url="http://cs1110.cs.cornell.edu/2016fa/a1server.php?"+parameter
	doc = urlopen(url)
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii')
	return jstr

def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    xx=currency_response(currency,"USD","1")
    return not(has_error(xx))

def isNum1(value):
"""judge if the value can convert to type float or type int"""
    try:
        x = float(value) #此处更改想判断的类型
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception as e:
        return False
    else:
        return True
    

def exchange(currency_from1, currency_to1, amount_from1):
	"""Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
	cc=currency_response(currency_from1,currency_to1,amount_from1)
	if iscurrency(currency_from1) is False:
		return "Source currency code is invalid."
	if iscurrency(currency_to1) is False:
		return "Exchange currency code is invalid."
	if isNum1(amount_from1)  is False:
		return "Currency amount is invalid."
	if iscurrency(currency_from1) and iscurrency(currency_to1) and isNum1(amount_from1):
		vv=get_to(cc)
		njnj=float(before_space(vv))
		return njnj


def test_before_space():
	"""test the function before_space"""
	assert(before_space("0.8963 Euros")=="0.8963")
	assert(before_space("0.384987 Omani Rials")=="0.384987")
	assert((before_space("0.8963Euros")=="0.8963") is False)
	assert(before_space("  0.001743287645 Bitcoins")=="0.001743287645")

def test_after_space():
	"""test the function after_space"""
	assert(after_space("0.8963 Euros")=="Euros")
	assert(after_space("0.384987 Omani Rials")=="Omani Rials")
	assert((after_space("0.8963Euros")=="Euros") is False)
	assert(after_space("  0.001743287645 Bitcoins")=="Bitcoins")

def testA():
	"""test part A"""
	test_after_space()
	test_before_space()

def test_get_from():
	"""test function get_from"""
	assert(get_from('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')=='2.5 United States Dollars')
	assert(get_from('{"from" : "","to":"","success":false,"error":"Source currency code is invalid."}')=='')

def test_get_to():
	"""test fuction get_to"""
	assert(get_to('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')=="2.1589225 Euros")
	assert(get_to('{"from":"","to":"","success":false,"error":"Source currency code is invalid."}')=='')

def test_has_error():
	"""test function get_from"""
	assert(has_error('{"from":"","to":"","success":false,"error":"Source currency code is invalid."}') is True)
	assert(has_error('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }') is False)

def testB():
	"""test part B"""
	test_get_from()
	test_get_to()
	test_has_error()


def test_currency_response():
	"""test function currency_response"""
	assert(currency_response("USD","EUR","2.5")=='{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')
	assert(currency_response("k","huhu","0.35")=='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
	assert(currency_response("AOA","LRD","6.6")=='{ "from" : "6.6 Angolan Kwanzas", "to" : "3.6514236470128 Liberian Dollars", "success" : true, "error" : "" }')
	assert(currency_response("AQA","MNT","3.5")=='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')

def test_isNum1():
	assert(isNum1("9") is True)
	assert(isNum1("0.98") is True)
	assert(isNum1("llp") is False)

def test_iscurrency():
	"""test function iscurrency"""
	assert(iscurrency("AOA") is True)
	assert(iscurrency("bili") is False)
	assert(iscurrency("AQA") is False)
	assert(iscurrency("EUR") is True)
    
def testC():
	test_iscurrency()
	test_isNum1()

def test_exchange():
	"""test function exchange"""
	assert(exchange("USD","EUR","2.5")==2.1589225)
	assert(exchange("k","huhu","0.35")=="Source currency code is invalid.")
	assert(exchange("AOA","LRD","6.6")==3.6514236470128)
	assert(exchange("AQA","MNT","3.5")=="Source currency code is invalid.")
	assert(exchange("AOA","MNT","kk")=="Currency amount is invalid.")
	assert(exchange("AOA","MN","3.5")=="Exchange currency code is invalid.")

def testD():
	test_currency_response()
	test_exchange()


def testall():
	"""Unit test for module exchange

	When run as a script, this module invokes several procedures that 
	test the various functions in the module a1."""
	testA()
	testB()
	testC()
	testD()
	print("All tests passed")

def main():
	"""get the codes and mone,test all the functions,
	and then print corresponding value and test result."""
	aa=input("please input the code of the currency you want to change:")
	bb=input("please input the code of the currency you want to change into:")
	cc=input("please input how much currency you want to change:")
	ss=exchange(aa,bb,cc)
	print(ss)
	testall()
if __name__ == '__main__':
    main()







