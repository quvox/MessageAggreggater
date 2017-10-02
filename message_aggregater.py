# -*- coding: utf-8 -*-
import struct


class Message:
    HEADER_LEN = 4

    def __init__(self):
        self.pending_buf = bytearray()
        self.is_new_chunk = True
        self.msg_body = None
        self.msg_len = 0

    def recv(self, dat):
        self.pending_buf.extend(dat)

    def parse(self):
        #print(" > pending_buf=%d,%d"%(len(self.pending_buf), Message.HEADER_LEN))
        if self.is_new_chunk:
            if len(self.pending_buf) < Message.HEADER_LEN:
                return None
            self.msg_len = struct.unpack("I", self.pending_buf[:Message.HEADER_LEN])[0]
            self.is_new_chunk = False
            self.msg_body = None
            #print("  >> msg_len=%d"%(self.msg_len))

        if self.msg_len == Message.HEADER_LEN:
            self.is_new_chunk = True
            self.msg_body = []
            self.pending_buf = self.pending_buf[self.msg_len:]
            #print("  --self.msg_len == Message.HEADER_LEN -->true")
            return None

        if self.msg_len > Message.HEADER_LEN and len(self.pending_buf) >= self.msg_len:
            self.is_new_chunk = True
            self.msg_body = self.pending_buf[Message.HEADER_LEN:self.msg_len]
            self.pending_buf = self.pending_buf[self.msg_len:]
            #print("  --self.msg_len > Message.HEADER_LEN -->true")
            return self.msg_body
        #print(" --->>> false")
        return None


def make_message(dat):
    dat = packer.pack(dat)
    msg = bytearray()
    msg.extend(struct.pack("I", len(dat) + 4))
    msg.extend(dat)
    return msg
