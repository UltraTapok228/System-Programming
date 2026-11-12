import subprocess,sys,time
from pathlib import Path
path=str(Path(__file__).parent/'worker.py');children=[]
def launch(mode):
    p=subprocess.Popen([sys.executable,path,'--mode',mode,'--seconds','60']);children.append(p)
    print(f'{mode}: PID={p.pid}',flush=True);return p
try:
    a=launch('growth');b=launch('steady')
    time.sleep(12)
    print('Перезапускаю один процесс',flush=True)
    a.terminate();a.wait(timeout=4)
    a=launch('growth');time.sleep(20)
finally:
    for p in children:
        if p.poll() is None:
            p.terminate()
            try:p.wait(timeout=3)
            except subprocess.TimeoutExpired:p.kill()
