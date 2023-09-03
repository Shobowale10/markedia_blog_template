// REMOVE EXCESS MARGIN TOP FORM ERROERS PARARGRAPHS
var errors = document.querySelectorAll("#form p.text-danger");
for (i = 0; i < errors.length; i++) {
    errors[i].style.marginTop = "-20px";
}


// SELECT FORM INPUTS & ERRORS 
const form = {
    Reply: document.getElementById("mailreply"),
    button: document.getElementById("contact-button"),
    name: document.getElementById("name"),
    mail: document.getElementById("mail"),
    phone: document.getElementById("phone"),
    subject: document.getElementById("subject"),
    message: document.getElementById("message"),
    nameErr: document.getElementById("nameErr"),
    mailErr: document.getElementById("mailErr"),
    phoneErr: document.getElementById("phoneErr"),
    subjectErr: document.getElementById("subjectErr"),
    messageErr: document.getElementById("messageErr"),
    iframe: document.getElementById("iframe"),
}



// VALIDATE DATA BEFORE SENDING
if(form.button) {
    var nameCorrect = 1; var email = 1; var website = 1; var commentInput = 1;
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var phoneno = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?([0-9]{4})$/;

    form.button.addEventListener('click', () => {
        document.getElementById('form-row').scrollIntoView();

        // VALIDATE NAME
            if (form.name.value === "") {
                nameCorrect = 0;
                nameErr.style.display = "block";
                nameErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter your Name!';
            } else {
                nameCorrect = 1;
                nameErr.style.display = "none";
                nameErr.innerHTML = '';
            }

        // VALIDATE EMAIL
            if (form.mail.value !== "") {
                if (form.mail.value.match(mailformat) == null) {
                    emailCorrect = 0;
                    mailErr.style.display = "block";
                    mailErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter a valid email!';
                } else {
                    emailCorrect = 1;
                    mailErr.style.display = "none";
                    mailErr.innerHTML = '';
                }
            } else {
                emailCorrect = 0;
                mailErr.style.display = "block";
                mailErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter your email address!';
            }

        // VALIDATE PHONE NUMBER
            if (form.phone.value != "") {
                if (form.phone.value.match(phoneno) == false) {
                    phoneCorrect = 0;
                    phoneErr.style.display = "block";
                    phoneErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Your phone number can can only be numbers!';
                } else if (form.phone.value.length < 11) {
                    phoneCorrect = 0;
                    phoneErr.style.display = "block";
                    phoneErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Your phone number cannot be shorter than 11 digits!';
                } else if (form.phone.value.length > 14) {
                    phoneCorrect = 0;
                    phoneErr.style.display = "block";
                    phoneErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Your phone number cannot be greater than 14 digits!';
                } else {
                    phoneCorrect = 1;
                    phoneErr.style.display = "none";
                    phoneErr.innerHTML = '';
                }
            } else {
                phoneCorrect = 1;
            }

        // VALIDATE SUBJECT
            if (form.subject.value === "") {
                subjectCorrect = 0;
                subjectErr.style.display = "block";
                subjectErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter your subject for your mail!';
            } else {
                subjectCorrect = 1;
                subjectErr.style.display = "none";
                subjectErr.innerHTML = '';
            }

        // VALIDATE COMMENTS
            if (form.message.value === "") {
                messageInput = 0;
                messageErr.style.display = "block";
                messageErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter a message!';
            } else {
                messageInput = 1;
                messageErr.style.display = "none";
                messageErr.innerHTML = '';
            }


            // SEND MAIL IF DATA VALIDATION IS SUCCESSFUL
            if (nameCorrect === 1 & emailCorrect === 1 & phoneCorrect === 1 & subjectCorrect === 1 & messageInput === 1) {
                var myname = form.name.value;
                var mail = form.mail.value;
                var phone = form.phone.value;
                var subject = form.subject.value;
                var message = form.message.value;
                sendMail(myname, mail, phone, subject, message);
                
                const emptyVal = [    
                    form.name,
                    form.mail,
                    form.phone,
                    form.subject,
                    form.message,
                    form.nameErr,
                    form.mailErr,
                    form.phoneErr,
                    form.subjectErr,
                    form.messageErr,
                ];
                let i = 0;
                while (emptyVal[i]) {
                    emptyVal[i].value = "";
                    i++;
                }

                setTimeout(() => {
                    form.Reply.innerHTML = 'Mail has been sent sucessfully. We will get in touch with you!';
                }, 2000);
                
            } else {
                setTimeout(() => {
                    form.Reply.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please Check all Inputs';
                }, 4000);
            }
    })
}




// REGISTER FORM
function sendMail(myname, mail, phone, subject, message) {
        const requestContactMail = `name=${myname}email=${mail}&phone=${phone}&subject=${subject}&message=${message}`;
        var url = ("http://localhost/phpmailer/contact_email.php?name=" + myname + "&email=" + mail + "&phone=" + phone + "&subject=" + subject + "&message=" + message);
        form.iframe.src = url;
        console.log(form.iframe.src);
}

