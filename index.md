## Blaze8834

<head>
  </head>

  <body>
  <center><h1> Hey guys! </h1>
   Most people know me as Shredder_ or Blaze_, this is my website! Some of my hobbies are coding, playing video games, and chatting with friends on discord.</center>
  
<script>
  function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
 function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
  if (getCookie("name") == null) {
 var x = prompt("Please enter your name.");
  setCookie("name", x, 500000000000000);
} else {
   var name = getCookie("name");
   document.write("Welcome back "+name+"!")
                               
                               
                               
                               
