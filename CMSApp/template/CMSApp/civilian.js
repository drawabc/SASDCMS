// Function that enables submission of form or rejection of form
checker = true;
function disableSubmit(){
  document.getElementById("submit").disabled = true;
}

function enableSubmit(){
  document.getElementById("submit").disabled = false;
}



function checkValid(id){
  var nric_regex = /^\w\d+\w$/;
  var name_regex = /^[a-zA-Z ]+$/;
  var mobile_regex = /^\+?\d{10}$/;
  var email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var mytag = document.getElementById(id);
  switch(id) {
  case "NRIC":
    var value = nric_regex.test(mytag.value);
    break;
  case "Name":
    var value = name_regex.test(mytag.value);
    break;
  case "Email":
    var value = email_regex.test(mytag.value);
    break;
  case "Mobile":
    var value = mobile_regex.test(mytag.value);
    break;
  default:
    // code block
  }
  var mylist = [];
  mylist.push(document.getElementById("NRIC"));
  mylist.push(document.getElementById("Name"));
  mylist.push(document.getElementById("Email"));
  mylist.push(document.getElementById("Mobile"));
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
document.getElementById("Mobile").addEventListener("focusout",function(){
  checkValid("Mobile");
});
document.getElementById("Name").addEventListener("focusout",function(){
  checkValid("Name");
});
document.getElementById("Email").addEventListener("focusout",function(){
  checkValid("Email");
});
document.getElementById("NRIC").addEventListener("focusout",function(){
  checkValid("NRIC");
});
