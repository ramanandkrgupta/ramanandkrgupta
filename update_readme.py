import json

# Load the current README template
with open("README_TEMPLATE.md", "r") as file:
    readme = file.read()

# Replace weather data
with open("weather.json", "r") as file:
    weather = json.load(file)
    weather_info = f"{weather['main']['temp']}°C, {weather['weather'][0]['description']}"
    readme = readme.replace("{weather}", weather_info)

# Replace GitHub stats
with open("github-stats.json", "r") as file:
    stats = json.load(file)
    contributions = stats['data']['viewer']['contributionsCollection']['contributionCalendar']['totalContributions']
    readme = readme.replace("{contributions}", str(contributions))

# Write back the updated README
with open("README.md", "w") as file:
    file.write(readme)
