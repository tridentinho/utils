#!/usr/bin/env node
API_BASE = process.env.API_BASE;
TOKEN = process.env.TOKEN;
NAMESPACE = process.env.NAMESPACE;

const socket = require('socket.io-client')(`${API_BASE}${NAMESPACE}`, {extraHeaders: {
    authorization: TOKEN
  }});
const someDelay = 10;
socket.on('connect', function () {
    console.log('connected...');
    if (process.argv[2] && process.argv[3]) {
        console.log('sending ' + process.argv[2] + ': ' + process.argv[3]);
        socket.emit('command', {'automation':process.argv[2], 'command':process.argv[3]});
        setTimeout(() => {
            process.exit(0);  
        }, someDelay);
    } else {
        console.log('usage: ./client.js <automation> <command>');
        process.exit(1);
    }
});