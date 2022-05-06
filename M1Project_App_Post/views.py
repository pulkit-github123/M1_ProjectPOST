from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
#import requests

#PROGRAM TO CHECK WHETHER ENTERED NUMBER IS A PRIME OR NOT USING POSTMAN
@api_view(['POST'])
def CheckPrimeNumberPOST(request):
    number = int(request.POST.get('number'))
    list = []
    for x in range(number):
        x = x + 1
        y = number%x
        if y == 0:
            list.append(y)
    if len(list) == 2:
        message = "The number entered is a prime number"
    else:
        message = "The number entered is NOT a prime number"
    return Response(message)


#PROGRAM TO CHECK WHETHER ENTERED NUMBER IS AN ARMSTRONG NUMBER OR NOT USING POSTMAN
@api_view(['POST'])
def CheckArmstrongNumberPOST(request):
    number = int(request.POST.get('number'))
    List = [int(x) for x in str(number)]
    LenOfNumber = len(List)
    ArmstrongSum = 0
    for i in range(LenOfNumber):
        ArmstrongSum = List[i]**LenOfNumber + ArmstrongSum
    if ArmstrongSum == number:
        message = "The number is an Armstrong Number"
    else:
        message = "The number is NOT an Armstrong Number"
    return Response(message)


#BELOW PROGRAM IS TO CHECK WHETHER THE STRING IS AN ANAGRAM OR NOT USING POSTMAN
@api_view(['POST'])
def CheckAnagramPOST(request):
    s1 = request.POST.get('s1')
    s2 = request.POST.get('s2')
    s1 = s1.replace(" ","") #deleting all spaces from a string as anagram consider only rearrangements of letters and not spaces
    s2 = s2.replace(" ","") #deleting all spaces from a string as anagram consider only rearrangements of letters and not spaces
    l1 = [x for x in s1.lower()] #converting all cases into lower before inputting that string into a list
    l2 = [x for x in s2.lower()] #converting all cases into lower before inputting that string into a list
    print (l1,end = "\n")
    print (l2)
    l1.sort() #sort() is the function in python to compare the elements of the list and that does not check the sequence/order of all elements
    l2.sort() #sort() is the function in python to compare the elements of the list and that does not check the sequence/order of all elements
    if l1 == l2:
        message = "Entered strings are Anagrams"
    else:
        message = "Entered strings are NOT Anagrams"
    return Response(message)


# BELOW PROGRAM TO CHECK WHETHER ENTERED STRING IS A PALINDROME OR NOT USING POSTMAN
@api_view(['POST'])
def CheckPalindromePOST(request):
    string = request.POST.get('string')
    string = string.lower()
    string = string.replace(" ","")
    reverse_string = string[::-1] # using the slicing and dicing method -1 in the third argument so that it starts in a reverse way
    if reverse_string == string:
        message = "The entered string is a Palindrome"
    else:
        message = "The entered string is NOT a Palindrome"
    return Response(message)