import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username = 'kiran'
  password = ''
  errormessage = 'Invalid Credentials'
  invalidLogin = false;
  
  
  //Router instancce
  //using dependency injection, just need to declare it as a dependency

  constructor(private router: Router) { }

  ngOnInit() {
  }

  handleLogin(){
    // console.log(this.username)
    if(this.username==="kiran" && this.password==='dummy'){
      //redirect to welcome page
      this.router.navigate(['welcome',this.username])
      this.invalidLogin=false}
      else{
        this.invalidLogin=true
      }
    }
  

}
