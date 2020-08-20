import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BasicAuthenticationService } from '../basic-authentication.service';

@Injectable({
  providedIn: 'root'
})
export class HttpIntercepterBasicAuthService implements HttpInterceptor{

  constructor(private basicAuthenticationService: BasicAuthenticationService) { }
  
  
  
  intercept(request: HttpRequest<any>, next: HttpHandler){
    // let username = 'kiran'
    // let password = 'dummy'
    //let basicauthHeaderString = 'Basic ' + window.btoa(username + ':' + password);
    let basicAuthHeaderString = this.basicAuthenticationService.getAuthenticatedToken();
    let username = this.basicAuthenticationService.getAuthenticatedUser();
    console.log('basicAuthHeaderString is '+basicAuthHeaderString+'  username is '+username)
    if(basicAuthHeaderString && username){
      request = request.clone({
        setHeaders : {
          Authorization: basicAuthHeaderString
        }
      })
    }
      return next.handle(request);
    }

  
}
