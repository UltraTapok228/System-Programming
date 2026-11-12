import argparse,time,os
p=argparse.ArgumentParser();p.add_argument('--mode',choices=['steady','growth'],required=True);p.add_argument('--seconds',type=int,default=60);a=p.parse_args()
start=time.monotonic();blocks=[]
print(f'PID={os.getpid()} mode={a.mode}',flush=True)
while time.monotonic()-start<min(a.seconds,120):
    if a.mode=='growth' and len(blocks)<35: blocks.append(bytearray(1024*1024))
    time.sleep(0.7)
