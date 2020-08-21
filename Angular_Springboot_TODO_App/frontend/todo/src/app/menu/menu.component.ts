import { Component, OnInit } from '@angular/core';
import { BasicAuthenticationService } from '../service/basic-authentication.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  constructor(public basicAuthenticationService: BasicAuthenticationService) { }

  username:string;

  ngOnInit() {
    this.username = this.basicAuthenticationService.getAuthenticatedUser();
  }

}
