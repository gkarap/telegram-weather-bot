#  Daily Telegram Weather Assistant

Welcome! This is a simple, automated Python bot that checks the weather forecast for your city and sends a beautiful, customized morning report directly to your Telegram app every day. 

You don't need to be a programmer to use this! Follow this simple, step-by-step guide to set it up for yourself in about 10 minutes.

---

## What You Need Before Starting
To make this work, you need 3 free "Keys" (think of them as passwords) and your city's location.

## 1. Get your Telegram Bot Token
1. Download the Telegram app and search for "BotFather".
2. Send the message "/newbot" and follow the instructions to give your bot a name.
3. BotFather will give you a long text called a **Token** (e.g., `123456789:ABCdefGhI...`). Save this!

## 2. Get your Telegram Chat ID
1. Still in Telegram, search for **RawDataBot** (or similar ID bots) and press Start.
2. It will reply with a lot of text. Look for the `"chat"` section and find your `"id"` (e.g,`1234567890`). Save this number!

## 3. Get your OpenWeather API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/) and create a free account.
2. Click on your profile name  -> "My API keys".
3. Generate a new key and copy the long sequence of letters and numbers. Save this!

## 4. Find Your City's Coordinates (Latitude & Longitude)
The bot needs to know exactly where you live.
1. Open Google Maps on your computer.
2. Find your city or neighborhood.
3. "Right Click" exactly on the map where you want the weather for.
4. The very first thing in the menu is a pair of numbers (e.g., `12.3456, -23.4567`). Click on them to copy them! The first number is your **Latitude (lat)** and the second is your **Longitude (lon)**.

---

# How to Set It Up on Your GitHub

## Step 1: Copy this Project 
1. At the top right of this page, click the "Fork" button. This creates a copy of this entire project into your own GitHub account so you can edit it safely.

## Step 2: The "Secrets" (Keep your passwords safe)
We NEVER! put our passwords directly into the code where everyone can see them. Instead, GitHub has a safe vault called "Secrets".
1. In your new repository, click on **Settings** (the gear icon at the top).
2. On the left menu, scroll down and click **Secrets and variables**, then select **Actions**.
3. Click the green button **New repository secret**.
4. You need to add 4 secrets exactly like this:
   * Name: OWM_API_KEY | Secret: "(paste your OpenWeather key here)"
   * Name: TELEGRAM_BOT_TOKEN | Secret: "(paste your BotFather token here)"
   * Name: TELEGRAM_CHAT_ID | Secret: "(paste your Chat ID number here)"
   * Name: USER_NAME | Secret: "(type your first name, e.g., George)"

## Step 3: Add Your Coordinates to the Code
1. Go back to the main page of your repository and click on the `main.py` file.
2. Click the Pencil icon (Edit) at the top right.
3. Look for the API parameters section in the code (around line 29-30):
   
   "lat": "37.983810", 
   "lon": "23.727539", 

4. Replace those numbers with the ones you got from Google Maps.
5. Click the green **Commit changes** button at the top right.

## Step 4: Set Your Daily Delivery Time (main.yml)
GitHub servers run on **UTC time** (Coordinated Universal Time). To get the message at the right time in your local timezone, you need to adjust the schedule.
1. From your repository's main page, open the `.github` folder, then `workflows`, and click on the `main.yml` file.
2. Click the **Pencil icon** to edit.
3. Look for the `schedule` section with the `cron` parameter. It will look like this:
   
   - cron: '0 5 * * *' 

4. **Calculate your local time:**
   * Find your timezone's offset from UTC. 
   * *Example 1 (Europe/Greece):* Greece is UTC+3 in the summer. If you want the message at 08:00 AM local time, subtract 3 hours (8 - 3 = 5). So you leave it as `0 5 * * *`.
   * *Example 2 (USA/New York):* New York is UTC-4. If you want the message at 07:00 AM local time, you add 4 hours (7 + 4 = 11). So you change it to `0 11 * * *`.
5. Replace the cron schedule with your calculated number, and click the green **Commit changes** button at the top right.

## Step 5: Turn on the Bot!
1. Click on the **Actions** tab at the top of your repository.
2. Click on the workflow name (e.g., "Daily Weather Assistant") on the left.
3. Click the **Run workflow** button on the right side.
4. Check your Telegram! You should receive your very first weather report! 

---

#  How it works under the hood
Once set up, GitHub Actions will automatically run this script every day at your specified time. It securely loads your API credentials, fetches a 12-hour forecast, calculates the minimum/maximum temperatures, checks for rain or high winds, and delivers a beautifully formatted dashboard to your phone.

---

### Author
Created by George Κ.
