document.addEventListener("DOMContentLoaded", button());
function accept(req){
    var returnResponse = JSON.parse(req.responseText);
    var cityOutput = document.getElementById("outputCity");
    var tempOutput = document.getElementById("outputTemp");
    var humidOutput = document.getElementById("outputHumid");
    var weatherOutput = document.getElementById("outputWeather");
    cityOutput.textContent = returnResponse["name"];
    if (returnResponse["main"]["temp"] > 273.15){
        returnResponse["main"]["temp"] -= 273.15 
    }
    tempOutput.textContent = Math.round(returnResponse["main"]["temp"]);
    humidOutput.textContent = returnResponse["main"]["humidity"];
    weatherOutput.textContent = returnResponse["weather"][0]["main"];
}
function button(){
    var apiKey = 'fa7d80c48643dfadde2cced1b1be6ca1';
    var cityZipInput = document.getElementById("cityOrZipInput");
    var countryInput = document.getElementById("countryInput");    
    var button1 = document.getElementById("form1Submit");
    var button2 = document.getElementById("form2Submit");
    button2.addEventListener("click", function(event){
        var req = new XMLHttpRequest();
        var payload = {value:null};
        payload.value = document.getElementById("textArea").value;
        req.open("POST","http://httpbin.org/post",true);
        req.setRequestHeader("Content-Type","application/json")
        req.addEventListener("load", function(){
            document.getElementById("textArea").value = null;
            document.getElementById("textArea").setAttribute("placeholder", "Enter Text Here...");
            if (req.status >= 200 && req.status < 400){
                var response = JSON.parse(req.responseText);
                var newResponse = JSON.parse(response["data"]);
                document.getElementById("textOutput").textContent = newResponse["value"];
            }else{
                alert("Error: Invalid Submission - Form 2")
            }
        })
        req.send(JSON.stringify(payload));
        event.preventDefault();
    })
    button1.addEventListener("click", function(event){
        var req = new XMLHttpRequest();
        req.open("GET",`http://api.openweathermap.org/data/2.5/weather?q=${cityZipInput.value},${countryInput.value}&units=metric,&appid=${apiKey}`,true);
        req.addEventListener("load", function(){           
            if (req.status >= 200 && req.status < 400 && cityZipInput.value != "" && countryInput.value != ""){
                cityZipInput.value = null;
                countryInput.value = null;
                accept(req);
            }else{
                alert("Invalid Search - Form 1")
            }
        })
        req.send(null);
        event.preventDefault();
    })
}