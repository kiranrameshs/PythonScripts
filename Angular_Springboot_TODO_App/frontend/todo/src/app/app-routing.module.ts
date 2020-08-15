import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { ErrorComponent } from './error/error.component';
import { ListTodosComponent } from './list-todos/list-todos.component';
import { LogoutComponent } from './logout/logout.component';
import {RoutegaurdService} from './service/routegaurd.service'
import { from } from 'rxjs';

//welcome
const routes: Routes = [
  {path:'',component: LoginComponent},
  {path:'login',component: LoginComponent},
  {path:'welcome/:name',component: WelcomeComponent, canActivate:[RoutegaurdService]},
  {path:'todos',component: ListTodosComponent,canActivate:[RoutegaurdService]},
  {path:'logout',component: LogoutComponent,canActivate:[RoutegaurdService]},
  {path:'**',component: ErrorComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
