// VALIDATE EMAIL BEFORE ADDING TO EMAIL LIST
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
var mail = document.getElementById("subscribeMail");
var mailbutton = document.getElementById("subscribeBtn");
var mailErr = document.getElementById("subscribeErr");
var subscribeEmail = new FormData();
mailErr.style.marginTop = "-15px";
mailErr.style.marginBottom = "10px";
mailErr.style.display = "none";
mailErr.style.textAlign = "left";

$(document).on('click', '#subscribeBtn', function(e) {
    // VALIDATE EMAIL
    if (mail.value !== "") {
        if (mail.value.match(mailformat) == null) {
            emailCorrect = 0;
            mailErr.style.display = "block";
            mailErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter a valid email!';

        } else {
            subscribeEmail.append('email', $('#subscribeMail').val());
            subscribeEmail.append('action', 'subscribe');
            subscribeEmail.append('csrfmiddlewaretoken', '{{ csrf_token }}');

            $.ajax({
                type: 'POST',
                url: '{% "subscribe" %}',
                data: subscribeEmail,
                cache: false,
                processData: false,
                contentType: false,
                enctype: 'multipart/form-data',
                success: function (){
                    mail.innerHTML= "";
                    mailErr.style.color = "#fff";
                    mailErr.style.display = "block";
                    mailErr.innerHTML = "<b style='color:'#fff';'>Subscription Sucessful!</b>";
                    setTimeout(() => {
                        mailErr.style.innerHTML = "";
                        mailErr.style.display = "none";
                    }, 3000)
                },error: function (xhr, errmsg, err) {
                    console.log(xhr.status + ":" + xhr.responseText);
                }
            });
            
        }
    } else {
        emailCorrect = 0;
        mailErr.style.display = "block";
        mailErr.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Please enter your email address!';
    }
})