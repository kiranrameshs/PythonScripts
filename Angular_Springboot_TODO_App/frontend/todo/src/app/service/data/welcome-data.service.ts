import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";

export class HelloWorldBean{
  constructor(public message:string) {}
}

export class helloWorldPathVariable{
  constructor(public message:string){}
}


@Injectable({
  providedIn: 'root'
})
export class WelcomeDataService {

  constructor(private http: HttpClient) { }

  executeHelloWorldBeanService(){
    //console.log("hello world bean service")
    return (this.http.get<HelloWorldBean>('http://localhost:8080/hello-world-bean'));

  }

  executeHelloWorldBeanServiceWithVariable(name){
    let basicauthHeaderString = this.createBasicAuthenticationHttpHeader();
    let headers = new HttpHeaders({Authorization:basicauthHeaderString })
    //console.log("hello world bean service")
    return this.http.get<helloWorldPathVariable>(`http://localhost:8080/hello-world/path-variable/${name}`,
    {headers});

  }

  createBasicAuthenticationHttpHeader(){
    let username = 'kiran'
    let password = 'dummy'
    let basicauthHeaderString = 'Basic ' + window.btoa(username + ':' + password);
    return basicauthHeaderString;
  }

  //Access to XMLHttpRequest at 'http://localhost:8080/hello-world/path-variable/kiran' from origin 'http://localhost:4200' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
//zone-evergreen.js:2845 GET http://localhost:8080/hello-world/path-variable/kiran net::ERR_FAILED
}

