let {auth} = require("google-auth-library");
const mailField = document.getElementById('mail');
const labels = document.getElementsByTagName('label');
const resetPassword = document.getElementById('resetPassword');
const successModal = document.querySelector('.success');
const failureModal = document.querySelector('.failure');

const firebase = {
  apiKey: "AIzaSyBfTC04mTX6MhbvS61ixHrM7oFLrlwMfUY",
  authDomain: "cs3-st.firebaseapp.com",
  databaseURL: "https://cs3-st-default-rtdb.firebaseio.com",
  projectId: "cs3-st",
  storageBucket: "cs3-st.appspot.com",
  messagingSenderId: "94001336639",
  appId: "1:94001336639:web:442c48169e52ed0744c38a",
  measurementId: "G-DGLQBLKH36"
};
auth = firebase.auth();
// const auth = firebase

//auth.languageCode = 'DE_de';

auth.useDeviceLanguage();

const resetPasswordFunction = () => {
    const email = mailField.value;

    auth.sendPasswordResetEmail(email)
    .then(() => {
        console.log('Password Reset Email Sent Successfully!');
    })
    .catch(error => {
        console.error(error);
    })
}


resetPassword.addEventListener('click', resetPasswordFunction);

//Animations
mailField.addEventListener('focus', () => {
    labels.item(0).className = "focused-field";
});

mailField.addEventListener('blur', () => {
    if(!mailField.value)
        labels.item(0).className = "unfocused-field";
});