import { Component, OnInit } from '@angular/core';
import {TodoDataService} from '../service/data/todo-data.service'
import { Router } from '@angular/router';
import { BasicAuthenticationService } from '../service/basic-authentication.service';

export class Todo{
  constructor(
    public id: number,
    public description: string,
    public done: boolean,
    public targetDate:Date ){
  }
}


@Component({
  selector: 'app-list-todos',
  templateUrl: './list-todos.component.html',
  styleUrls: ['./list-todos.component.css']
})
export class ListTodosComponent implements OnInit {

  todos: Todo[]

  message: string;
  username: string;

  constructor(private todoservice: TodoDataService,
    private router: Router,
    private basicAuthenticationService: BasicAuthenticationService) { }

  ngOnInit() {
    this.username = this.basicAuthenticationService.getAuthenticatedUser()
    this.refreshTodos();
    console.log('username in list-todos is '+this.username)
  }

  refreshTodos() {
    this.todoservice.retrieveAllTodos(this.username).subscribe(
      response => {
        console.log(response);
        this.todos = response;
      }
    )
  }

  handleDeleteTodo(id){
    this.todoservice.deleteTodo(this.username,id).subscribe(
      response => {
        console.log(response);
        this.message = `Delete of ${id} Successful`;
        this.refreshTodos();
      }
    )
  }

  handleUpdateTodo(id){
      this.router.navigate(['todos',id])
      }

      handleAddTodo(){
        this.router.navigate(['todos',-1])
      }



}
