@echo off
call yoloenv\Scripts\activate

pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu118

pip install opencv_contrib_python-4.10.0.84-cp37-abi3-win_amd64.whl

echo command was succesfully.
pause