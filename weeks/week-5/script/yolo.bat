@echo off
mkdir yoloproject

mkdir yoloenv

python -m venv yoloenv

call yoloenv\Scripts\activate

pip install ultralytics

echo command was succesfully.
pause