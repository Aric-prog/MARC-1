credential = $1;

ffmpeg -f video4linux2 -i /dev/video0 -c:v libx264 -an -f flv rtmp://marc0.jasoncoding.com/marc1live/$credential