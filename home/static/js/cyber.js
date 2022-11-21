let signup = document.form
let username = document.form.username
let fname = document.form.first_name
let lname = document.form.last_name
let email = document.form.email
let state = document.form.state
let phone = document.form.phone
let address = document.form.address
let password = document.form.password

let validate = () =>{
    if(username.value.length <=0){
        alert('Please, Supply username');
        username.focus()
        return form;
    }

    if(fname.value.length <=0){
        alert('Please, Supply first name');
        fname.focus()
        return form;
    }

    if(lname.value.length <=0){
        alert('Please,Supply last name');
        lname.focus()
        return form;
    }

    if(email.value.length <=0){
        alert('Please,Supply Email Address');
        email.focus()
        return form;
    }

    if(state.value.length <=0){
        alert('Please,Supply State');
        state.focus()
        return form;
    }

    if(phone.value.length <=0){
        alert('Please,Supply Phone Number');
        phone.focus()
        // return form;
    }

    if(address.value.length <=0){
        alert('Please,Supply Home Address');
        address.focus()
        // return form;
    }
}



