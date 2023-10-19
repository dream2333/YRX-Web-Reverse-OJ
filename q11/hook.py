import frida
import sys

#辅助用脚本，用于测试java层算法

with open(sys.path[0]+'/hook.js') as f:
    frida_script = f.read()

def on_message(message, data):
    print(message)
    print(data)


device = frida.get_usb_device()
pid = device.spawn(["com.yuanrenxue.onlinejudge2020"])
device.resume(pid)
session = device.attach(pid)
script = session.create_script(frida_script)
script.on("message", on_message)

script.load()
sys.stdin.read()