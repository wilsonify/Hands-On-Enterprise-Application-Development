// check if the localStorage is supported by the browser or not

if(localStorage) {
    // Put some contents inside the local storage
    localStorage.setItem("username", "joe_henry");
    localStorage.setItem("uid", "28372");
    // Retrieve some contents from the local storage
    var user_email = localStorage.getItem("user_email");
} else {
    alert("The browser does not support local web storage");
}

// check if the sessionStorage is supported by the browser or not
if(sessionStorage) {
  // Put some contents inside the local storage
  sessionStorage.setItem("username", "joe_henry");
  sessionStorage.setItem("uid", "28372");
  // Retrieve some contents from the session storage
  var user_email = sessionStorage.getItem("user_email");
} else {
  alert("The browser does not support session web storage");
}