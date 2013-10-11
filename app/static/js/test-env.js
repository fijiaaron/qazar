function validateForm(){
	var name=document.forms["myForm"]["name"].value;
	var email=document.forms["myForm"]["email"].value;
	var phone=document.forms["myForm"]["phone"].value;
	var company=document.forms["myForm"]["company"].value;
	var fname=document.forms["user_profile"]["fname"].value;
	var lname=document.forms["user_profile"]["lname"].value;
	var phone1=phone;

	var atpos=email.indexOf("@");
	var dotpos=email.lastIndexOf(".");

	if (name=="")
	{
		alert("Please fill out your first name.");
		name.focus();
		return false;
	}
	if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
	{
	    alert("Not a valid e-mail address.");
	    email.focus();
	    return false;
	}
	if (fname=="")
	{
		alert("Please enter your first name.");
		fname.focus;
		return false;
	}
	if (lname=="")
	{
		alert("Please enter your last name.");
		lname.focus;
		return false;
	}
	if (phone)
};

function splitNames(e){
	var splitName = e.value.split(" ");
	var lastname = splitName[splitName.length-1];
	var firstnames = "";
	for(var i=0; i<splitName.length-1; i++)
	{
		firstnames += splitName[i] + "";	
	}

	document.getElementById("fname").value = firstnames;
	document.getElementById("lname").value = lastname;
};

function autoFill(){
	
}