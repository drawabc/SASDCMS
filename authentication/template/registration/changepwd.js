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
  //var username_regex = /^[a-zA-Z1-9]{8,150}$/;
  //var name_regex = /^\w+$/;
  //var email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var mytag = document.getElementById(id);
  switch(id) {
  case "oldpassword":
    //var value = username_regex.test(mytag.value);
    break;
  case "newpassword":
    var value = password_regex.test(mytag.value);
    break;
  case "newpassword2":
    var password = document.getElementById("newpassword");
    if (password.value != mytag.value){
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
  mylist.push(document.getElementById("newpassword"));
  mylist.push(document.getElementById("newpassword2"));
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
document.getElementById("newpassword").addEventListener("focusout",function(){
  checkValid("newpassword");
});
document.getElementById("newpassword2").addEventListener("focusout",function(){
  checkValid("newpassword2");
});
