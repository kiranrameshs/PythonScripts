import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

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
    //console.log("hello world bean service")
    return (this.http.get<helloWorldPathVariable>(`http://localhost:8080/hello-world/path-variable/${name}`));

  }
}

