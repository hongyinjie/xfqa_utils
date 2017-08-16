NUM_WORKER=1
BIND_ADDR=0.0.0.0:5040

#kill -s 9 `ps -aux | grep python | grep $BIND_ADDR | awk '{print $2}'`
sh stop.sh

LD_LIBRARY_PATH=".:./libs/x64" gunicorn -w $NUM_WORKER -b $BIND_ADDR -p gunicorn.pid -t 6000 ws_xfqa:app  >> log.xfqa.txt 2>&1  &
