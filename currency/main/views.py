from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from selenium import webdriver
import time
import requests

# Create your views here.
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



def main (request):
    amount = request.GET.get('amount')
    if amount:
        options = Options()
        options.headless = True

        browser = webdriver.Firefox(options=options)
        url = "https://bigpara.hurriyet.com.tr/altin/altin-ons-fiyati/"
        browser.get(url)
        ons = browser.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div[2]/div[2]/span[2]")
        ons = ons.text
        ons = ons.replace(".","")
        ons = ons.replace(",", ".")
        browser.close()
        options = Options()
        options.headless = True

        browser2 = webdriver.Firefox(options=options)
        url2 = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        browser2.get(url2)

        dollar = browser2.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div[2]/div[2]/span[2]")
        dollar = dollar.text
        dollar = dollar.replace(",", ".")

        browser2.close()

        liras = (float(ons)/31.10)*float(dollar)*float(amount)
        return render(request,'main.html',{'liras':liras,'amount':amount})
    return render(request,'main.html')