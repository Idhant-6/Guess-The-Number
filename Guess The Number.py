from art import logo
from random import randint
import pyttsx3
from requests.api import put
import speech_recognition as sr 
import wikipedia 
import sys
import webbrowser   
import os
import smtplib
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageGrab
import requests
from bs4 import BeautifulSoup
import psutil
import cv2
import speedtest
import pyautogui
import datetime
import pandas
import lib

# Necessary Lines to make Machine Speak! DO NOT CHANGE UNTIL NECESSARY!
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """Is Used to Make Machine Speak Anything You Want..."""
    engine.say(audio)
    engine.runAndWait()

def prispk(value):
    """Used to Both Speak And Print Commands at the Same Time."""
    print(value)
    speak(value)

answer = randint(1, 100)
chances_left = 0
quit_game = False
print(logo)
prispk(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
	chances_left += 10
elif difficulty_level == "hard":
	chances_left += 5
else:
	print("Invalid Input You Lost!")

while chances_left > 0:
	user_guess = int(input("Make a guess: "))
	if user_guess > answer:
		print("Too high.")
		chances_left -= 1
		if not user_guess == answer:
			print("Guess again.")
			print(f"You Have {chances_left} Chances Left")
	elif user_guess < answer:
		print("Too low.")
		if not user_guess == answer:
			print("Guess again.")
			print(f"You Have {chances_left} Chances Left")
		chances_left -= 1
	elif user_guess == answer:
		print(f"You got it! The answer was {answer}")
		chances_left = 0
	if chances_left <= 0:
		print(f"You've run out of guesses, you lose. By The Way, The Answer was {answer}")

