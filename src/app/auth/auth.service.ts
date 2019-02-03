import * as firebase from 'firebase';

export class AuthService {
  signupUser(email:string, password: string) {
    //console.log('authService ka signupUser method called');
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .catch(
        error => console.log(error)
      )
  }

  signinUser(email: string, password: string) {
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then(
        response => console.log(response)
      )
      .catch(
        error => console.log(error)
      );
  }
}
