import argparse, shlex, socket, subprocess, sys, textwrap, threading

class NetX:
    def __init__(self, args, buffer = None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # use IPv4 & TCP-socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))

        if self.buffer:
            self.socket.send(self.buffer)
        
        try:
            while 1:

                recv_len = 1
                response = ''

                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()

                    if recv_len < 4096:
                        break
                
                if response:
                    print(response)
                    try:
                        buffer = input('> ')
                    except EOFError:
                        print('input not received..')
                        break
                    buffer += '\n'
                    self.socket.send(buffer.encode())

        
        except KeyboardInterrupt:
            print('User terminated')
            self.socket.close()
            sys.exit()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)

        while 1:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(target = self.handle, args = (client_socket,))
            client_thread.start()

    def handle(self, client_socket):
        if self.args.run_command:
            output = run_command(self.args.run_command)
            client_socket.send(output.encode())

        elif self.args.upload:
            file_buffer = b''
            while 1:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)

            message = f'Saved file: {self.args.upload}'
            client_socket.send(message.encode())

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'$ >')
                    while '\n' not in cmd_buffer.decode(): 
                        cmd_buffer += client_socket.recv(64)
                    response = run_command(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server stopped {e}')
                    self.socket.close()
                    sys.exit()

def run_command(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr = subprocess.STDOUT)
    return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'NetX Net Tool', 
        formatter_class = argparse.RawDescriptionHelpFormatter,
        epilog = textwrap.dedent('''NetX Use Cases:
            netX.py -t 192.168.1.101 -p 5555 -l -c # command shell
            netX.py -t 192.168.1.101 -p 5555 -l -u=results.txt # download results
            netX.py -t 192.168.1.101 -p 5555 -l -r=\"cat info.txt\" # run command
            echo 'hello netX' | ./netX.py -t 192.168.1.101 -p 135 # send text to server port 135
            netX.py -t 192.168.1.101 -p 5555 # connecting to the server
            '''))
    parser.add_argument('-c', '--command', action='store_true', help = 'command shell')
    parser.add_argument('-r', '--run_command', help = 'run specified command')
    parser.add_argument('-l', '--listen', action = 'store_true', help = 'listen')
    parser.add_argument('-p', '--port', type = int, default = 5555, help = 'target port')
    parser.add_argument('-t', '--target', default = '192.168.1.101', help = 'target IP')
    parser.add_argument('-u', '--upload', help = 'upload file')

    args = parser.parse_args()

    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    

    nx = NetX(args, buffer.encode())
    nx.run()
