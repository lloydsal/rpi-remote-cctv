var PubNub = require('pubnub')

var channel = "cctv";

pubnub = new PubNub({
    publishKey : 'pub-c-4f10f066-06e2-4211-9a1c-7586daf79629',
    subscribeKey : 'sub-c-cb88f1a4-cfaf-11e4-9de3-02ee2ddab7fe'
})
function publish() {
    pubnub.publish(
    {
        message : {
            action: "capture",
            duration: 10
        },
        channel: channel,
        sendByPost: false, // true to send via post
        storeInHistory: false, //override default storage options
        meta: {
            "cool": "meta"
        }   // publish extra meta with the request
    },
    function (status, response) {
        if (status.error) {
            // handle error
            console.log(status)
        } else {
            console.log("message Published\n timetoken", response.timetoken)
        }
    }
  );
};

publish();
