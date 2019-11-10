const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 5678 });

let socks = []

wss.on('connection', function connection(ws) {

  socks.push(ws);

  ws.on('message', function incoming(message) {
    console.log('echoing: %s', message);
    socks.forEach((sock) => {
      sock.send(message);
    })
  });

});
