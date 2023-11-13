from flask import Flask, render_template, request, redirect, url_for
import discord
from discord.ext import commands

app = Flask(__name__)

# Initialize your Discord bot
intents = discord.Intents.default()
intents.message_content = True
intents.message_mentions = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Your Discord bot token
TOKEN = "MTE3MzcxOTY3MjE2ODkxMDg1OA.G3FK-z.xSIJB3riGKaDfh6ININIKZsN0ABJ6oaD0qrwoE"

# Dictionary to store embeds
embeds = {}

# Replace CHANNEL_ID with your actual channel ID
CHANNEL_ID = 1167199446472347700

# Route for the main dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html', embeds=embeds)

# Route to create and send embeds
@app.route('/create_embed', methods=['POST'])
def create_embed():
    title = request.form['title']
    description = request.form['description']
    color = int(request.form['color'], 16)  # Convert hex color to integer

    # Create an embed
    embed = discord.Embed(title=title, description=description, color=color)

    # Add the embed to the dictionary
    embeds[title] = embed

    # Send the embed to a specific channel
    channel = bot.get_channel(CHANNEL_ID)
    channel.send(embed=embed)

    return redirect(url_for('dashboard'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)