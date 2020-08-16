import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { WelcomeDataService } from "../service/data/welcome-data.service";

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  
  welcomeMessageFromService: string
  errormessageFromService: string
  name = ''
  //Activated route

  constructor(private route:ActivatedRoute,
    private service: WelcomeDataService) { }

  ngOnInit(){
    // console.log(this.route.snapshot.params['name'])
    this.name = this.route.snapshot.params['name']
  }

  getWelcomeMessage(){
    
    //console.log(this.service.executeHelloWorldBeanService());
    this.service.executeHelloWorldBeanService().subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    );
    //console.log("last line of getWelcomeMessage")
  }

  getWelcomeMessageWithParameter(){
    
    this.service.executeHelloWorldBeanServiceWithVariable(this.name).subscribe(
      response => this.handleSuccessfulResponse(response),
      error => this.handleErrorResponse(error)
    );
    //console.log("last line of getWelcomeMessage")
  }

  handleSuccessfulResponse(response){
  this.welcomeMessageFromService = response.message;
    //console.log(response.message);
  }

  handleErrorResponse(error){
    this.errormessageFromService = error.error.message;
  }

}
