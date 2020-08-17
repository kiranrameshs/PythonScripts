import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpIntercepterBasicAuthService implements HttpInterceptor{

  constructor() { }
  intercept(request: HttpRequest<any>, next: HttpHandler){
    let username = 'kiran'
    let password = 'dummy'
    let basicauthHeaderString = 'Basic ' + window.btoa(username + ':' + password);
    request = request.clone({
      setHeaders : {
        Authorization: basicauthHeaderString
      }
    })
    return next.handle(request);
  }
  
}
