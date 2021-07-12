

class index {
  constructor() {
    this.te = require('./test.js')
    this.bindEvents();
  }

  bindEvents() {
    document.addEventListener('deviceready', onDeviceReady, false);
    console.log(this.te);
  }
}

new index();





// function onDeviceReady() {
//   // Cordova is now initialized. Have fun!

//   console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
//   document.getElementById('deviceready').classList.add('ready');
// }


// var app = {
//     // Application Constructor
//     initialize: function() {
//         this.bindEvents();
//     },
//     // Bind Event Listeners
//     //
//     // Bind any events that are required on startup. Common events are:
//     // 'load', 'deviceready', 'offline', and 'online'.
//     bindEvents: function() {
//         document.addEventListener('deviceready', this.onDeviceReady, false);
//     },
//     // deviceready Event Handler
//     //
//     // The scope of 'this' is the event. In order to call the 'receivedEvent'
//     // function, we must explicitly call 'app.receivedEvent(...);'
//     onDeviceReady: function() {
//         app.receivedEvent('deviceready');
//     },
//     // Update DOM on a Received Event
//     receivedEvent: function(id) {
//         var parentElement = document.getElementById(id);

//         console.log('Received Event: ' + id);
//     }
// };
