// Function that enables submission of form or rejection of form
checker = true;
function disableSubmit(){
  document.getElementById("submit").disabled = true;
}

function enableSubmit(){
  document.getElementById("submit").disabled = false;
}



function checkValid(id){
  var password_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,20}$/;
  var username_regex = /^[a-zA-Z1-9]{8,150}$/;
  var name_regex = /^\w+$/;
  var email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var mytag = document.getElementById(id);
  switch(id) {
  case "email":
    var value = email_regex.test(mytag.value);
    break;
  case "username":
    var value = username_regex.test(mytag.value);
    break;
  case "password":
    var value = password_regex.test(mytag.value);
    break;
  case "password2":
    var password = document.getElementById("password");
    if (password.value != password2.value){
      var value = false;
    }
    else{
      var value = true;
    }
    break;
  case "firstname":
      var value = name_regex.test(mytag.value);
    break;
  case "lastname":
      var value = name_regex.test(mytag.value);
    break;
  default:
    // code block
  }
  var mylist = [];
  mylist.push(document.getElementById("username"));
  mylist.push(document.getElementById("password"));
  mylist.push(document.getElementById("password2"));
  mylist.push(document.getElementById("firstname"));
  mylist.push(document.getElementById("lastname"));
  mylist.push(document.getElementById("email"));
  if (value){
    mytag.classList.remove("is-invalid");
    mytag.classList.add("is-valid");
      }
  else{
    mytag.classList.add("is-invalid");
    mytag.classList.remove("is-valid");
  }
  for (i=0;i<mylist.length;i++){
    if (mylist[i].classList.contains("is-invalid")){
      checker = false;
      break;
    }
    checker = true;
  }
  if (checker){
    enableSubmit();
  }
  else{
    disableSubmit();
  }
}


// Adding event that checks if input is valid
document.getElementById("username").addEventListener("focusout",function(){
  checkValid("username");
});
document.getElementById("email").addEventListener("focusout",function(){
  checkValid("email");
});
document.getElementById("password").addEventListener("focusout",function(){
  checkValid("password");
});
document.getElementById("password2").addEventListener("focusout",function(){
  checkValid("password2");
});
document.getElementById("firstname").addEventListener("focusout",function(){
  checkValid("firstname");
});
document.getElementById("lastname").addEventListener("focusout",function(){
    checkValid("lastname");
});
