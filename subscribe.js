var PubNub = require('pubnub')
require('dotenv').config();

pubnub = new PubNub({
    publishKey : process.env.PUBNUB_PUBLISH_KEY,
    subscribeKey : process.env.PUBNUB_SUBSCRIBE_KEY
})

function callback(msg){
  if(typeof msg.message.action !== undefined){

    switch (msg.message.action) {
      case "capture":
        var duration = msg.message.duration;
        const { spawn } = require('child_process');
        const pyProg = spawn('python', ['capture.py', duration]);

        pyProg.stdout.on('data', function(data) {

            console.log(data.toString());
            res.write(data);
            res.end('end');
        });

        break;
      default:
        console.log("ERROR : Illegal action provided");
    }
  }
};

function subscribe() {

    pubnub.addListener({
        status: function(statusEvent) {
            if (statusEvent.category === "PNConnectedCategory") {
                console.log("Connected, Waiting for Message");
            }
        },
        message: function(msg) {
            console.log('Message Received, action =' + msg.message.action);
            callback(msg);
        },
        presence: function(presenceEvent) {
            // handle presence
        }
    })
    console.log("Subscribing..");
    pubnub.subscribe({
        channels: [process.env.PUBNUB_CHANNEL]
    });

};

subscribe();
