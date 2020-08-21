import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {BasicAuthenticationService} from './../service/basic-authentication.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username = ''
  password = ''
  errormessage = 'Invalid Credentials'
  invalidLogin = false
  
  

  constructor(private router: Router,
    private basicAuthenticationService: BasicAuthenticationService ) { }

  ngOnInit() {
  }

    handleJWTAuthLogin() {
      this.basicAuthenticationService.executeJWTAuthenticationService(this.username, this.password)
          .subscribe(
            data => {
              console.log(data)
              this.invalidLogin = false
              console.log("Authentication successful")
              this.router.navigate(['welcome', this.username])
              console.log("Calling welcome page")      
            },
            error => {
              console.log(error)
              this.invalidLogin = true
            }
          )
    }

  

}
