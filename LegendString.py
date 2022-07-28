import os

os.system("pip install telethon")
os.system("pip install pyrogram")
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("•••   GodFather  SESSION  GENERATOR   •••")
print("\nHello!! Welcome to GodFather Session Generator\n")
okvai = input("Enter 69 to continue: ")
if okvai == "69":
    print("Choose the string session type: \n1. GodFather \n2. Music Bot")
    library = input("\nYour Choice: ")
    if library == "1":
        print("\nTelethon Session For GodFather")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with TelegramClient(StringSession(), APP_ID, API_HASH) as godfather:
            print("\nYour GodFather Session Is sent in your Telegram Saved Messages.")
            godfather.send_message(
                "me", f"#GodFather #GODFATHER_STRING \n\n`{godfather.session.save()}`"
            )
    elif library == "2":
        print("Pyrogram Session for Music Bot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as godfather:
            print("\nYour MusicBot Session Is sent in your Telegram Saved Messages.")
            godfather.send_message(
                "me",
                f"#GODFATHER_MUSIC #MUSICBOT_SESSION\n\n`{godfather.export_session_string()}`",
            )
    else:
        print("Please Enter 1 or 2 only.")
else:
    print("Bhag jaa bhosdike")
