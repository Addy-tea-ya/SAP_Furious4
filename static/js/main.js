var url="http://localhost:5000/";
var junc=[];
function send()
{
        var data = {};
        data.junction1 = [];
        
        var json = JSON.stringify(data);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader('Content-type','application/json; charset=utf-8');
        xhr.onload = function () {
            
            var users = JSON.parse(xhr.responseText);
            var rec=JSON.parse(xhr.responseText);
            junc=rec['task']['junction1'];
            alert(junc);
        if (xhr.readyState == 4 && xhr.status == "201") {
        console.table(users);
        } else {
        console.error(users);
        }
        }
    
    xhr.send(json);
}