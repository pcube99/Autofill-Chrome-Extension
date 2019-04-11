// // Copyright 2018 The Chromium Authors. All rights reserved.
// // Use of this source code is governed by a BSD-style license that can be
// // found in the LICENSE file.

// 'use strict';
//  let page = document.getElementById('buttonDiv');
// const kButtonColors = ['#3aa757', '#e8453c', '#f9bb2d', '#4688f1'];
// function constructOptions(kButtonColors) {
//   for (let item of kButtonColors) {
//     let button = document.createElement('button');
//     button.style.backgroundColor = item;
//     button.addEventListener('click', function() {
//       chrome.storage.sync.set({color: item}, function() {
//         console.log('color is ' + item);
//       })
//     });
//     page.appendChild(button);
//   }
// }


// constructOptions(kButtonColors);

// function httpGetAsync(theUrl, callback)
// {
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.onreadystatechange = function() { 
//         if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
//             callback(xmlHttp.responseText);
//     }
//     console.log(xmlHttp.responseText)
//     xmlHttp.open("GET", theUrl, false); // true for asynchronous 
//     xmlHttp.send(null);
// }

// document.addEventListener('DOMContentLoaded', function() {
//   document.getElementById("buttonlogin").addEventListener("click", myFunctio);
// });
// function myFunctio(){
//    var email = document.getElementById("linklogin").value;
//    var password =  document.getElementById("linkpassword").value;
//    console.log(email);
//    httpGetAsync(("https://afss.herokuapp.com/login?email=" + email +"&password=" + password), function(response) {
//   var ans=response
//    console.log(JSON.parse(ans)[0])['first_name'];
// });
// }


// var urlfor;
// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById("linkb").addEventListener("click", myFunction);
//   });
// function myFunction(){
//      urlfor = document.getElementById("link").value;
//      console.log(urlfor);
//      httpGetAsync(("https://afss.herokuapp.com/autofill?url=" + urlfor), function(response) {
//     var ans=response
//      console.log(JSON.parse(ans)[0]);
// });
// }




//   // opens a communication port
//   chrome.runtime.onConnect.addListener(function(port) {

//     // listen for every message passing throw it
//     port.onMessage.addListener(function(o) {
  
//         // if the message comes from the popup
//         if (o.from && o.from === 'popup' && o.start && o.start === 'Y') {
  
//             // inserts a script into your tab content
//             chrome.tabs.executeScript(null, {
  
//                 // the script will click the button into the tab content
//                 code: "document.getElementById('link').setAttribute('value', 'panikil);"
//             });
//         }
//     });
//   });