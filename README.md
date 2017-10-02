Message aggregater
===
This is a utility class for message aggregation. In stream socket communication like TCP, there is no message delimiter in the protocol level. The Message class provides a function of finding a message block.

## Usage

Make an instance of Message class and put data into the instance by recv() method. After that, calling parse() method will returns the message block if it has received enough data to resume the message.

## Example

code snippet is below.

```
import message_aggregater


buf = []
message_agg = message_aggregater.Message()

while True:
    buf = sock.recv(8192)  # receive from stream socket
    if len(buf) == 0:
        sock.close()
        break
    message_agg.recv(buf)
    while True:
        msg = message_agg.parse()
        if msg is None:
            break
        ** do something on msg here**
```

## Licence

[MIT](LICENCE)

## Author

[quvox](https://github.com/quvox)
