import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { API_URL } from "./../../app.constants"
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
    return (this.http.get<HelloWorldBean>(`${API_URL}/hello-world-bean`));

  }

  executeHelloWorldBeanServiceWithVariable(name){
    return this.http.get<helloWorldPathVariable>(`${API_URL}/hello-world/path-variable/${name}`
    //,{headers}
    );

  }
}

