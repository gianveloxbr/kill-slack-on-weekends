from datetime import datetime
import os

actual_day = datetime.today().strftime('%A')

if actual_day == 'Saturday' or actual_day == 'Sunday':
    os.system('taskkill /f /im slack.exe')
else:
    quit()
