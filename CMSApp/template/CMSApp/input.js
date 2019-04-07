// Function that enables submission of form or rejection of form
checker = true;
function disableSubmit(){
  document.getElementById("submit").disabled = true;
}

function enableSubmit(){
  document.getElementById("submit").disabled = false;
}

function checkValid(id){
  var postal_regex = /^\d{6}$/;
  var name_regex = /^[a-zA-Z ]+$/;
  var mobile_regex = /^\+?\d{10}$/;
  var mytag = document.getElementById(id);
  switch(id) {
  case "name_1":
    var value = name_regex.test(mytag.value);
    break;
  case "postalCode":
    var value = postal_regex.test(mytag.value);
    break;
  case "mobilenum":
    var value = mobile_regex.test(mytag.value);
    break;
  default:
    // code block
  }
  var mylist = [];
  mylist.push(document.getElementById("name_1"));
  mylist.push(document.getElementById("name_1"));
  mylist.push(document.getElementById("postalCode"));
  mylist.push(document.getElementById("mobilenum"));
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
document.getElementById("mobilenum").addEventListener("focusout",function(){
  checkValid("mobilenum");
});
document.getElementById("name_1").addEventListener("focusout",function(){
  checkValid("name_1");
});
document.getElementById("postalCode").addEventListener("focusout",function(){
  checkValid("postalCode");
});
