console.log("go go go")


chrome.runtime.onMessage.addListener(gotMessage);
function gotMessage(message, sender, sendResponse) {
    console.log(message.txt);
    if(message.txt == "hello"){
        console.log("sended");
    }
}