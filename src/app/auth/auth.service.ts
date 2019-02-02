import * as firebase from 'firebase';

export class AuthService {
  signupUser(email:string, password: string) {
    //console.log('authService ka signupUser method called');
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .catch(
        error => console.log(error)
      )
  }
}
