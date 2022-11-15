@echo off
:x
echo There will be a 5 minute delay between runs because otherwise we will make more requests than allowed on the cmc API free tier!
timeout 300
python cmcAPI.py
goto :x