var PubNub = require('pubnub')
require('dotenv').config();

pubnub = new PubNub({
    publishKey : process.env.PUBNUB_PUBLISH_KEY,
    subscribeKey : process.env.PUBNUB_SUBSCRIBE_KEY
})
function publish() {
    pubnub.publish(
    {
        message : {
            action: "capture",
            duration: 10
        },
        channel: process.env.PUBNUB_CHANNEL,
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
