#!/bin/bash
echo Enter the URL to download:
read URL

regex='(https?|ftp|file)://[-[:alnum:]\+&@#/%?=~_|!:,.;]*[-[:alnum:]\+&@#/%=~_|]'
if [[ $URL =~ $regex ]]; then 
    file_name=$(basename "$URL")
    start_time=$(date +%s)
    st=$(date +%c)
    wget_output=$(wget -nv "$URL")
    end_time=$(date +%s)
    et=$(date +%c)
    download_time=$((end_time - start_time))
    file_size=$(du -h "$file_name" | cut -f1)
    if [ $? -eq 0 ]; then
        echo "Download Link: <$URL>" >> Report.txt
        echo "Download successful: $file_name" >> Report.txt
        echo "Start time: $st" >> Report.txt
        echo "End time: $et" >> Report.txt
        echo "Download time: $download_time seconds" >> Report.txt
        echo "File size: $file_size" >> Report.txt
        echo "----------------------------------------" >> Report.txt
        echo "File downloaded successfully!!!"
    else
        echo "Download Link: <$URL>" >> Report.txt
        echo "Download failed: $file_name" >> Report.txt
        echo "Start time: $(date -d @$start_time)" >> Report.txt
        echo "End time: $(date -d @$end_time)" >> Report.txt
        echo "Download time: ${download_time} seconds" >> Report.txt
        echo "Download details:" >> Report.txt
        echo "$wget_output" >> Report.txt
        echo "----------------------------------------" >> Report.txt
        echo "Error: File download failed!"
    fi
else
    echo "Link not valid!"
    echo "<$URL> not a valid URL!" >> Report.txt
    echo "----------------------------------------" >> Report.txt
fi

