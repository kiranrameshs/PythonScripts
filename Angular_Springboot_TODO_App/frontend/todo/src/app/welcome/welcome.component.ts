import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  name = ''
  //Activated route

  constructor(private route:ActivatedRoute) { }

  ngOnInit(){
    // console.log(this.route.snapshot.params['name'])
    this.name = this.route.snapshot.params['name']
  }

}
