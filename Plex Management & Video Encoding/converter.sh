#!/bin/bash

for file in *.mkv; do
    output="${file%.mkv}_x265.mkv"	#add -vf realtime to limit speed
    ffmpeg -hwaccel cuda -y -i "$file" -c:v libx265 -preset medium -crf 24 -c:a copy -c:s copy "$output" && rm "$file"
done
