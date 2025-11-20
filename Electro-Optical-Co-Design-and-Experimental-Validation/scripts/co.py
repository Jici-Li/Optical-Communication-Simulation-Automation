import socket
import numpy as np
import time

class MZMController:
    def __init__(self, host='127.0.0.1', port=5465):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self._send("INIT MZM Vpi=3.14")  
        assert self._recv() == "READY"
    
    def set_voltage(self, voltage):
        self._send(f"SET VOLTAGE {float(voltage):.4f}")
        return self._recv() == "OK"

    def _send(self, cmd):
        self.sock.sendall((cmd + '\n').encode())

    def _recv(self):
        return self.sock.recv(1024).decode().strip()

    def close(self):
        self.sock.close()

def sweep_voltage():
    mzm = MZMController()
    try:
        voltages = np.linspace(0, 3.14, 10)  
        dt = 0.1  
        
        for v in voltages:
            start_time = time.time()
            mzm.set_voltage(v) 
            elapsed = time.time() - start_time
            if elapsed < dt:
                time.sleep(dt - elapsed)
    finally:
        mzm.close()

if __name__ == "__main__":
    sweep_voltage()