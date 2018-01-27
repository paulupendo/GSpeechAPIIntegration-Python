#!/bin/bash
echo converting .webm audio to .wav
echo y|ffmpeg -i uploads/rec_data1.wav -acodec pcm_s16le -ac 1 -ar 16000 uploads/rec.wav 

echo converting .wav audio to .flac
sox uploads/rec.wav -c 1 uploads/rec.flac
