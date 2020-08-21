import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { BasicAuthenticationService } from './basic-authentication.service';

@Injectable({
  providedIn: 'root'
})
export class RoutegaurdService implements CanActivate{

    constructor(public basicAuthenticationService: BasicAuthenticationService,
              private router: Router ) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot){
    if(this.basicAuthenticationService.isUserLoggedIn())
      console.log('User is logged in')
      return true;
    
    this.router.navigate(['login'])
    console.log('User is not logged in')
    return false;
  }
}
