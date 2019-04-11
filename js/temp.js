function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    console.log(xmlHttp.responseText)
    xmlHttp.open("GET", theUrl, false); // true for asynchronous 
    xmlHttp.send(null);
}
/*
chrome.storage.local.get(['islogin'], function(result) {
  if(result.islogin){
    document.getElementById('container').style.display = "none";
    document.getElementById('logined').style.display = "block";
  }
else{
  document.getElementById('container').style.display = "block";
  document.getElementById('logined').style.display = "none";
}
  
});*/
document.addEventListener('DOMContentLoaded', documentEvents  , false);
document.addEventListener('DOMContentLoaded', documentEvents1  , false);
document.addEventListener('DOMContentLoaded', documentEvents2  , false);
var email;
var password;
var login_response;
function myAction(email, pass) { 
  email = email.value;
  password = pass.value;
  console.log(email);
  console.log(password);
  httpGetAsync(("https://afss.herokuapp.com/login?email=" + email +"&password=" + password), function(response) {
  login_response=response;
  if(login_response){
    console.log(login_response);
    //chrome.storage.local.get({islogin:}, function(result) {
      chrome.storage.local.set({islogin: true}, function(value) {
        console.log('Value is set to ' + value);
        var islogin;
        chrome.storage.local.get(['islogin'], function(result) {
         console.log(result);
          if(result.islogin){
        document.getElementById('container').style.display = "none";
        document.getElementById('logined').style.display = "block";
          }
        else{
          document.getElementById('container').style.display = "block";
        document.getElementById('logined').style.display = "none";
        }
          
        });     
      });
  }
});
}
function documentEvents() {    
  document.getElementById('ok_btn').addEventListener('click', 
    function() { myAction(document.getElementById('name_textbox'), document.getElementById('pass_textbox'));
  });
  console.log("gg guyzz");
  // you can add listeners for other objects ( like other buttons ) here 
}

var url;
function documentEvents1() {    
  document.getElementById('autofill_btn').addEventListener('click', 
    function() { 
      chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
        url = tabs[0].url;
    });
    console.log(url);
    httpGetAsync(("https://afss.herokuapp.com/autofill?url=" + url), function(response) {
  var ans=response;
  var keys = JSON.parse(ans)[1];
  var data = JSON.parse(ans)[0];
  var data1 = JSON.parse(ans)[1];
  if(ans){
    var count=0;
    for(var i in data){
      if(data.hasOwnProperty(i))
      count++;
    }
    console.log("count " + count);
    
    console.log(data1)
    var flag = [];
    for(var i =0;i<count;i++){
      flag.push(0);
    }
    console.log(flag);
    console.log("dat length " + data.length);
    for (var i=0;i<count;i=i++){
      for(var j=0;j<data.length;j++){
        if(data[j]['area-label'].includes(data1[i]) || data[j]['dname'].includes(data1[i]) || data[j]['name'].includes(data1[i]) ){
         // console.log(data1[i])
          if(flag[j]==0){ 
            flag[j] = 1;
            console.log(data[j]['dname'].includes(data1[i]));
            console.log(JSON.parse(login_response)[i][data1[i]]);
            var dta = JSON.parse(login_response)[i][data1[i]];
            chrome.storage.local.set({d1 : data[j]['id']},function(){
              console.log("fuck off");
              chrome.storage.local.set({d2: dta},function(){
                console.log("fuck");
                chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
                  console.log("yuppe");
                  chrome.storage.local.get(['d1'],function(result1){
                    chrome.storage.local.get(['d2'],function(result2){
                      console.log(i + " " + result1.d1);
                      console.log(i + " " + result2.d2);
                      chrome.tabs.executeScript(
                          tabs[0].id,
                          {code: "document.getElementById('"+result1.d1+"').value = '"+result2.d2+"';"});
                  });
                });    
              });
            });
          });
                     // document.getElementById(data[j]['id']).value = login_response[data1[i]];\
           
            break;
          }
        }
        
      }
    }
   
  }
});
  });
  console.log("gg guyzz");
  // you can add listeners for other objects ( like other buttons ) here 
}

function documentEvents2() {    
  document.getElementById('logout_btn').addEventListener('click', 
    function() { 
      console.log("logouted");
      chrome.storage.local.set({islogin: false}, function(value) {
        console.log('Value is set to ' + value);
        var islogin;
        chrome.storage.local.get(['islogin'], function(result) {
         console.log(result);
          if(result.islogin){
        document.getElementById('container').style.display = "none";
        document.getElementById('logined').style.display = "block";
          }
        else{
          document.getElementById('container').style.display = "block";
        document.getElementById('logined').style.display = "none";
        }
          
        });     
      });

  });
  // you can add listeners for other objects ( like other buttons ) here 
}


