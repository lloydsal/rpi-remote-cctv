var PubNub = require('pubnub')

var channel = "cctv";

pubnub = new PubNub({
    publishKey : 'pub-c-4f10f066-06e2-4211-9a1c-7586daf79629',
    subscribeKey : 'sub-c-cb88f1a4-cfaf-11e4-9de3-02ee2ddab7fe'
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
        channels: [channel]
    });

};

subscribe();
